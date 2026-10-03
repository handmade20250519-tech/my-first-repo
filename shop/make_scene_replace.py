"""使い方: python3 make_scene_replace.py americanshorthair_1
Geminiの場面写真の袋に、本物の袋の表(Canvaの無地ページ)を貼り直す。
Geminiが袋の絵を描き変えてしまうため。"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, str(Path(__file__).parent))
import make_listing_variants as mv

# 名前: (場面の画像, 袋の表に使う無地のページ, 袋の四隅[左上・右上・右下・左下])
SCENES = {
    "japanesemix_1": ("128.jpg", "122.jpg", [(273, 230), (586, 227), (601, 694), (272, 698)]),
    "americanshorthair_1": ("137.jpg", "131.jpg", [(318, 224), (647, 224), (652, 729), (308, 729)]),
}
name = sys.argv[1] if len(sys.argv) > 1 else "japanesemix_1"
scene_fn, FRONT, QUAD = SCENES[name]
SCENE = mv.D / scene_fn


def coeffs(dst, src):
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
        B += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(B, float))


scene = Image.open(SCENE).convert("RGB")
W, H = scene.size
front = mv.front(mv.D / FRONT)
fw, fh = front.size
c = coeffs(QUAD, [(0, 0), (fw, 0), (fw, fh), (0, fh)])
warped = front.transform((W, H), Image.PERSPECTIVE, c, Image.BICUBIC)
mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(mask).polygon(QUAD, fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(0.8))

# 光と影: 元の袋の白い部分の明るさを、なめらかな面で近似してかける
a = np.asarray(scene).astype(float)
m = np.asarray(mask) > 250
white = m & (a.min(axis=2) > 200) & ((a.max(axis=2) - a.min(axis=2)) < 30)
ys, xs = np.nonzero(white)
X = np.stack([np.ones_like(xs), xs, ys, xs * xs, xs * ys, ys * ys], 1).astype(float)
k = [np.linalg.lstsq(X, a[ys, xs, ch], rcond=None)[0] for ch in range(3)]
yy, xx = np.mgrid[0:H, 0:W]
G = np.stack([np.ones_like(xx), xx, yy, xx * xx, xx * yy, yy * yy], -1).astype(float)
light = np.stack([G @ k[ch] for ch in range(3)], -1) / 255.0
wf = np.asarray(warped).astype(float) / 255.0
wbg = np.asarray(front).astype(float).max() / 255.0
shaded = np.clip(wf / wbg * light, 0, 1) * 255
# 紙の質感(細かなざらつき)
rng = np.random.default_rng(1)
grain = Image.fromarray((rng.normal(128, 10, (H, W))).clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.7))
shaded = np.clip(shaded + (np.asarray(grain).astype(float)[..., None] - 128) * 0.35, 0, 255)
al = (np.asarray(mask).astype(float) / 255.0)[..., None]
out = a * (1 - al) + shaded * al
Image.fromarray(out.astype(np.uint8)).save(Path(__file__).parent / f"scene_{name}.jpg", quality=92)
print("done")
