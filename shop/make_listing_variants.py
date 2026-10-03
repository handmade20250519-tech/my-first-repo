"""商品画像: 6種類(のしのみ・おとしだま・ありがとう・おめでとう・こころばかり・無地)を並べる。
Canvaの画面のスクリーンショットから、左の袋の表だけを切り出す。"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).parent
D = Path("/tmp/claude-0/-home-user-my-first-repo/02cb9a5c-e2c2-5947-887e-aad52a1618eb/images")
FONT = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
BG, INK = (244, 239, 230), (60, 52, 48)
S = 2000
ITEMS = [("78.jpg", "のしのみ"), ("81.jpg", "おとしだま"), ("79.jpg", "ありがとう"),
         ("80.jpg", "おめでとう"), ("76.jpg", "こころばかり"), ("77.jpg", "無地(手書き用)")]


def front(path):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(int)
    g = (a.max(axis=2) < 200) & (a.min(axis=2) > 80) & ((a.max(axis=2) - a.min(axis=2)) < 25)
    H, W = g.shape
    best = (0, 0, 0)
    for y in range(int(H * 0.03), int(H * 0.4)):
        xs = np.nonzero(g[y, : W // 2])[0]
        if len(xs) < 100:
            continue
        r = max(np.split(xs, np.nonzero(np.diff(xs) > 3)[0] + 1), key=len)
        if len(r) > best[0]:
            best = (len(r), y, r[0])
    L, y, x = best
    k = L / 52.0
    x0, y0 = x - 6 * k, y + 20 * k
    pad = 1.2 * k  # 折り目の線を入れない
    return im.crop((int(x0 + pad), int(y0 + pad), int(x0 + 64 * k - pad), int(y0 + 95 * k - pad)))


def main(items=ITEMS, out="listing_shiba_3.jpg"):
    c = Image.new("RGBA", (S, S), BG + (255,))
    d = ImageDraw.Draw(c)
    f = lambda n: ImageFont.truetype(FONT, n)
    d.text((S / 2, 110), "文字違い 6種類入り", font=f(92), fill=INK, anchor="mm")
    d.text((S / 2, 215), "使いたいページだけ印刷できます", font=f(50), fill=INK, anchor="mm")
    w, h, gx, gy, top = 468, 695, 110, 160, 290
    left = (S - 3 * w - 2 * gx) // 2
    for i, (fn, label) in enumerate(items):
        im = front(D / fn).resize((w, h), Image.LANCZOS)
        x = left + (i % 3) * (w + gx)
        y = top + (i // 3) * (h + gy)
        sh = Image.new("RGBA", c.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).rectangle((x + 8, y + 12, x + w + 8, y + h + 12), fill=(60, 45, 30, 60))
        c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
        c.paste(im, (x, y))
        d.rectangle((x, y, x + w, y + h), outline=(215, 208, 198), width=2)
        d.text((x + w / 2, y + h + 55), label, font=f(46), fill=INK, anchor="mm")
    c.convert("RGB").save(ROOT / out, quality=90)


if __name__ == "__main__":
    main()
    print("done")
