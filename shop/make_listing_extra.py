"""商品画像の追加分: 作り方(4工程)と、大きさ・裏のしかけ。2000x2000。"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

ROOT = Path(__file__).parent
IMG = Path("/tmp/claude-0/-home-user-my-first-repo/02cb9a5c-e2c2-5947-887e-aad52a1618eb/images")
PH = ROOT.parent / "templates/pochi/photos"
FONT = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
BG, INK, RED = (244, 239, 230), (60, 52, 48), (190, 60, 50)
S = 2000


def f(n):
    return ImageFont.truetype(FONT, n)


def norm(im):
    a = np.asarray(im.convert("RGB")).astype(float)
    a = np.clip(a * (240.0 / np.percentile(a.mean(axis=2), 90)), 0, 255)
    return Image.fromarray(a.astype("uint8"))


def fit(im, w, h):
    return ImageOps.fit(im, (w, h), Image.LANCZOS)


def shadow_paste(c, im, x, y):
    sh = Image.new("RGBA", c.size, (0, 0, 0, 0))
    sh.paste((60, 45, 30, 70), (x + 10, y + 14, x + im.width + 10, y + im.height + 14))
    c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
    c.alpha_composite(im.convert("RGBA"), (x, y))


def howto():
    c = Image.new("RGBA", (S, S), BG + (255,))
    d = ImageDraw.Draw(c)
    d.text((S / 2, 120), "かんたん 4ステップ", font=f(96), fill=INK, anchor="mm")
    d.text((S / 2, 230), "ご自宅のプリンターかコンビニで印刷して作れます", font=f(50), fill=INK, anchor="mm")
    steps = [("1", "印刷して、折り目をつける", "step1.jpg"), ("2", "線に沿って切る", "step2.jpg"),
             ("3", "左右を折って貼る", "step3.jpg"), ("4", "下を折って貼り、シールで留める", "step5.jpg")]
    W, H, gx, gy, top = 860, 700, 80, 110, 330
    for i, (n, t, fn) in enumerate(steps):
        x = 100 + (i % 2) * (W + gx)
        y = top + (i // 2) * (H + gy)
        im = fit(norm(ImageOps.exif_transpose(Image.open(PH / fn))), W, H)
        shadow_paste(c, im, x, y)
        d.ellipse((x - 30, y - 30, x + 70, y + 70), fill=RED)
        d.text((x + 20, y + 20), n, font=f(64), fill=(255, 255, 255), anchor="mm")
        d.text((x + W / 2, y + H + 48), t, font=f(50), fill=INK, anchor="mm")
    c.convert("RGB").save(ROOT / "listing_shiba_4.jpg", quality=90)


def size_and_back():
    c = Image.new("RGBA", (S, S), BG + (255,))
    d = ImageDraw.Draw(c)
    d.text((S / 2, 120), "裏を返すと、リードの続きが", font=f(88), fill=INK, anchor="mm")
    fr = norm(ImageOps.exif_transpose(Image.open(IMG / "69.jpg")).crop((233, 229, 926, 1280)))
    bk = norm(ImageOps.exif_transpose(Image.open(IMG / "68.jpg")).crop((292, 290, 878, 1190)))
    h = 1250
    fr = fr.resize((int(fr.width * h / fr.height), h), Image.LANCZOS)
    bk = bk.resize((int(bk.width * h / bk.height), h), Image.LANCZOS)
    x1, y = 150, 300
    x2 = S - 150 - bk.width
    shadow_paste(c, fr, x1, y)
    shadow_paste(c, bk, x2, y)
    d.text((x1 + fr.width / 2, y + h + 60), "おもて", font=f(56), fill=INK, anchor="mm")
    d.text((x2 + bk.width / 2, y + h + 60), "うら", font=f(56), fill=INK, anchor="mm")
    # 大きさの矢印(おもての下と右)
    yy = y + h + 130
    d.line([(x1, yy), (x1 + fr.width, yy)], fill=INK, width=5)
    for xx in (x1, x1 + fr.width):
        d.line([(xx, yy - 22), (xx, yy + 22)], fill=INK, width=5)
    d.text((x1 + fr.width / 2, yy + 60), "64mm", font=f(52), fill=INK, anchor="mm")
    d.text((S / 2, S - 110), "仕上がり 64×95mm ・ 一万円札を三つ折りにして入ります", font=f(54), fill=INK, anchor="mm")
    # 裏のリードの先に丸印
    rx, ry = x2 + int(bk.width * 0.07), y + int(h * 0.47)
    d.ellipse((rx - 110, ry - 80, rx + 150, ry + 80), outline=RED, width=8)
    c.convert("RGB").save(ROOT / "listing_shiba_5.jpg", quality=90)


if __name__ == "__main__":
    howto()
    size_and_back()
    print("done")
