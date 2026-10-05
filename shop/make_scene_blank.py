"""Geminiに「白紙の袋」で作ってもらった場面写真に、本物の袋の絵を貼る。
白紙の袋の明るさ(影・紙のざらつき)をそのまま絵にかけるので、光が自然になる。
使い方: python3 make_scene_blank.py greatdane_1"""
import os
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).parent))
import make_listing_variants as mv

if os.environ.get("IMG_DIR"):  # この会話で受け取った画像の場所
    mv.D = Path(os.environ["IMG_DIR"])

HERE = Path(__file__).parent
# 名前: (場面の画像, [(貼る絵, 袋の四隅[左上・右上・右下・左下]), ...])
SCENES = {
    "greatdane_2": ("154.jpg", [
        # 左にうしろ、右におもて(ユーザーの案)。うしろの右端のしっぽと、おもての左端のおしりがつながって見える
        (HERE / "check/back_greatdane_final.png", [(203, 265), (470, 265), (472, 683), (201, 683)]),
        (HERE / "check/front_greatdane_final.png", [(502, 265), (765, 265), (770, 683), (500, 683)]),
    ]),
    "chipoo_1": ("165.jpg", [  # Geminiで袋を小さくした版(164.jpgは袋が大きすぎた)
        ("160.jpg", [(517, 548), (757, 548), (760, 936), (515, 939)]),
    ]),
    "munchkin_2": ("7.jpg", [  # ふたを閉じた表側の袋(プロンプトを直した版)。形が本物とほぼ同じなので、そのまま貼る
        ("1.jpg", [(665, 735), (844, 735), (848, 1005), (665, 1005)]),
    ]),
    "munchkin_1": ("5.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.58、本物は0.67)。絵がつぶれないように、
        # 絵は幅に合わせて袋の下にそろえ、上の余りは紙の白にした(check/front_munchkin_pad.png)
        (HERE / "check/front_munchkin_pad.png", [(1140, 822), (1516, 822), (1515, 1482), (1132, 1482)]),
    ]),
    "chatora_1": ("159.jpg", [
        ("155.jpg", [(648, 516), (886, 517), (885, 884), (639, 885)]),  # 無地のページの袋の表
    ]),
}

# 切り取る範囲(左, 上, 右, 下)。下の角のボタンを外す
CROP = {"greatdane_2": (52, 0, 907, 855)}
# 白紙の袋に細い線(ふたの折り目など)が写っているとき、光をこの半径でならして線を消す
SMOOTH = {"munchkin_1": 20, "munchkin_2": 8}


def coeffs(dst, src):
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
        B += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(B, float))


name = sys.argv[1]
scene_fn, items = SCENES[name]
scene = Image.open(mv.D / scene_fn).convert("RGB")
W, H = scene.size
out = np.asarray(scene).astype(float)
for art_path, quad in items:
    # 文字列ならCanvaのスクリーンショット(袋の表を切り出す)、Pathなら絵そのもの
    art = (mv.front(mv.D / art_path) if isinstance(art_path, str) else Image.open(art_path)).convert("RGB")
    aw, ah = art.size
    aa = np.asarray(art).astype(float)
    paper = np.median(aa[aa.min(2) > 200], axis=0)  # 絵の紙の白
    warped = np.asarray(art.transform((W, H), Image.PERSPECTIVE,
                                      coeffs(quad, [(0, 0), (aw, 0), (aw, ah), (0, ah)]), Image.BICUBIC,
                                      fillcolor=tuple(int(v) for v in paper))).astype(float)  # 絵の外は紙の白(黒い線を出さない)
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).polygon(quad, fill=255)
    inner = np.asarray(mask.filter(ImageFilter.MinFilter(5))) > 0
    # 白紙の袋の明るさ = 光と影(袋のふちの影は除いて、少しなめらかに)
    sc = np.asarray(scene.filter(ImageFilter.GaussianBlur(1.2))).astype(float)
    white = np.percentile(sc[inner], 99, axis=0)
    light = sc / white
    if name in SMOOTH:  # 袋の内側だけで光をならす(ふちの影や、となりの物の色を混ぜない)
        m = inner.astype(float)[..., None]
        r = SMOOTH[name]

        def blur(x):  # 箱形のぼかしを2回(ガウスぼかしに近い)
            for _ in range(2):
                for ax in (0, 1):
                    c = np.cumsum(np.pad(x, [(r + 1, r) if a == ax else (0, 0) for a in range(x.ndim)], mode="edge"), axis=ax)
                    x = (np.take(c, range(2 * r + 1, c.shape[ax]), axis=ax) - np.take(c, range(0, c.shape[ax] - 2 * r - 1), axis=ax)) / (2 * r + 1)
            return x
        bm = blur(m)  # 袋のふち(内側の外)も、内側の光でうめる
        light = np.where(bm > 0.05, blur(light * m) / np.maximum(bm, 1e-3), light)
    res = np.clip(warped / paper * light * white, 0, 255)
    al = (np.asarray(mask.filter(ImageFilter.GaussianBlur(0.7))).astype(float) / 255)[..., None]
    out = out * (1 - al) + res * al
res_im = Image.fromarray(out.astype(np.uint8))
if name in CROP:  # Geminiの画面のボタン(編集・共有)が写っているとき、正方形に切り取って外す
    res_im = res_im.crop(CROP[name])
res_im.save(HERE / f"scene_{name}.jpg", quality=92)
print("done", f"scene_{name}.jpg")
