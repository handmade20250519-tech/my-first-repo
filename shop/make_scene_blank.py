"""Geminiに「白紙の袋」で作ってもらった場面写真に、本物の袋の絵を貼る。
白紙の袋の明るさ(影・紙のざらつき)をそのまま絵にかけるので、光が自然になる。
使い方: python3 make_scene_blank.py greatdane_1"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).parent))
import make_listing_variants as mv

HERE = Path(__file__).parent
# 名前: (場面の画像, [(貼る絵, 袋の四隅[左上・右上・右下・左下]), ...])
SCENES = {
    "greatdane_2": ("154.jpg", [
        # 左にうしろ、右におもて(ユーザーの案)。うしろの右端のしっぽと、おもての左端のおしりがつながって見える
        (HERE / "check/back_greatdane_final.png", [(203, 265), (470, 265), (472, 683), (201, 683)]),
        (HERE / "check/front_greatdane_final.png", [(502, 265), (765, 265), (770, 683), (500, 683)]),
    ]),
    "chipoo_1": ("164.jpg", [
        ("160.jpg", [(443, 421), (821, 419), (829, 981), (438, 987)]),
    ]),
    "chatora_1": ("159.jpg", [
        ("155.jpg", [(648, 516), (886, 517), (885, 884), (639, 885)]),  # 無地のページの袋の表
    ]),
}

# 切り取る範囲(左, 上, 右, 下)。下の角のボタンを外す
CROP = {"greatdane_2": (52, 0, 907, 855)}


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
                                      coeffs(quad, [(0, 0), (aw, 0), (aw, ah), (0, ah)]), Image.BICUBIC)).astype(float)
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).polygon(quad, fill=255)
    inner = np.asarray(mask.filter(ImageFilter.MinFilter(5))) > 0
    # 白紙の袋の明るさ = 光と影(袋のふちの影は除いて、少しなめらかに)
    sc = np.asarray(scene.filter(ImageFilter.GaussianBlur(1.2))).astype(float)
    white = np.percentile(sc[inner], 99, axis=0)
    light = sc / white
    res = np.clip(warped / paper * light * white, 0, 255)
    al = (np.asarray(mask.filter(ImageFilter.GaussianBlur(0.7))).astype(float) / 255)[..., None]
    out = out * (1 - al) + res * al
res_im = Image.fromarray(out.astype(np.uint8))
if name in CROP:  # Geminiの画面のボタン(編集・共有)が写っているとき、正方形に切り取って外す
    res_im = res_im.crop(CROP[name])
res_im.save(HERE / f"scene_{name}.jpg", quality=92)
print("done", f"scene_{name}.jpg")
