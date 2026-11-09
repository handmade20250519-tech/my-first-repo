"""商品画像: あけおめ動画の見本。2000x2000。スマホ3台に、動画の3つの場面を並べて、動くことを見せる。
make_greeting_video.py が作った greeting/<名前>_akeome.mp4 から作る。
使い方: python3 make_video_listing.py chin   → listing_chin_video.jpg"""
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw

import make_listing_extra as ex

ROOT = Path(__file__).parent
TIMES = (0.3, 2.3, 4.3)  # 動画の何秒目を見せるか


def frame(video, t):
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", str(video), "-frames:v", "1",
                        f"{tmp}/f.png"], check=True)
        return Image.open(f"{tmp}/f.png").convert("RGB")


def phone(screen, w):
    """スマホのわく(黒いふち・角丸)に画面を入れる"""
    h = round(screen.height * w / screen.width)
    b = 22  # ふちの太さ
    ph = Image.new("RGBA", (w + 2 * b, h + 2 * b), (0, 0, 0, 0))
    d = ImageDraw.Draw(ph)
    d.rounded_rectangle((0, 0, ph.width - 1, ph.height - 1), radius=70, fill=(40, 38, 36, 255))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), radius=50, fill=255)
    ph.paste(screen.resize((w, h), Image.LANCZOS), (b, b), mask)
    return ph


def main(name):
    S = ex.S
    video = ROOT / "greeting" / f"{name}_akeome.mp4"
    c = Image.new("RGBA", (S, S), ex.BG + (255,))
    d = ImageDraw.Draw(c)
    d.text((S / 2, 150), "動く「あけおめ動画」付き", font=ex.f(96), fill=ex.INK, anchor="mm")
    d.text((S / 2, 265), "スマホに保存して、LINEなどでそのまま送れます", font=ex.f(50), fill=ex.INK, anchor="mm")
    phones = [phone(frame(video, t), 570) for t in TIMES]
    gap = 40
    x = (S - sum(p.width for p in phones) - gap * 2) // 2
    y = 380
    for i, p in enumerate(phones):
        ex.shadow_paste(c, p, x, y)
        if i < 2:  # 場面のあいだに、時間が進む矢印
            ax = x + p.width + gap / 2
            d.polygon([(ax - 14, y + p.height / 2 - 26), (ax + 16, y + p.height / 2), (ax - 14, y + p.height / 2 + 26)],
                      fill=ex.RED)
        x += p.width + gap
    d.text((S / 2, y + phones[0].height + 120), "縦長(スマホの画面サイズ)・5秒・くり返し再生・音なし",
           font=ex.f(54), fill=ex.INK, anchor="mm")
    d.text((S / 2, y + phones[0].height + 220), "※動きの見本は、作品ページの動画でご覧いただけます",
           font=ex.f(44), fill=ex.INK, anchor="mm")
    out = ROOT / f"listing_{name}_video.jpg"
    c.convert("RGB").save(out, quality=92)
    print("done:", out.name)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
