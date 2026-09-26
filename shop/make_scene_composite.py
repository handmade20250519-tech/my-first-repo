"""Geminiで作った場面写真の袋の部分に、本物の袋の写真(表)を貼り直す。
AIが袋の絵を描き変えるので、商品の見た目を本物に戻すため。"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageFont

ROOT = Path(__file__).parent
IMG = Path("/tmp/claude-0/-home-user-my-first-repo/02cb9a5c-e2c2-5947-887e-aad52a1618eb/images")
FONT = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"


def coeffs(dst, src):
    """dst(出力の4点)→src(入力の4点)の射影変換の係数。"""
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
        B += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()


def front():
    im = ImageOps.exif_transpose(Image.open(IMG / "69.jpg")).convert("RGB").crop((233, 229, 926, 1280))
    a = np.asarray(im).astype(float)
    a = np.clip(a * (240.0 / np.percentile(a.mean(axis=2), 90)), 0, 255)
    return Image.fromarray(a.astype("uint8"))


def paste(scene, env, quad):
    W, H = scene.size
    w, h = env.size
    c = coeffs(quad, [(0, 0), (w, 0), (w, h), (0, h)])
    warped = env.transform((W, H), Image.PERSPECTIVE, c, Image.BICUBIC)
    # 場面の光に合わせる: 元の袋の明るさの分布をそのまま掛ける
    s = np.asarray(scene).astype(float)
    mask = Image.new("L", (W * 4, H * 4), 0)
    ImageDraw.Draw(mask).polygon([(x * 4, y * 4) for x, y in quad], fill=255)
    mask = mask.resize((W, H), Image.LANCZOS)
    m = np.asarray(mask) > 250
    lum = s.mean(axis=2)
    light = Image.fromarray(np.clip(lum, 0, 255).astype("uint8")).filter(ImageFilter.GaussianBlur(40))
    light = np.asarray(light).astype(float)
    light = light / np.median(light[m])
    wa = np.asarray(warped).astype(float) * np.clip(light, 0.75, 1.15)[..., None]
    warped = Image.fromarray(np.clip(wa, 0, 255).astype("uint8")).filter(ImageFilter.GaussianBlur(0.6))
    scene.paste(warped, (0, 0), mask)


def main():
    scene = Image.open(IMG / "70.jpg").convert("RGB")
    env = front()
    paste(scene, env, [(277, 527), (708, 467), (826, 898), (399, 961)])   # 左の袋(うしろ)
    paste(scene, env, [(874, 526), (1298, 602), (1173, 1071), (687, 963)])  # 右の袋(手前)
    scene = scene.resize((2000, int(2000 * scene.height / scene.width)), Image.LANCZOS)
    d = ImageDraw.Draw(scene)
    f = ImageFont.truetype(FONT, 40)
    d.text((scene.width - 30, scene.height - 30), "※袋以外はイメージです", font=f, fill=(255, 255, 255),
           anchor="rd", stroke_width=3, stroke_fill=(90, 70, 50))
    scene.save(ROOT / "listing_shiba_2.jpg", quality=90)


if __name__ == "__main__":
    main()
    print("done")
