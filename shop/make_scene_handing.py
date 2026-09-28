"""Geminiの「お年玉を渡す場面」の袋を、本物の袋の表(Canvaのデータ)に貼り替える。手の指は上に残す。"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import sys
sys.path.insert(0, str(Path(__file__).parent))
from make_scene_composite import coeffs
from make_listing_variants import front

ROOT = Path(__file__).parent
IMG = Path("/tmp/claude-0/-home-user-my-first-repo/02cb9a5c-e2c2-5947-887e-aad52a1618eb/images")
FONT = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
QUAD = [(573, 489), (890, 466), (975, 970), (668, 1007)]


def main():
    scene = Image.open(IMG / "83.jpg").convert("RGB")
    W, H = scene.size
    env = Image.open(IMG / "84.png").convert("RGB").crop((28, 28, 421, 616))
    # 紙の色を場面の紙に合わせる(真っ白→生成り)
    e = np.asarray(env).astype(float) * np.array([218/245, 207/245, 190/245])
    env = Image.fromarray(np.clip(e, 0, 255).astype("uint8"))
    w, h = env.size
    warped = env.transform((W, H), Image.PERSPECTIVE, coeffs(QUAD, [(0, 0), (w, 0), (w, h), (0, h)]), Image.BICUBIC)
    # 場面の光(明るさのむら)を移す
    s = np.asarray(scene).astype(float)
    quad = Image.new("L", (W * 4, H * 4), 0)
    ImageDraw.Draw(quad).polygon([(x * 4, y * 4) for x, y in QUAD], fill=255)
    quad = np.asarray(quad.resize((W, H), Image.LANCZOS)).astype(float) / 255
    lum = Image.fromarray(s.mean(axis=2).astype("uint8")).filter(ImageFilter.GaussianBlur(60))
    lum = np.asarray(lum).astype(float)
    light = np.clip(lum / np.median(lum[quad > 0.99]), 0.85, 1.06)
    wa = np.asarray(warped).astype(float) * light[..., None]
    # 手(肌色)は元の画像のまま残す
    r, g, b = s[..., 0], s[..., 1], s[..., 2]
    skin = (r > 120) & (r - b > 48) & (g - b < 48) & (r - g > 22) & (g > 0.6 * r)
    yy, xx = np.mgrid[0:H, 0:W]
    core = ((xx > 700) & (xx < 900) & (yy > 520) & (yy < 890)) | ((xx > 680) & (xx < 905) & (yy > 880) & (yy < 952))   # 袋の絵の部分(犬のオレンジを手と見間違えないように)
    skin &= ~core
    # 袋の外から続いている肌色だけを指とみなす(袋の中の影を指と間違えないように)
    from scipy import ndimage
    lab, _ = ndimage.label(skin)
    qm = np.asarray(Image.new("L", (W, H), 0)) > 0
    inside = np.zeros((H, W), bool)
    tmp = Image.new("L", (W, H), 0)
    ImageDraw.Draw(tmp).polygon(QUAD, fill=255)
    inside = np.asarray(tmp) > 0
    keep = np.unique(lab[skin & ~inside])
    skin = np.isin(lab, keep[keep > 0])
    skin = Image.fromarray((skin * 255).astype("uint8")).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(3))
    skin = np.asarray(skin.filter(ImageFilter.GaussianBlur(1.5))).astype(float) / 255
    alpha = quad * (1 - skin)
    out = s * (1 - alpha[..., None]) + wa * alpha[..., None]
    img = Image.fromarray(np.clip(out, 0, 255).astype("uint8"))
    img = img.crop((70, 40, W - 25, H - 10))   # 元の画面の黒いふちを切る
    side = min(img.size)
    img = img.crop(((img.width - side) // 2, (img.height - side) // 2, (img.width + side) // 2, (img.height + side) // 2))
    img = img.resize((2000, 2000), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    d.text((1970, 1970), "※袋以外はイメージです", font=ImageFont.truetype(FONT, 40), fill=(255, 255, 255),
           anchor="rd", stroke_width=3, stroke_fill=(90, 70, 50))
    img.save(ROOT / "listing_shiba_6.jpg", quality=90)


if __name__ == "__main__":
    main()
    print("done")
