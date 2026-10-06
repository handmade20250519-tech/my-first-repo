"""組み立てた袋のうしろを撮った写真を、まっすぐにして明るく整える(暗さ・しわの影を消す)。
使い方: IMG_DIR=… python3 clean_back_photo.py 16.jpg bordercollie "85,88 908,88 973,1327 90,1329"
四隅は 左上 右上 右下 左下(写真の中の袋の角)。できた画像は check/back_<名前>_photo.png"""
import os
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter

HERE = Path(__file__).parent
D = Path(os.environ.get("IMG_DIR", "."))
src, tag, corners = sys.argv[1], sys.argv[2], sys.argv[3]
quad = [tuple(map(float, c.split(","))) for c in corners.split()]
R = 10  # 1mmあたりのピクセル
W, H = 64 * R, 95 * R

im = Image.open(D / src).convert("RGB")
# 袋の四隅 → 64×95mmの長方形
A, B = [], []
for (u, v), (x, y) in zip(quad, [(0, 0), (W, 0), (W, H), (0, H)]):
    A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
    B += [u, v]
flat = im.transform((W, H), Image.PERSPECTIVE, np.linalg.solve(np.array(A, float), np.array(B, float)), Image.BICUBIC)

# 紙の明るさ(線や絵を消してから大きくぼかす)= 部屋の暗さとしわの影
paper = flat.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(18))
a = np.asarray(flat).astype(float)
p = np.asarray(paper).astype(float)
out = a / np.maximum(p, 1) * 250  # 紙を白(250)にそろえる
# 線(折り返しのふち)は少し濃くして、はっきり見せる
gray = out.mean(2, keepdims=True)
out = np.where(gray < 235, out - (235 - gray) * 0.6, out)
out = np.clip(out, 0, 255)

# 写真のふちに残った線(袋のふちの影)と、小さなごみ・点を消す。
# ERASE: 消す四角(x0, y0, x1, y1、ピクセル)。ふたの線・合わせ目・しっぽは残す
ERASE = {"bordercollie": [(0, 0, 5, 870), (629, 690, W, 880), (634, 590, W, 690)]}
# うめる色 = まわりの紙の色(線や点を消してから、なめらかにした紙)
fill = np.asarray(Image.fromarray(out.astype(np.uint8)).filter(ImageFilter.MaxFilter(7))
                  .filter(ImageFilter.GaussianBlur(6))).astype(float)
for x0, y0, x1, y1 in ERASE.get(tag, []):
    out[y0:y1, x0:x1] = fill[y0:y1, x0:x1]
from scipy import ndimage
dark = out.mean(2) < 170  # はっきり暗い点だけ(紙の繊維の模様は残す)
lab, n = ndimage.label(ndimage.binary_dilation(dark, iterations=2))
size = ndimage.sum(dark, lab, range(1, n + 1))
ext = ndimage.find_objects(lab)
for i, (sz, sl) in enumerate(zip(size, ext)):
    h, w = sl[0].stop - sl[0].start, sl[1].stop - sl[1].start
    if max(h, w) < 25:  # 線より小さい点・ごみ
        m = ndimage.binary_dilation(lab[sl] == i + 1, iterations=1)
        out[sl][m] = fill[sl][m]
res = Image.fromarray(out.astype(np.uint8))
res.save(HERE / "check" / f"back_{tag}_photo.png")
print("done", f"check/back_{tag}_photo.png")
