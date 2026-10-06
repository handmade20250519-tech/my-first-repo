"""はみ出す構図の検証: Canvaの型の上に置いた絵を、組み立てたときの
おもて・うしろの見え方にして、隠れる部分を赤で示す。
使い方: python3 check_wraparound.py 145.png greatdane [x0,y0,x1,y1]
画像はCanvaの型(案内つき)の左の袋1つ分。袋のおもての四角を自動で探す。"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).parent))
import make_listing_variants as mv

if __import__("os").environ.get("IMG_DIR"):  # この会話で受け取った画像の場所
    mv.D = Path(__import__("os").environ["IMG_DIR"])

FLAP_L, FLAP_R, FRONT_W, FRONT_H, TOP, BOTTOM = 44, 32, 64, 95, 20, int(__import__("os").environ.get("POCHI_BOTTOM", 25))
LID_IN, LID_TIP = 2, 6
FONT = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
R = 10  # 出力の1mmあたりのピクセル

src_name, tag = sys.argv[1], sys.argv[2]
img = np.asarray(Image.open(mv.D / src_name).convert("RGB")).astype(int)
H, W, _ = img.shape

# 袋のおもての折り線(灰色の破線)を探す
g = (img.max(2) < 190) & (img.min(2) > 90) & ((img.max(2) - img.min(2)) < 20)
cols = g[int(H * .25):int(H * .8)].sum(0)
xs = np.argsort(cols)[::-1]
x0, x1 = sorted([xs[0], next(x for x in xs if abs(x - xs[0]) > W * .2)])
rows = g[:, x0 + 20:x1 - 20].sum(1)
ys = np.argsort(rows)[::-1]
y0, y1 = sorted([ys[0], next(y for y in ys if abs(y - ys[0]) > H * .2)])
if len(sys.argv) > 3:  # 自動で見つからないときは x0,y0,x1,y1 を渡す
    x0, y0, x1, y1 = map(int, sys.argv[3].split(","))
sx, sy = (x1 - x0) / FRONT_W, (y1 - y0) / FRONT_H


def sample(xf, yf):
    """おもて基準のmm座標 → 画像の色"""
    px = np.clip((x0 + xf * sx).astype(int), 0, W - 1)
    py = np.clip((y0 + yf * sy).astype(int), 0, H - 1)
    return img[py, px]


def inside(poly, x, y):
    """点が多角形の中にあるか(レイキャスト法)"""
    res = np.zeros(x.shape, bool)
    n = len(poly)
    for k in range(n):
        (xa, ya), (xc, yc) = poly[k], poly[(k + 1) % n]
        cross = ((ya > y) != (yc > y)) & (x < (xc - xa) * (y - ya) / (yc - ya + 1e-12) + xa)
        res ^= cross
    return res


F1 = [(0, 0), (-FLAP_L, 3), (-FLAP_L, FRONT_H - 3), (0, FRONT_H)]
F2 = [(FRONT_W, 0), (FRONT_W + FLAP_R, 3), (FRONT_W + FLAP_R, FRONT_H - 3), (FRONT_W, FRONT_H)]
F3 = [(0, FRONT_H), (FRONT_W, FRONT_H), (FRONT_W - 3, FRONT_H + BOTTOM), (3, FRONT_H + BOTTOM)]
F4 = [(LID_IN, 0), (FRONT_W - LID_IN, 0), (FRONT_W - LID_TIP, -TOP), (LID_TIP, -TOP)]

# うしろから見た座標(xb, yb mm) → 各折り返しの元の座標
yb, xb = np.mgrid[0:FRONT_H * R, 0:FRONT_W * R] / R + 0.5 / R
layers = [  # 下から上の順(①→②→③→④)
    ("①", F1, xb - FRONT_W, yb),
    ("②", F2, xb + FRONT_W, yb),
    ("③", F3, FRONT_W - xb, 2 * FRONT_H - yb),
    ("④", F4, FRONT_W - xb, -yb),
]
back = np.full(xb.shape + (3,), 238)  # おもての裏(何も印刷されない)
top = np.full(xb.shape, -1)
for i, (_, poly, xf, yf) in enumerate(layers):
    m = inside(poly, xf, yf)
    col = sample(xf, yf)
    back[m] = col[m]
    top[m] = i

# 展開図の上で、組み立てると隠れる部分(下の層に回る部分)
uy, ux = np.mgrid[-TOP * R:(FRONT_H + BOTTOM) * R, -FLAP_L * R:(FRONT_W + FLAP_R) * R] / R + 0.5 / R
art = sample(ux, uy)
is_art = ((art.max(2) - art.min(2)) > 18) | (art.max(2) < 90)
hidden = np.zeros(ux.shape, bool)
for i, (_, poly, _, _) in enumerate(layers):
    m = inside(poly, ux, uy)
    if not m.any():
        continue
    # その点がうしろのどこに来るか
    if i == 0: bx, by = ux + FRONT_W, uy
    elif i == 1: bx, by = ux - FRONT_W, uy
    elif i == 2: bx, by = FRONT_W - ux, 2 * FRONT_H - uy
    else: bx, by = FRONT_W - ux, -uy
    ix = np.clip((bx * R).astype(int), 0, FRONT_W * R - 1)
    iy = np.clip((by * R).astype(int), 0, FRONT_H * R - 1)
    covered = top[iy, ix] > i
    hidden |= m & covered & is_art
net = art.copy()
net[hidden] = (net[hidden] * 0.3 + np.array([230, 30, 30]) * 0.7).astype(int)

front = sample(*np.meshgrid(np.arange(FRONT_W * R) / R, np.arange(FRONT_H * R) / R))

# 1枚にまとめる
f = ImageFont.truetype(FONT, 34)
fr = Image.fromarray(front.astype(np.uint8))
bk = Image.fromarray(back.astype(np.uint8))
nt = Image.fromarray(net.astype(np.uint8))
pad = 40
Wc = nt.width + fr.width + bk.width + pad * 4
Hc = max(nt.height, fr.height) + 140
c = Image.new("RGB", (Wc, Hc), (250, 248, 244))
d = ImageDraw.Draw(c)
x = pad
for im, label in [(nt, "展開図(赤=組み立てると隠れる絵)"), (fr, "組み立てたおもて"), (bk, "組み立てたうしろ")]:
    c.paste(im, (x, 100))
    d.rectangle((x - 1, 99, x + im.width, 100 + im.height), outline=(180, 170, 160))
    d.text((x, 40), label, font=f, fill=(60, 52, 48))
    x += im.width + pad
fr.save(Path(__file__).parent / "check" / f"front_{tag}.png")
bk.save(Path(__file__).parent / "check" / f"back_{tag}.png")  # 場面写真に貼る用
out = Path(__file__).parent / "check" / f"wrap_{tag}.png"
c.save(out)
print(out, "隠れる絵のピクセル数:", int(hidden.sum()), "front box", x0, y0, x1, y1)
