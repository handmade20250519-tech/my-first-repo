"""トイプードルの商品画像(1枚目のデザイン見本)。"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import sys
sys.path.insert(0, str(Path(__file__).parent))
import make_listing_variants as mv

ROOT = Path(__file__).parent
BG, INK = (244, 239, 230), (60, 52, 48)
FONT = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
S = 2000
c = Image.new("RGBA", (S, S), BG + (255,))
d = ImageDraw.Draw(c)
f = lambda n: ImageFont.truetype(FONT, n)


def card(fn, h, angle):
    im = mv.front(mv.D / fn)
    im = im.resize((int(im.width * h / im.height), h), Image.LANCZOS).convert("RGBA")
    return im.rotate(angle, expand=True, resample=Image.BICUBIC)


def put(im, x, y):
    sh = Image.new("RGBA", c.size, (0, 0, 0, 0))
    a = im.getchannel("A").point(lambda v: 70 if v else 0)
    sh.paste((60, 45, 30, 255), (x + 14, y + 20), a)
    c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18)))
    c.alpha_composite(im, (x, y))


put(card("107.jpg", 1250, -6), 1000, 300)
put(card("108.jpg", 1450, 3), 230, 230)
badge = Image.open(ROOT.parent / "templates/listing/badge_download.png")
badge = badge.resize((int(badge.width * 1.25), int(badge.height * 1.25)), Image.LANCZOS)
c.alpha_composite(badge, (S - badge.width - 90, S - badge.height - 90))
d.text((110, S - 215), "印刷して作る ぽち袋", font=f(78), fill=INK)
d.text((110, S - 120), "のし・文字違い 6種入り", font=f(56), fill=INK)
d.text((S - 60, 50), "デザイン見本", font=f(44), fill=INK, anchor="ra")
c.convert("RGB").save(ROOT / "listing_toypoodle_1.jpg", quality=90)
print("done")


# 6種類の画像は、おめでとう・こころばかりの画像がそろってから作る
if len(sys.argv) > 2:  # 例: python3 make_toypoodle_images.py 111.jpg 110.jpg
    mv.main([("107.jpg", "のしのみ"), ("108.jpg", "おとしだま"), ("109.jpg", "ありがとう"),
             (sys.argv[1], "おめでとう"), (sys.argv[2], "こころばかり"), ("106.jpg", "無地(手書き用)")],
            "listing_toypoodle_3.jpg")
