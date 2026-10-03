"""場面写真(AIのイメージ画像)の右下に、小さく注記を入れる。
使い方: python3 add_ai_note.py scene_americanshorthair_1.jpg"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
TEXT = "※AIで作ったイメージ画像です。袋の絵柄は実際の商品と同じです。"
for fn in sys.argv[1:]:
    p = Path(__file__).parent / fn
    im = Image.open(p).convert("RGBA")
    W, H = im.size
    f = ImageFont.truetype(FONT, max(14, W // 48))
    d0 = ImageDraw.Draw(im)
    x0, y0, x1, y1 = d0.textbbox((0, 0), TEXT, font=f)
    pad = W // 100
    bw, bh = x1 - x0 + pad * 2, y1 - y0 + pad * 2
    bx, by = W - bw - pad * 2, H - bh - pad * 2
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=pad, fill=(255, 255, 255, 200))
    d.text((bx + pad - x0, by + pad - y0), TEXT, font=f, fill=(60, 52, 48, 255))
    im = Image.alpha_composite(im, ov).convert("RGB")
    im.save(p.with_name(p.stem + "_note.jpg"), quality=92)
    print(p.stem + "_note.jpg")
