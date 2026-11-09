"""Canvaの「スマホ動画」(縦1080×1920)に入れる、もとの絵の下じき画像を作る。
横長の絵(ビションなど)は、そのままCanvaに入れると枠からはみ出るので、絵を枠の幅に収めて、
上(1行目の文字)と下(2行目の文字)をあけた縦長の画像にする。背景は白にそろえる。
使い方: python3 make_video_base.py <もとの絵> <名前> [--label "Bichon Frise"] [--scale 0.88]   → video_base/<名前>_video_base.png
--scale は、文字のまわりをもっとあけたいときに絵を小さくする割合。
--label を付けると、AIが絵に描いた名前を消して、Klee One で入れ直す(白くするときに細い字が欠けることがあるため)"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import make_postcard as mp

ROOT = Path(__file__).parent
W, H = 1080, 1920
SIDE = 70                 # 左右の余白(動かしたときに枠から出ないように)
TOP, BOTTOM = 0.16, 0.86  # 絵(名前を含む)を置く高さの範囲。文字は 0.065 と 0.885 から


LABEL_PX, GAP = 58, 50   # 名前の文字の大きさと、絵とのあいだ(px)


def main(src, name, label=None, scale=1.0):
    im = mp.whiten(Image.open(src).convert("RGB"))
    if label:
        im = mp.strip_name(im)
    art = im.crop(mp.art_box(im))
    font = ImageFont.truetype(str(mp.FONT), LABEL_PX)
    extra = GAP + font.getbbox("Ag")[3] if label else 0
    box_w, box_h = W - 2 * SIDE, int(H * (BOTTOM - TOP))
    k = min(box_w / art.width, (box_h - extra) / art.height) * scale
    art = art.resize((round(art.width * k), round(art.height * k)), Image.LANCZOS)
    c = Image.new("RGB", (W, H), "white")
    y = int(H * TOP) + (box_h - art.height - extra) // 2
    c.paste(art, ((W - art.width) // 2, y))
    if label:
        ImageDraw.Draw(c).text((W / 2, y + art.height + GAP), label, font=font, fill=mp.INK, anchor="ma")
    out = ROOT / "video_base"
    out.mkdir(exist_ok=True)
    p = out / f"{name}_video_base.png"
    c.save(p)
    print(f"done: {p.name}(絵 {art.width}×{art.height}px)")


if __name__ == "__main__":
    args = sys.argv[1:]
    label, scale = None, 1.0
    if "--label" in args:
        i = args.index("--label")
        label = args[i + 1]
        del args[i:i + 2]
    if "--scale" in args:
        i = args.index("--scale")
        scale = float(args[i + 1])
        del args[i:i + 2]
    if len(args) != 2:
        raise SystemExit(__doc__)
    main(*args, label=label, scale=scale)
