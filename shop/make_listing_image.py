"""商品画像1枚目: 完成した袋の写真を生成り色の背景に置き、バッジと短い言葉を添える(2000x2000)。"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps, ImageEnhance

ROOT = Path(__file__).parent
FONT = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
BG = (244, 239, 230)
INK = (60, 52, 48)
S = 2000


def cut(path, box, inset=6):
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    x0, y0, x1, y1 = box
    im = im.crop((x0 + inset, y0 + inset, x1 - inset, y1 - inset))
    # 紙の白を基準に明るさを合わせる(色みは変えない)
    import numpy as np
    a = np.asarray(im).astype(float)
    white = np.percentile(a.mean(axis=2), 90)
    a = np.clip(a * (240.0 / white), 0, 255).astype("uint8")
    return Image.fromarray(a)


def place(canvas, im, x, y, h, angle=0):
    im = im.resize((int(im.width * h / im.height), h), Image.LANCZOS).convert("RGBA")
    if angle:
        im = im.rotate(angle, expand=True, resample=Image.BICUBIC)
    sh = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    a = im.getchannel("A").point(lambda v: 70 if v else 0)
    sh.paste((60, 45, 30, 255), (x + 14, y + 20), a)
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18)))
    canvas.alpha_composite(im, (x, y))


def main(front, back, out, front_box, back_box):
    c = Image.new("RGBA", (S, S), BG + (255,))
    place(c, cut(back, back_box), 1060, 330, 1250, angle=-6)
    place(c, cut(front, front_box), 230, 250, 1450, angle=3)
    d = ImageDraw.Draw(c)
    badge = Image.open(ROOT.parent / "templates/listing/badge_download.png")
    badge = badge.resize((int(badge.width * 1.25), int(badge.height * 1.25)), Image.LANCZOS)
    c.alpha_composite(badge, (S - badge.width - 90, S - badge.height - 90))
    f = ImageFont.truetype(FONT, 78)
    d.text((110, S - 215), "印刷して作る ぽち袋", font=f, fill=INK)
    d.text((110, S - 120), "のし・文字違い 6種入り", font=ImageFont.truetype(FONT, 56), fill=INK)
    c.convert("RGB").save(out, quality=90)


if __name__ == "__main__":
    import sys
    img = "/tmp/claude-0/-home-user-my-first-repo/02cb9a5c-e2c2-5947-887e-aad52a1618eb/images/"
    main(img + "69.jpg", img + "68.jpg", ROOT / "listing_shiba_1.jpg",
         (227, 223, 932, 1286), (286, 284, 884, 1196))
    print("done")
