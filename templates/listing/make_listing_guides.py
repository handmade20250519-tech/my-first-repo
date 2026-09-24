"""minneの商品画像(正方形)を Canva で作るための、配置ガイドとバッジ画像を作る。"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent
FONT_PATH = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
S = 2000  # 正方形の一辺(px)
INK = (64, 56, 51)
RED = (178, 60, 50)
ZONE = (225, 238, 250)
ZONE_LINE = (120, 160, 210)


def font(size):
    return ImageFont.truetype(FONT_PATH, size)


def label(d, box, text, size=48):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=ZONE, outline=ZONE_LINE, width=4)
    lines = text.split("\n")
    h = size * 1.4
    top = (y0 + y1) / 2 - h * len(lines) / 2
    for i, t in enumerate(lines):
        d.text(((x0 + x1) / 2, top + i * h + h / 2), t, font=font(size), fill=ZONE_LINE, anchor="mm")


def safe_frame(d):
    m = int(S * 0.05)
    d.rectangle((m, m, S - m, S - m), outline=(200, 200, 200), width=3)
    d.text((S / 2, m / 2), "この枠の外には大事なものを置かない(一覧で端が切れることがある)", font=font(34), fill=(160, 160, 160), anchor="mm")


def guide_main():
    im = Image.new("RGB", (S, S), "white")
    d = ImageDraw.Draw(im)
    safe_frame(d)
    label(d, (200, 200, 1800, 1500), "① 完成したぽち袋の写真\n(1枚、前面の絵を大きく)\n\n無地の明るい背景・自然光", 60)
    label(d, (1300, 1560, 1800, 1800), "② バッジ\n(badge_download.png)", 40)
    label(d, (200, 1560, 1240, 1800), "③ 短い言葉(任意)\n例: 印刷して作る ぽち袋", 44)
    im.save(OUT / "guide_1_main.png")


def guide_variants():
    im = Image.new("RGB", (S, S), "white")
    d = ImageDraw.Draw(im)
    safe_frame(d)
    label(d, (200, 170, 1800, 330), "見出し: 文字違い6種入り", 56)
    names = ["1 のしのみ", "2 おとしだま", "3 ありがとう", "4 おめでとう", "5 こころばかり", "6 無地(手書き用)"]
    w, h, gx, gy = 460, 640, 110, 80
    for i, n in enumerate(names):
        c, r = i % 3, i // 3
        x = 200 + c * (w + gx)
        y = 400 + r * (h + gy)
        label(d, (x, y, x + w, y + h), f"{n}\n\n仕上がりの\n画像", 40)
    im.save(OUT / "guide_2_variants.png")


def badge():
    w, h = 560, 200
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((4, 4, w - 4, h - 4), radius=40, fill=(255, 255, 255, 235), outline=RED, width=8)
    d.text((w / 2, 72), "ダウンロード商品", font=font(64), fill=RED, anchor="mm")
    d.text((w / 2, 145), "紙の袋はお届けしません", font=font(38), fill=INK, anchor="mm")
    im.save(OUT / "badge_download.png")


if __name__ == "__main__":
    guide_main()
    guide_variants()
    badge()
    print("done")
