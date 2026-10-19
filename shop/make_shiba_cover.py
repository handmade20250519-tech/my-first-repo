"""柴犬の商品画像1枚目(デザイン見本)を、ほかの種類と同じ形で作り直す。
もとのCanvaのスクリーンショットが手元にないので、6種類の画像(listing_shiba_3.jpg)から袋の表を切り出して使う。"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).parent
BG, INK = (244, 239, 230), (60, 52, 48)
FONT = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
S = 2000
src = Image.open(ROOT / "listing_shiba_3.jpg").convert("RGB")
# make_listing_variants.main の並べ方: w=468, h=695, 横のすき間110, 上290, 左はし188
w, h = 468, 695
def cell(i):
    x = 188 + i * (w + 110)
    return src.crop((x + 2, 290 + 2, x + w - 2, 290 + h - 2))
noshi, otoshi = cell(0), cell(1)

c = Image.new("RGBA", (S, S), BG + (255,))
d = ImageDraw.Draw(c)
f = lambda n: ImageFont.truetype(FONT, n)


def card(im, hh, angle):
    im = im.resize((int(im.width * hh / im.height), hh), Image.LANCZOS).convert("RGBA")
    return im.rotate(angle, expand=True, resample=Image.BICUBIC)


def put(im, x, y):
    sh = Image.new("RGBA", c.size, (0, 0, 0, 0))
    a = im.getchannel("A").point(lambda v: 70 if v else 0)
    sh.paste((60, 45, 30, 255), (x + 14, y + 20), a)
    c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18)))
    c.alpha_composite(im, (x, y))


put(card(noshi, 1250, -6), 1000, 300)
put(card(otoshi, 1450, 3), 230, 230)
badge = Image.open(ROOT.parent / "templates/listing/badge_download.png")
badge = badge.resize((int(badge.width * 1.25), int(badge.height * 1.25)), Image.LANCZOS)
c.alpha_composite(badge, (S - badge.width - 90, S - badge.height - 90))
d.text((110, S - 215), "印刷して作る ぽち袋", font=f(78), fill=INK)
d.text((110, S - 120), "のし・文字違い 6種入り", font=f(56), fill=INK)
d.text((S - 60, 50), "デザイン見本", font=f(44), fill=INK, anchor="ra")
c.convert("RGB").save(ROOT / "listing_shiba_1.jpg", quality=90)
print("done")
