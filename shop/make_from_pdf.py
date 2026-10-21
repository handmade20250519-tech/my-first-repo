"""CanvaのPDF(A4横・6ページ)から、商品画像の1枚目(デザイン見本)と3枚目(6種類)を作る。
スクリーンショットの代わりに使う。袋の切り出しは、折り位置の目印(トンボ)で行う。

使い方: python3 make_from_pdf.py <PDF> <名前>               (例: python3 make_from_pdf.py Chihuahua.pdf chihuahua)
        python3 make_from_pdf.py <PDF> <名前> --overwrite   (すでにある画像を作り直すとき)

作るもの:
  listing_<名前>_1.jpg          デザイン見本(make_covers.py と同じ形)
  listing_<名前>_3.jpg          6種類(make_listing_variants.py と同じ形)
  check/front_<名前>_blank.png  文字なしの袋の表(場面写真に貼るとき使う)

ページの順番は問わない。文字(おとしだま など)と、のしの赤い色で見分ける。"""
import subprocess
import sys
import tempfile
import unicodedata
from collections import Counter
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
import make_covers
import make_listing_variants as mv

ROOT = Path(__file__).parent
DPI = 300
MM = DPI / 25.4
WORDS = ["おとしだま", "ありがとう", "おめでとう", "こころばかり"]
ORDER = ["のしのみ", "おとしだま", "ありがとう", "おめでとう", "こころばかり", "無地(手書き用)"]


def groups(idx):
    """となり合う番号をまとめて、それぞれの真ん中を返す"""
    if len(idx) == 0:
        return []
    return [int(g.mean()) for g in np.split(idx, np.nonzero(np.diff(idx) > 3)[0] + 1)]


def front(page):
    """左の袋の表を、トンボの位置で切り出す。返り値: (表の画像, 幅mm, 高さmm)"""
    a = np.asarray(page.convert("L")).astype(int)
    dark = a < 200
    H, W = a.shape
    # まん中の高さで、袋の外形の縦線(左の袋の左はし・右はし、右の袋の左はし)を探す
    runs = groups(np.nonzero(dark[H // 2])[0])
    xl, xr, xn = runs[0], runs[1], runs[2]
    # ふたの上のはし(袋のまん中あたりの、いちばん上の線)より上に、表の左右を示すトンボがある
    xc = (xl + xr) // 2
    y_top = min(np.nonzero(dark[:, x])[0].min() for x in range(xc - 150, xc + 150, 5) if dark[:, x].any())
    band = dark[int(y_top - 12 * MM):int(y_top - 0.5 * MM), xl:xr]
    tx = groups(np.nonzero(band.any(axis=0))[0])
    # 2つの袋のすき間に、表の上下を示すトンボがある
    gap = dark[:, xr + 5:xn - 5]
    ty = groups(np.nonzero(gap.any(axis=1))[0])
    if len(tx) != 2 or len(ty) != 2:
        raise SystemExit(f"トンボが見つからない(横{len(tx)}本・縦{len(ty)}本)。展開図の形が変わっていないか確かめる")
    x0, x1 = xl + tx[0], xl + tx[1]
    y0, y1 = ty
    p = round(1.2 * MM)  # 折り目の線を入れない(make_listing_variants.front と同じ余白)
    return page.crop((x0 + p, y0 + p, x1 - p, y1 - p)), (x1 - x0) / MM, (y1 - y0) / MM


def kind(text, im):
    flat = unicodedata.normalize("NFC", "".join(text.split()))  # 縦書きは1文字ずつ改行されて出てくる
    for w in WORDS:
        if w in flat:
            return w
    a = np.asarray(im).astype(int)
    red = ((a[..., 0] > 150) & (a[..., 1] < 90) & (a[..., 2] < 90)).sum()
    return "のしのみ" if red > 200 else "無地(手書き用)"


def main(pdf, name, overwrite=False):
    outs = [ROOT / f"listing_{name}_1.jpg", ROOT / f"listing_{name}_3.jpg", ROOT / f"check/front_{name}_blank.png"]
    if not overwrite and any(o.exists() for o in outs):
        raise SystemExit(f"すでにある画像は上書きしない: {[o.name for o in outs if o.exists()]}(作り直すときは --overwrite)")
    n = int(next(l.split()[1] for l in subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout.splitlines()
                 if l.startswith("Pages:")))
    if n != 6:
        raise SystemExit(f"ページ数が{n}。6ページのPDFを使う")
    work = Path(tempfile.mkdtemp())
    subprocess.run(["pdftoppm", "-r", str(DPI), "-png", pdf, str(work / "p")], check=True)
    fronts, names = {}, Counter()
    for i in range(1, 7):
        text = subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), pdf, "-"], capture_output=True, text=True).stdout
        names.update(w for w in text.split() if w.isascii() and w.isalpha())
        page = Image.open(next(work.glob(f"p-{i}.png"))).convert("RGB")
        im, w, h = front(page)
        k = kind(text, im)
        print(f"{i}ページ目: {k}  表の大きさ {w:.1f} x {h:.1f} mm")
        if abs(w - 64) > 0.5 or abs(h - 95) > 0.5:
            raise SystemExit("袋の表が 64x95mm ではない。Canvaの展開図の大きさを確かめる")
        if k in fronts:
            raise SystemExit(f"「{k}」のページが2つある")
        fronts[k] = im
    if set(fronts) != set(ORDER):
        raise SystemExit(f"足りないページ: {set(ORDER) - set(fronts)}")
    print("動物名(PDFの文字):", ", ".join(w for w, _ in names.most_common(2)))

    mv.front = lambda path: fronts[str(path)]
    mv.D = Path("")
    mv.main([(k, k) for k in ORDER], outs[1].name)
    make_covers.make(name, (fronts["のしのみ"], fronts["おとしだま"]))
    fronts["無地(手書き用)"].save(outs[2])
    print("done:", ", ".join(o.name for o in outs))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        raise SystemExit(__doc__)
    main(args[0], args[1], "--overwrite" in sys.argv)
