"""黒猫の商品画像(1枚目のデザイン見本と、3枚目の6種類)。"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import os
import sys
sys.path.insert(0, str(Path(__file__).parent))
import make_listing_variants as mv

mv.D = Path(os.environ.get("IMG_DIR", "/tmp/claude-0/-home-user/068ade54-c79c-53ef-8da1-36e19e767c22/images"))
# 2ページ分を1枚にまとめたスクリーンショットは、左右に切って使う
for n in ("18", "19"):
    im = Image.open(mv.D / f"{n}.jpg")
    w, h = im.size
    im.crop((0, 0, w // 2, h)).save(mv.D / f"{n}a.jpg", quality=95)
    im.crop((w // 2, 0, w, h)).save(mv.D / f"{n}b.jpg", quality=95)

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


put(card("18a.jpg", 1250, -6), 1000, 300)
put(card("18b.jpg", 1450, 3), 230, 230)
badge = Image.open(ROOT.parent / "templates/listing/badge_download.png")
badge = badge.resize((int(badge.width * 1.25), int(badge.height * 1.25)), Image.LANCZOS)
c.alpha_composite(badge, (S - badge.width - 90, S - badge.height - 90))
d.text((110, S - 215), "印刷して作る ぽち袋", font=f(78), fill=INK)
d.text((110, S - 120), "のし・文字違い 6種入り", font=f(56), fill=INK)
d.text((S - 60, 50), "デザイン見本", font=f(44), fill=INK, anchor="ra")
c.convert("RGB").save(ROOT / "listing_kuroneko_1.jpg", quality=90)

mv.main([("18a.jpg", "のしのみ"), ("18b.jpg", "おとしだま"), ("19a.jpg", "ありがとう"),
         ("19b.jpg", "おめでとう"), ("20.jpg", "こころばかり"), ("17.jpg", "無地(手書き用)")],
        "listing_kuroneko_3.jpg")
print("done")
