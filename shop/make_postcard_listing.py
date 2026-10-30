"""商品画像: ポストカード2種(絵いっぱい・手紙用)の見本。2000x2000。
make_postcard.py が作った postcard/postcard_<名前>_<タイプ>.pdf から作る。
使い方: python3 make_postcard_listing.py shiba        → listing_shiba_postcard.jpg
        python3 make_postcard_listing.py dachshund yoko (横向きのとき)"""
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw

import make_listing_extra as ex

ROOT = Path(__file__).parent


def card(pdf, h):
    """PDFを画像にして、高さ h にそろえる"""
    with tempfile.TemporaryDirectory() as t:
        subprocess.run(["pdftoppm", "-r", "150", "-png", "-singlefile", str(pdf), f"{t}/p"], check=True)
        im = Image.open(f"{t}/p.png").convert("RGB")
    return im.resize((round(im.width * h / im.height), h), Image.LANCZOS)


def main(name, yoko=False):
    S = ex.S
    c = Image.new("RGBA", (S, S), ex.BG + (255,))
    d = ImageDraw.Draw(c)
    d.text((S / 2, 120), "ポストカード 2種類付き", font=ex.f(96), fill=ex.INK, anchor="mm")
    d.text((S / 2, 230), "はがき用紙にそのまま印刷できます(100×148mm)", font=ex.f(50), fill=ex.INK, anchor="mm")
    suffix = "_yoko" if yoko else ""
    cards = [(card(ROOT / "postcard" / f"postcard_{name}_{k}{suffix}.pdf", 680 if yoko else 1300), label)
             for k, label in (("full", "飾る・贈る"), ("letter", "お手紙に"))]
    if yoko:  # 横長は上下に並べる
        y = 330
        for im, label in cards:
            x = (S - im.width) // 2
            ex.shadow_paste(c, im, x, y)
            d.text((S / 2, y + im.height + 45), label, font=ex.f(56), fill=ex.INK, anchor="mm")
            y += im.height + 150
    else:
        gap = 120
        x = (S - sum(im.width for im, _ in cards) - gap) // 2
        for im, label in cards:
            ex.shadow_paste(c, im, x, 360)
            d.text((x + im.width / 2, 360 + im.height + 80), label, font=ex.f(60), fill=ex.INK, anchor="mm")
            x += im.width + gap
    out = ROOT / f"listing_{name}_postcard.jpg"
    c.convert("RGB").save(out, quality=92)
    print("done:", out.name)


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        raise SystemExit(__doc__)
    main(sys.argv[1], len(sys.argv) == 3 and sys.argv[2] == "yoko")
