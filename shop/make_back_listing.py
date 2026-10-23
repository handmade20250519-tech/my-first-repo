"""はみ出す絵(大型犬など)の商品画像: 組み立てた「うら」(左)と「おもて」(右)を並べる。2000x2000。
check_wraparound.py が作った check/front_<名前>.png と check/back_<名前>.png を使う。
使い方: python3 make_back_listing.py husky しっぽ   → listing_husky_5.jpg"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

import make_listing_extra as ex

ROOT = Path(__file__).parent
name, part = sys.argv[1], sys.argv[2]
S = ex.S
c = Image.new("RGBA", (S, S), ex.BG + (255,))
d = ImageDraw.Draw(c)
d.text((S / 2, 120), f"裏を返すと、{part}の続きが", font=ex.f(88), fill=ex.INK, anchor="mm")
fr = Image.open(ROOT / "check" / f"front_{name}.png").convert("RGB")
bk = Image.open(ROOT / "check" / f"back_{name}.png").convert("RGB")
h = 1150
sc = h / fr.height
fr = fr.resize((int(fr.width * sc), h), Image.LANCZOS)
bk = bk.resize((int(bk.width * sc), h), Image.LANCZOS)
# うらを左、おもてを右に置く(グレート・デーンの場面写真と同じ並び)。うらの右はしに回った絵が、
# すぐとなりのおもての左はしにつながって見える
gap = 60
x2 = (S - bk.width - gap - fr.width) // 2
x1 = x2 + bk.width + gap
y = 330
ex.shadow_paste(c, bk, x2, y)
ex.shadow_paste(c, fr, x1, y)
d.text((x2 + bk.width / 2, y + h + 60), "うら", font=ex.f(56), fill=ex.INK, anchor="mm")
d.text((x1 + fr.width / 2, y + h + 60), "おもて", font=ex.f(56), fill=ex.INK, anchor="mm")
d.text((S / 2, S - 110), "仕上がり 64×95mm ・ 一万円札を三つ折りにして入ります", font=ex.f(54), fill=ex.INK, anchor="mm")
c.convert("RGB").save(ROOT / f"listing_{name}_5.jpg", quality=90)
print("done", f"listing_{name}_5.jpg")
