"""もとの絵から、ハガキ(縦100×148mm)のポストカードPDFを作る。
Canvaでダウンロードすると絵が小さく(粗く)なるので、こちらで作る。

使い方: python3 make_postcard.py <絵の画像> <名前> full        (縦。ハガキいっぱいに絵を入れる)
        python3 make_postcard.py <絵の画像> <名前> letter      (縦・手紙用。左下に小さく絵を入れる)
        python3 make_postcard.py <絵の画像> <名前> full_yoko   (横148×100mm。横長の犬(ダックスなど)用)
        python3 make_postcard.py <絵の画像> <名前> letter_yoko (横・手紙用)

作るもの: postcard/postcard_<名前>_<タイプ>.pdf と、確認用の postcard/postcard_<名前>_<タイプ>.jpg

紙の色(少しクリーム色)がついた絵は、背景が真っ白になるように色を直す。
絵の白い背景は切り落とし、絵の部分(白でないところ)の大きさで配置を決める。
大きさと位置は、ユーザーがCanvaで作ったラブラドールの2枚に合わせた。"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).parent
DPI = 350
MM = DPI / 25.4

# タイプごとの紙の大きさと配置(mm)。left・bottom が None なら紙の真ん中
# full: 絵の幅83mm。letter: 絵の幅41mmで、左から7mm・下から16mm(ユーザーのCanvaの配置)
LAYOUT = {
    "full": {"size": (100, 148), "width": 83, "left": None, "bottom": None},
    "letter": {"size": (100, 148), "width": 41, "left": 7, "bottom": 16},
    "full_yoko": {"size": (148, 100), "width": 128, "left": None, "bottom": None},
    "letter_yoko": {"size": (148, 100), "width": 70, "left": 8, "bottom": 10},
}
SAFE = 5  # 家のプリンターはふちまで印刷できないことが多いので、絵はふちから5mm以上離す


def whiten(im):
    """ふちの色(紙の色)を背景とみなし、それが真っ白になるように色ごとに明るくする"""
    a = np.asarray(im).astype(float)
    border = np.concatenate([a[:20].reshape(-1, 3), a[-20:].reshape(-1, 3), a[:, :20].reshape(-1, 3), a[:, -20:].reshape(-1, 3)])
    bg = np.median(border, axis=0)
    if bg.min() >= 254:  # もともと真っ白(ラブラドールなど)。何もしない
        return im
    a = np.clip(a * 255 / bg, 0, 255)
    # 紙の細かいむら(ざらざら)も残ると、ハガキの白との境目が四角く見えるので、ほぼ白のところを白にそろえる。
    # 236より暗いところ(絵・影)はそのまま、236〜250はなめらかに白へ近づける
    t = np.clip((a.min(axis=2, keepdims=True) - 236) / 14, 0, 1)
    return Image.fromarray((a * (1 - t) + 255 * t).astype(np.uint8))


def art_box(im):
    """白い背景をのぞいた、絵の部分の範囲(紙の細かいむらは数えない)"""
    a = np.asarray(im).min(axis=2) < 232
    # 紙の小さな点(ごみ)で範囲が広がらないように、9画素以上ある行・列だけを絵とみなす
    ys, xs = np.nonzero(a.sum(axis=1) > 8)[0], np.nonzero(a.sum(axis=0) > 8)[0]
    pad = 30  # うすい影などを、切り口でぷつんと切らないように少し広めに取る
    H, W = a.shape
    return max(xs.min() - pad, 0), max(ys.min() - pad, 0), min(xs.max() + 1 + pad, W), min(ys.max() + 1 + pad, H)


def main(src, name, kind):
    lay = LAYOUT[kind]
    im = whiten(Image.open(src).convert("RGB"))
    W_MM, H_MM = lay["size"]
    art = im.crop(art_box(im))
    w = round(lay["width"] * MM)
    h = round(art.height * w / art.width)
    if art.width < w * 0.9:
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
