"""ポストカードの机の写真(絵を貼ったあとの完成画像)から、ハガキを白紙に戻した写真を作る。
もとの白紙の写真(172.jpg・174.jpg)が作業場所の引っこしで消えたので、完成画像から作り直した。
使い方: python3 make_desk_blank.py <完成画像> tate|yoko  → templates/scenes/172.jpg(縦) / 174.jpg(横)

- ハガキの中は、紙の部分(明るい画素)だけで光のむらを2次式で近似して、絵と文字を消す
- 右下の注記(※AIで作った…)は、箱のすぐ上と下の色をなめらかにつないで消す"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).parent
CARDS = {  # make_scene_blank.py と同じ四隅
    "tate": ("172.jpg", [[(255, 232), (604, 232), (608, 707), (257, 707)],
                         [(724, 708), (1084, 752), (977, 1098), (502, 1002)]], []),
    "yoko": ("174.jpg", [[(320, 295), (877, 294), (878, 660), (322, 663)],
                         [(440, 757), (1039, 812), (1002, 1069), (275, 983)]],
             [(381, 629), (819, 629), (819, 703), (381, 703)]),  # 手前のスタンドは消さない
}
NOTE = (340, 1176, 1240, 1238)  # 注記の箱(左, 上, 右, 下)


def fill_card(a, quad, keep):
    H, W, _ = a.shape
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).polygon(quad, fill=255)
    if keep:
        ImageDraw.Draw(m).polygon(keep, fill=0)
    inner = np.asarray(m.filter(ImageFilter.MinFilter(9))) > 0
    area = np.asarray(m.filter(ImageFilter.MaxFilter(3))) > 0
    ys, xs = np.nonzero(inner)
    px = a[ys, xs]
    paper = px.min(axis=1) > np.percentile(px.min(axis=1), 40)  # 絵や文字をのぞいた紙
    X = np.stack([np.ones_like(xs), xs, ys, xs * xs, xs * ys, ys * ys], 1).astype(float)[paper]
    ya, xa = np.nonzero(area)
    Xa = np.stack([np.ones_like(xa), xa, ya, xa * xa, xa * ya, ya * ya], 1).astype(float)
    out = a.copy()
    for c in range(3):
        coef, *_ = np.linalg.lstsq(X, px[paper, c], rcond=None)
        out[ya, xa, c] = np.clip(Xa @ coef, 0, 255)
    # ふちは少しぼかして、もとの写真となじませる
    al = (np.asarray(m.filter(ImageFilter.GaussianBlur(1.0))).astype(float) / 255)[..., None]
    return a * (1 - al) + out * al


def main(src, kind):
    fn, quads, keep = CARDS[kind]
    a = np.asarray(Image.open(src).convert("RGB")).astype(float)
    for q in quads:
        a = fill_card(a, q, keep)
    x0, y0, x1, y1 = NOTE
    top = a[y0 - 4:y0 - 1, x0:x1].mean(axis=0)  # 箱のすぐ上と、すぐ下の色を
    bot = a[y1 + 1:y1 + 4, x0:x1].mean(axis=0)  # 上から下へなめらかにつなぐ(写真のこのあたりはぼけているので目立たない)
    t = np.linspace(0, 1, y1 - y0)[:, None, None]
    a[y0:y1, x0:x1] = top * (1 - t) + bot * t
    a[y0 - 6:y1 + 6, x0 - 6:x1 + 6] = np.asarray(Image.fromarray(a[y0 - 6:y1 + 6, x0 - 6:x1 + 6].astype(np.uint8)).filter(ImageFilter.GaussianBlur(2))).astype(float)
    out = ROOT.parent / "templates" / "scenes" / fn
    Image.fromarray(a.astype(np.uint8)).save(out, quality=95)
    print("done:", out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
