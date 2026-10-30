"""もとの絵から、ハガキ(縦100×148mm)のポストカードPDFを作る。
Canvaでダウンロードすると絵が小さく(粗く)なるので、こちらで作る。

使い方: python3 make_postcard.py <絵の画像> <名前> full     (ハガキいっぱいに絵を入れる)
        python3 make_postcard.py <絵の画像> <名前> letter   (手紙用。左下に小さく絵を入れる)

作るもの: postcard/postcard_<名前>_<タイプ>.pdf と、確認用の postcard/postcard_<名前>_<タイプ>.jpg

絵の白い背景は切り落とし、絵の部分(白でないところ)の大きさで配置を決める。
大きさと位置は、ユーザーがCanvaで作ったラブラドールの2枚に合わせた。"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).parent
DPI = 350
W_MM, H_MM = 100, 148
MM = DPI / 25.4

# タイプごとの配置(mm)。full: 絵の幅83mmで、紙の真ん中。letter: 絵の幅41mmで、左から7mm・下から16mm
LAYOUT = {
    "full": {"width": 83, "left": None, "bottom": None},
    "letter": {"width": 41, "left": 7, "bottom": 16},
}
SAFE = 5  # 家のプリンターはふちまで印刷できないことが多いので、絵はふちから5mm以上離す


def art_box(im):
    """白い背景をのぞいた、絵の部分の範囲"""
    a = np.asarray(im.convert("L")) < 245
    ys, xs = np.nonzero(a)
    return xs.min(), ys.min(), xs.max() + 1, ys.max() + 1


def main(src, name, kind):
    lay = LAYOUT[kind]
    im = Image.open(src).convert("RGB")
    art = im.crop(art_box(im))
    w = round(lay["width"] * MM)
    h = round(art.height * w / art.width)
    if art.width < w:
        print(f"注意: もとの絵が小さい(絵の幅 {art.width}px。{DPI}dpiでは {w}px ほしい)。少しぼやけるかもしれない")
    art = art.resize((w, h), Image.LANCZOS)
    page = Image.new("RGB", (round(W_MM * MM), round(H_MM * MM)), "white")
    x = (page.width - w) // 2 if lay["left"] is None else round(lay["left"] * MM)
    y = (page.height - h) // 2 if lay["bottom"] is None else page.height - h - round(lay["bottom"] * MM)
    page.paste(art, (x, y))
    edges = [x / MM, (page.width - x - w) / MM, y / MM, (page.height - y - h) / MM]
    print("ふちからの距離(左・右・上・下 mm):", ", ".join(f"{e:.1f}" for e in edges))
    if min(edges) < SAFE:
        raise SystemExit(f"絵がふちに近すぎる({SAFE}mm未満)。幅を小さくする")
    out = ROOT / "postcard"
    out.mkdir(exist_ok=True)
    pdf = out / f"postcard_{name}_{kind}.pdf"
    page.save(pdf, resolution=DPI, quality=92)
    page.resize((page.width // 3, page.height // 3), Image.LANCZOS).save(out / f"postcard_{name}_{kind}.jpg", quality=88)
    print(f"done: {pdf.name}(絵の大きさ {w / MM:.0f}×{h / MM:.0f}mm、{DPI}dpi)")


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[3] not in LAYOUT:
        raise SystemExit(__doc__)
    main(*sys.argv[1:])
