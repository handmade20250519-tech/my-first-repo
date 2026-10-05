"""マンチカンの商品画像(1枚目のデザイン見本)。"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import sys
sys.path.insert(0, str(Path(__file__).parent))
import make_listing_variants as mv

mv.D = Path("/tmp/claude-0/-home-user/068ade54-c79c-53ef-8da1-36e19e767c22/images")

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


put(card("2a.jpg", 1250, -6), 1000, 300)
put(card("2b.jpg", 1450, 3), 230, 230)
badge = Image.open(ROOT.parent / "templates/listing/badge_download.png")
badge = badge.resize((int(badge.width * 1.25), int(badge.height * 1.25)), Image.LANCZOS)
c.alpha_composite(badge, (S - badge.width - 90, S - badge.height - 90))
d.text((110, S - 215), "印刷して作る ぽち袋", font=f(78), fill=INK)
d.text((110, S - 120), "のし・文字違い 6種入り", font=f(56), fill=INK)
d.text((S - 60, 50), "デザイン見本", font=f(44), fill=INK, anchor="ra")
c.convert("RGB").save(ROOT / "listing_munchkin_1.jpg", quality=90)
print("done")


# 6種類の画像は、こころばかりの画像がそろってから作る
if True:  # 例: python3 make_munchkin_images.py 144.jpg(こころばかり)
    mv.main([("2a.jpg", "のしのみ"), ("2b.jpg", "おとしだま"), ("3a.jpg", "ありがとう"),
             ("3b.jpg", "おめでとう"), ("4.jpg", "こころばかり"), ("1.jpg", "無地(手書き用)")],
            "listing_munchkin_3.jpg")
