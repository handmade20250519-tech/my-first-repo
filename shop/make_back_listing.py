"""はみ出す絵(大型犬など)の商品画像: 組み立てた「おもて」と「うら」を並べ、うらに回った絵を赤い丸で囲む。2000x2000。
check_wraparound.py が作った check/front_<名前>.png と check/back_<名前>.png を使う。
使い方: python3 make_back_listing.py husky しっぽ   → listing_husky_5.jpg"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

import make_listing_extra as ex

ROOT = Path(__file__).parent
name, part = sys.argv[1], sys.argv[2]
S = ex.S
c = Image.new("RGBA", (S, S), ex.BG + (255,))
d = ImageDraw.Draw(c)
d.text((S / 2, 120), f"裏を返すと、{part}の続きが", font=ex.f(88), fill=ex.INK, anchor="mm")
fr = Image.open(ROOT / "check" / f"front_{name}.png").convert("RGB")
bk = Image.open(ROOT / "check" / f"back_{name}.png").convert("RGB")
# うらに回った絵の場所(濃い色のかたまりのうち、いちばん大きいもの)
a = np.asarray(bk).astype(int)
lab, n = ndimage.label(ndimage.binary_dilation(a.min(2) < 190, iterations=6))
k = int(np.argmax(ndimage.sum(np.ones(lab.shape), lab, range(1, n + 1)))) + 1
ys, xs = np.nonzero(lab == k)
h = 1150
sc = h / fr.height
fr = fr.resize((int(fr.width * sc), h), Image.LANCZOS)
bk = bk.resize((int(bk.width * sc), h), Image.LANCZOS)
x1, y = 170, 330
x2 = S - 170 - bk.width
ex.shadow_paste(c, fr, x1, y)
ex.shadow_paste(c, bk, x2, y)
d.text((x1 + fr.width / 2, y + h + 60), "おもて", font=ex.f(56), fill=ex.INK, anchor="mm")
d.text((x2 + bk.width / 2, y + h + 60), "うら", font=ex.f(56), fill=ex.INK, anchor="mm")
cx, cy = x2 + (xs.min() + xs.max()) / 2 * sc, y + (ys.min() + ys.max()) / 2 * sc
rx, ry = max(110, (xs.max() - xs.min()) / 2 * sc + 50), max(80, (ys.max() - ys.min()) / 2 * sc + 45)
d.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), outline=ex.RED, width=8)
d.text((S / 2, S - 110), "仕上がり 64×95mm ・ 一万円札を三つ折りにして入ります", font=ex.f(54), fill=ex.INK, anchor="mm")
c.convert("RGB").save(ROOT / f"listing_{name}_5.jpg", quality=90)
print("done", f"listing_{name}_5.jpg")
