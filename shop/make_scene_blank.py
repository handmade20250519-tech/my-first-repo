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
    "corgi_1": ("160.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.66)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_corgi_pad.png)
        (HERE / "check/front_corgi_pad.png", [(946, 706), (1151, 706), (1151, 1020), (943, 1017)]),
    ]),
    "beagle_1": ("159.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.66)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_beagle_pad.png)
        (HERE / "check/front_beagle_pad.png", [(966, 712), (1167, 712), (1166, 1020), (964, 1018)]),
    ]),
    "golden_1": ("158.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.64)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_golden_pad.png)
        (HERE / "check/front_golden_pad.png", [(975, 751), (1159, 751), (1160, 1041), (974, 1039)]),
    ]),
    "sabatora_1": ("156.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.62)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_sabatora_pad.png)
        (HERE / "check/front_sabatora_pad.png", [(971, 756), (1147, 756), (1146, 1044), (967, 1041)]),
    ]),
    "pomeranian_1": ("155.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.66)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_pomeranian_pad.png)
        (HERE / "check/front_pomeranian_pad.png", [(941, 719), (1146, 719), (1141, 1033), (932, 1032)]),
    ]),
    "dachshund_1": ("154.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.66)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_dachshund_pad.png)
        (HERE / "check/front_dachshund_pad.png", [(952, 674), (1168, 674), (1166, 1006), (948, 1002)]),
    ]),
    "westie_1": ("151.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.64)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_westie_pad.png)
        (HERE / "check/front_westie_pad.png", [(966, 701), (1169, 701), (1166, 1021), (960, 1019)]),
    ]),
    "bedlington_1": ("149.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.59)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_bedlington_pad.png)
        (HERE / "check/front_bedlington_pad.png", [(1010, 807), (1149, 807), (1148, 1048), (1006, 1046)]),
    ]),
    "russianblue_1": ("147.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.62)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_russianblue_pad.png)
        (HERE / "check/front_russianblue_pad.png", [(951, 742), (1152, 742), (1151, 1073), (943, 1070)]),
    ]),
    "akita_1": ("146.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.68)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_akita_pad.png)
        (HERE / "check/front_akita_pad.png", [(985, 741), (1174, 741), (1171, 1025), (979, 1021)]),
    ]),
    "pug_1": ("145.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.63)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_pug_pad.png)
        (HERE / "check/front_pug_pad.png", [(987, 582), (1172, 582), (1169, 883), (975, 880)]),
    ]),
    "norwegian_1": ("143.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.61)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_norwegian_pad.png)
        (HERE / "check/front_norwegian_pad.png", [(974, 791), (1162, 791), (1159, 1101), (968, 1099)]),
    ]),
    "sheltie_1": ("142.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.59)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_sheltie_pad.png)
        (HERE / "check/front_sheltie_pad.png", [(1006, 686), (1161, 686), (1158, 956), (995, 951)]),
    ]),
    "sabi_1": ("123.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.66)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_sabi_pad.png)
        (HERE / "check/front_sabi_pad.png", [(974, 771), (1150, 771), (1147, 1046), (966, 1041)]),
    ]),
    "labrador_1": ("122.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.63)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_labrador_pad.png)
        (HERE / "check/front_labrador_pad.png", [(972, 785), (1149, 785), (1148, 1074), (966, 1070)]),
    ]),
    "shihtzu_1": ("121.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.60)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_shihtzu_pad.png)
        (HERE / "check/front_shihtzu_pad.png", [(950, 703), (1156, 703), (1153, 1049), (945, 1044)]),
    ]),
    "husky_1": ("119.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.63)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_husky_pad.png)
        (HERE / "check/front_husky_pad.png", [(1015, 791), (1164, 791), (1162, 1033), (1006, 1030)]),
    ]),
    "cavalier_1": ("116.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.59)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_cavalier_pad.png)
        (HERE / "check/front_cavalier_pad.png", [(946, 668), (1123, 668), (1121, 974), (940, 970)]),
    ]),
    "kijitora_1": ("114.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.62)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_kijitora_pad.png)
        (HERE / "check/front_kijitora_pad.png", [(927, 652), (1122, 652), (1120, 969), (922, 966)]),
    ]),
    "chihuahua_1": ("111.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.59)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_chihuahua_pad.png)
        (HERE / "check/front_chihuahua_pad.png", [(910, 692), (1108, 692), (1106, 1034), (904, 1031)]),
    ]),
    "samoyed_1": ("94.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.60)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_samoyed_pad.png)
        (HERE / "check/front_samoyed_pad.png", [(974, 802), (1105, 802), (1104, 1023), (970, 1022)]),
    ]),
    "scottish_1": ("80.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.62)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_scottish_pad.png)
        (HERE / "check/front_scottish_pad.png", [(973, 791), (1116, 791), (1113, 1028), (965, 1026)]),
    ]),
    "british_1": ("72.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.60)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_british_pad.png)
        (HERE / "check/front_british_pad.png", [(940, 753), (1104, 757), (1098, 1036), (930, 1031)]),
    ]),
    "ragdoll_1": ("63.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.61)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_ragdoll_pad.png)
        (HERE / "check/front_ragdoll_pad.png", [(878, 702), (1068, 702), (1071, 1019), (875, 1019)]),
    ]),
    "mike_1": ("55.jpg", [  # 袋の形が本物とほぼ同じ(幅:高さ=0.68)なので、そのまま貼る
        ("49.jpg", [(845, 686), (1066, 686), (1067, 1013), (843, 1013)]),
    ]),
    "borzoi_1": ("45.jpg", [
        # Geminiの袋が本物より少し細長い(幅:高さ=0.64)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_borzoi_pad.png)
        (HERE / "check/front_borzoi_pad.png", [(913, 764), (1056, 765), (1057, 990), (910, 988)]),
    ]),
    "yorkie_1": ("38.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.58)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_yorkie_pad.png)
        (HERE / "check/front_yorkie_pad.png", [(822, 689), (1040, 689), (1041, 1066), (819, 1066)]),
    ]),
    "jackrussell_1": ("31.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.62)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_jackrussell_pad.png)
        (HERE / "check/front_jackrussell_pad.png", [(900, 716), (1147, 716), (1147, 1117), (897, 1116)]),
    ]),
    "afghan_1": ("26.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.61)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_afghan_pad.png)
        (HERE / "check/front_afghan_pad.png", [(987, 918), (1114, 918), (1114, 1128), (984, 1127)]),
    ]),
    "kuroneko_1": ("21.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.59)。絵がつぶれないよう、幅に合わせて下にそろえ、上の余りは紙の白(check/front_kuroneko_pad.png)
        (HERE / "check/front_kuroneko_pad.png", [(951, 689), (1127, 689), (1126, 991), (946, 990)]),
    ]),
    "bordercollie_2": ("14.jpg", [
        # 左にうしろ(ユーザーが撮った組み立てた袋の写真を clean_back_photo.py で整えたもの)、右におもて(おとしだま)
        (HERE / "check/back_bordercollie_photo.png", [(234, 341), (599, 341), (599, 912), (234, 912)]),
        (HERE / "check/front_bordercollie_otoshidama.png", [(656, 341), (1020, 341), (1020, 911), (656, 911)]),
    ]),
    "bordercollie_1": ("12.jpg", [  # ふたを閉じた表側の袋。木の箱に立てかけた袋
        ("8.jpg", [(882, 610), (1122, 610), (1119, 968), (877, 967)]),
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
SMOOTH = {"munchkin_1": 20, "munchkin_2": 8, "bordercollie_1": 8, "kuroneko_1": 8, "afghan_1": 6, "jackrussell_1": 8, "yorkie_1": 8, "borzoi_1": 6, "mike_1": 8, "ragdoll_1": 8, "british_1": 8, "scottish_1": 6, "samoyed_1": 6, "chihuahua_1": 6, "kijitora_1": 6, "cavalier_1": 6, "husky_1": 6, "shihtzu_1": 6, "labrador_1": 6, "sabi_1": 6, "sheltie_1": 6, "norwegian_1": 6, "pug_1": 6, "akita_1": 6, "russianblue_1": 6, "bedlington_1": 6, "westie_1": 6, "dachshund_1": 6, "pomeranian_1": 6, "sabatora_1": 6, "golden_1": 6, "beagle_1": 6, "corgi_1": 6}


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
