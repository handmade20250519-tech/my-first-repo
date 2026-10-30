"""もとの絵から、ハガキ(縦100×148mm)のポストカードPDFを作る。
Canvaでダウンロードすると絵が小さく(粗く)なるので、こちらで作る。

使い方: python3 make_postcard.py <絵の画像> <名前> full        (縦。ハガキいっぱいに絵を入れる)
        python3 make_postcard.py <絵の画像> <名前> letter      (縦・手紙用。左下に小さく絵を入れる)
        python3 make_postcard.py <絵の画像> <名前> full_yoko   (横148×100mm。横長の犬(ダックスなど)用)
        python3 make_postcard.py <絵の画像> <名前> letter_yoko (横・手紙用)
        最後に --label "Shiba Inu" を付けると、AIが絵に描いた名前を消し、絵いっぱい(full)には
        この名前を Klee One で入れ直す(手紙用は名前なし)。書体はユーザーが決めた(2026-10-30)

作るもの: postcard/postcard_<名前>_<タイプ>.pdf と、確認用の postcard/postcard_<名前>_<タイプ>.jpg

紙の色(少しクリーム色)がついた絵は、背景が真っ白になるように色を直す。
絵の白い背景は切り落とし、絵の部分(白でないところ)の大きさで配置を決める。
大きさと位置は、ユーザーがCanvaで作ったラブラドールの2枚に合わせた。"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

ROOT = Path(__file__).parent
DPI = 350
MM = DPI / 25.4

# タイプごとの紙の大きさと配置(mm)。left・bottom が None なら紙の真ん中
# full: 絵の幅83mm。letter: 絵の幅41mmで、左から7mm・下から16mm(ユーザーのCanvaの配置)
LAYOUT = {
    "full": {"size": (100, 148), "width": 83, "left": None, "bottom": None},
    "letter": {"size": (100, 148), "width": 41, "left": 7, "bottom": 16},
    "full_yoko": {"size": (148, 100), "width": 128, "left": None, "bottom": None, "max_block": 74},
    "letter_yoko": {"size": (148, 100), "width": 70, "left": 8, "bottom": 10, "max_block": 40},
}
FONT = ROOT / "fonts" / "KleeOne-SemiBold-latin.woff"  # OFL。商品に使ってよい
LABEL_MM = 5.5  # 名前の文字の大きさ(フォントの大きさ)
LABEL_GAP = 6  # 絵と名前のあいだ(mm)
INK = (60, 55, 50)  # 少しあたたかみのある墨色
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
    a = a * (1 - t) + 255 * t
    # 和紙の繊維(細い筋)や小さな点は、まだ灰色に残る。絵・影・文字のような大きなかたまりだけを残して、ほかは白にする
    dark = a.min(axis=2) < 240
    lab, n = ndimage.label(ndimage.binary_dilation(dark, iterations=4))  # 文字は1語が1つのかたまりになる
    size = ndimage.sum(dark, lab, index=np.arange(1, n + 1))  # かたまりの中の、もとの濃い画素の数
    keep = np.isin(lab, np.nonzero(size > 600)[0] + 1)
    keep = ndimage.binary_dilation(keep, iterations=8)
    a[~keep] = 255
    return Image.fromarray(a.astype(np.uint8))


def art_box(im):
    """白い背景をのぞいた、絵の部分の範囲(紙の細かいむらは数えない)"""
    a = np.asarray(im).min(axis=2) < 232
    # 紙の小さな点(ごみ)で範囲が広がらないように、9画素以上ある行・列だけを絵とみなす
    ys, xs = np.nonzero(a.sum(axis=1) > 8)[0], np.nonzero(a.sum(axis=0) > 8)[0]
    pad = 30  # うすい影などを、切り口でぷつんと切らないように少し広めに取る
    H, W = a.shape
    return max(xs.min() - pad, 0), max(ys.min() - pad, 0), min(xs.max() + 1 + pad, W), min(ys.max() + 1 + pad, H)


def strip_name(im):
    """AIが絵の下に描いた名前を消す。名前は、絵の下にすき間をあけた、低く短い行のかたまりになっている"""
    a = np.asarray(im).min(axis=2) < 232
    H, W = a.shape
    idx = np.nonzero(a.sum(axis=1) > 8)[0]
    segs = np.split(idx, np.nonzero(np.diff(idx) > H * 0.02)[0] + 1)
    last = segs[-1]
    cols = np.nonzero(a[last[0]:last[-1] + 1].any(axis=0))[0]
    if len(segs) < 2 or len(last) > H * 0.07 or cols[-1] - cols[0] > W * 0.6:
        raise SystemExit("絵の下に名前らしい文字が見つからない。絵を確かめる")
    out = np.asarray(im).copy()
    out[max(last[0] - 10, 0):last[-1] + 11] = 255
    print(f"絵の名前を消した(上から{last[0]}〜{last[-1]}px)")
    return Image.fromarray(out)


def main(src, name, kind, label=None):
    lay = LAYOUT[kind]
    im = whiten(Image.open(src).convert("RGB"))
    if label:
        im = strip_name(im)
    W_MM, H_MM = lay["size"]
    art = im.crop(art_box(im))
    w = round(lay["width"] * MM)
    h = round(art.height * w / art.width)
    show_label = label and kind.startswith("full")
    font = ImageFont.truetype(str(FONT), round(LABEL_MM * MM))
    lh = font.getbbox("Ag")[3] if show_label else 0
    extra = round(LABEL_GAP * MM) + lh if show_label else 0
    if "max_block" in lay and h + extra > lay["max_block"] * MM:  # 横長でない絵は、高さに合わせて小さくする
        h = round(lay["max_block"] * MM) - extra
        w = round(art.width * h / art.height)
    if art.width < w * 0.9:
        print(f"注意: もとの絵が小さい(絵の幅 {art.width}px。{DPI}dpiでは {w}px ほしい)。少しぼやけるかもしれない")
    art = art.resize((w, h), Image.LANCZOS)
    page = Image.new("RGB", (round(W_MM * MM), round(H_MM * MM)), "white")
    d = ImageDraw.Draw(page)
    block = h + extra  # 絵と名前を合わせた高さ
    x = (page.width - w) // 2 if lay["left"] is None else round(lay["left"] * MM)
    y = (page.height - block) // 2 if lay["bottom"] is None else page.height - block - round(lay["bottom"] * MM)
    page.paste(art, (x, y))
    if show_label:
        d.text((page.width / 2, y + h + round(LABEL_GAP * MM)), label, font=font, fill=INK, anchor="ma")
    edges = [x / MM, (page.width - x - w) / MM, y / MM, (page.height - y - block) / MM]
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
    args = sys.argv[1:]
    label = None
    if "--label" in args:
        i = args.index("--label")
        label = args[i + 1]
        del args[i:i + 2]
    if len(args) != 3 or args[2] not in LAYOUT:
        raise SystemExit(__doc__)
    main(*args, label=label)
