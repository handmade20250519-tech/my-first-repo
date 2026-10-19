"""商品画像1枚目(デザイン見本)を、全種類まとめて作り直す。
minneの一覧では右下にお気に入り(ハート)ボタンが重なるので、「ダウンロード商品」のマークを左上に置き、右下は空ける。
袋の絵は、6種類の画像(listing_<名前>_3.jpg)の「のしのみ」と「おとしだま」から切り出す。
使い方: python3 make_covers.py            (全種類)
        python3 make_covers.py shiba chatora  (指定した種類だけ)"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).parent
BG, INK = (244, 239, 230), (60, 52, 48)
FONT = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
S = 2000
NAMES = ["shiba", "toypoodle", "wire", "frenchie", "italiangreyhound", "japanesemix", "maltipoo", "chipoo",
         "greatdane", "bordercollie", "jackrussell", "yorkie", "afghan", "borzoi", "samoyed", "hachiware",
         "americanshorthair", "chatora", "munchkin", "kuroneko", "mike", "ragdoll", "british", "scottish"]
f = lambda n: ImageFont.truetype(FONT, n)


def cells(name):
    """make_listing_variants.main の並べ方(w=468, h=695, 横のすき間110, 上290, 左はし188)で、
    のしのみ(1番目)とおとしだま(2番目)を切り出す"""
    src = Image.open(ROOT / f"listing_{name}_3.jpg").convert("RGB")
    w, h = 468, 695
    out = []
    for i in (0, 1):
        x = 188 + i * (w + 110)
        out.append(src.crop((x + 2, 290 + 2, x + w - 2, 290 + h - 2)))
    return out


def make(name):
    noshi, otoshi = cells(name)
    c = Image.new("RGBA", (S, S), BG + (255,))
    d = ImageDraw.Draw(c)

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
    badge = Image.open(ROOT.parent / "templates/listing/badge_download.png")  # 560x200 そのままの大きさ
    c.alpha_composite(badge, (60, 22))
    d.text((110, S - 215), "印刷して作る ぽち袋", font=f(78), fill=INK)
    d.text((110, S - 120), "のし・文字違い 6種入り", font=f(56), fill=INK)
    d.text((S - 60, 50), "デザイン見本", font=f(44), fill=INK, anchor="ra")
    c.convert("RGB").save(ROOT / f"listing_{name}_1.jpg", quality=90)


for n in (sys.argv[1:] or NAMES):
    make(n)
    print("done", n)
