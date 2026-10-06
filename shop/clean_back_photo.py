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
res = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
res.save(HERE / "check" / f"back_{tag}_photo.png")
print("done", f"check/back_{tag}_photo.png")
