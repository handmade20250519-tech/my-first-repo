"""スマホで送る、動く「あけおめ画像」を作る(GIF と MP4)。
もとの絵の背景を白にし、雪がふわふわ降るなかで、あいさつの文字がゆっくり出てくる。最後はまた最初につながる(くり返し再生)。

使い方: python3 make_greeting.py <もとの絵> <名前> [--label "Calico"]
作るもの: greeting/greeting_<名前>.gif、greeting/greeting_<名前>.mp4、確認用の greeting/greeting_<名前>_still.jpg
文字の書体は Klee One(fonts/KleeOne-SemiBold.ttf。OFLで商用可)。"""
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

import make_postcard as mp

ROOT = Path(__file__).parent
FONT = ROOT / "fonts" / "KleeOne-SemiBold.ttf"
S = 1080          # 画像の大きさ(正方形。スマホで見やすい)
FPS = 15
SEC = 4           # 1回の長さ(秒)
INK = (60, 55, 50)
RED = (190, 60, 50)
LINE1, LINE2 = "あけましておめでとう", "今年もよろしくね"


def art_image(src, label):
    im = mp.whiten(Image.open(src).convert("RGB"))
    if label:
        im = mp.strip_name(im)
    art = im.crop(mp.art_box(im))
    h = int(S * 0.56)
    w = int(art.width * h / art.height)
    if w > S * 0.8:
        w = int(S * 0.8)
        h = int(art.height * w / art.width)
    return art.resize((w, h), Image.LANCZOS)


def snowflakes(n, seed=1):
    rng = np.random.default_rng(seed)
    # x, はじめのy, 大きさ, 1回で落ちる回数(1か2。くり返しても切れ目が出ない), ゆれの幅, ゆれの向き
    return [(rng.uniform(0, S), rng.uniform(0, S), rng.uniform(3, 9), rng.integers(1, 3),
             rng.uniform(8, 25), rng.uniform(0, 2 * np.pi)) for _ in range(n)]


def ease(t):
    return 0.5 - 0.5 * np.cos(np.pi * min(max(t, 0), 1))


def frame(i, n, art, flakes, f1, f2):
    t = i / n
    c = Image.new("RGB", (S, S), "white")
    ax = (S - art.width) // 2
    ay = int(S * 0.08)
    c.paste(art, (ax, ay))
    d = ImageDraw.Draw(c, "RGBA")
    # 雪(うすい青灰色のまるい点。ふちをぼかす)
    snow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    sd = ImageDraw.Draw(snow)
    for x, y0, r, k, amp, ph in flakes:
        y = (y0 + t * k * (S + 40)) % (S + 40) - 20
        xx = x + amp * np.sin(2 * np.pi * t * k + ph)
        sd.ellipse((xx - r, y - r, xx + r, y + r), fill=(175, 190, 210, int(70 + r * 7)))
    c.paste(snow.filter(ImageFilter.GaussianBlur(1.5)), (0, 0), snow.filter(ImageFilter.GaussianBlur(1.5)))
    # 文字: 1行目は 0.10〜0.30 で、2行目は 0.30〜0.50 で出てきて、0.85〜1.0 で両方うすくなって消える(最初につながる)
    fade = 1 - ease((t - 0.85) / 0.15)
    a1 = ease((t - 0.10) / 0.20) * fade
    a2 = ease((t - 0.30) / 0.20) * fade
    ty = ay + art.height + int(S * 0.06)
    d.text((S / 2, ty), LINE1, font=f1, fill=INK + (int(255 * a1),), anchor="ma")
    d.text((S / 2, ty + int(S * 0.095)), LINE2, font=f2, fill=INK + (int(255 * a2),), anchor="ma")
    return c


def main(src, name, label=None):
    art = art_image(src, label)
    flakes = snowflakes(28)
    f1 = ImageFont.truetype(str(FONT), int(S * 0.07))
    f2 = ImageFont.truetype(str(FONT), int(S * 0.05))
    n = FPS * SEC
    frames = [frame(i, n, art, flakes, f1, f2) for i in range(n)]
    out = ROOT / "greeting"
    out.mkdir(exist_ok=True)
    frames[int(n * 0.6)].save(out / f"greeting_{name}_still.jpg", quality=90)
    # GIF(LINEなどでそのまま送れる)。大きすぎないように 540px にする
    small = [f.resize((540, 540), Image.LANCZOS) for f in frames]
    pal = small[int(n * 0.6)].quantize(colors=128, method=Image.MEDIANCUT)
    gif = [f.quantize(palette=pal, dither=Image.Dither.NONE) for f in small]
    gif[0].save(out / f"greeting_{name}.gif", save_all=True, append_images=gif[1:],
                duration=int(1000 / FPS), loop=0, optimize=True)
    # MP4(きれいで軽い。スマホの写真アプリに保存して送れる)
    with tempfile.TemporaryDirectory() as tmp:
        for i, f in enumerate(frames):
            f.save(f"{tmp}/f{i:03d}.png")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{tmp}/f%03d.png",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-movflags", "+faststart",
                        str(out / f"greeting_{name}.mp4")], check=True)
    for ext in ("gif", "mp4"):
        p = out / f"greeting_{name}.{ext}"
        print(f"done: {p.name}({p.stat().st_size // 1024}KB)")


if __name__ == "__main__":
    args = sys.argv[1:]
    label = None
    if "--label" in args:
        i = args.index("--label")
        label = args[i + 1]
        del args[i:i + 2]
    if len(args) != 2:
        raise SystemExit(__doc__)
    main(*args, label=label)
