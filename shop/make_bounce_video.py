"""絵をそのまま使って、ふわっと跳ねる5秒の動画を作る(Canvaで動かすと絵のタッチが変わってしまうときの代わり)。
make_video_base.py の縦長の下じき画像から、犬(上のかたまり)だけを上下にゆらし、影は犬が上がると小さく・うすくする。
最後の場面が最初につながるので、くり返し再生しても切れ目が出ない。文字は入れない(このあと make_greeting_video.py で入れる)。
使い方: python3 make_bounce_video.py <名前>   → video_base/<名前>_bounce.mp4"""
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops

ROOT = Path(__file__).parent
FPS, SEC = 30, 5
HOPS = 2      # 5秒で跳ねる回数
LIFT = 60     # いちばん高いときに上がる量(px)


def parts(base):
    """下じきを、犬・影・名前の3つの高さの範囲に分ける(白いすき間で分かれている)"""
    a = np.asarray(base.convert("L"))
    rows = np.nonzero((a < 240).sum(axis=1) > 3)[0]
    segs = np.split(rows, np.nonzero(np.diff(rows) > 5)[0] + 1)
    if len(segs) < 3:
        raise SystemExit("犬・影・名前が分かれていない。絵を確かめる")
    return (segs[0][0], segs[0][-1] + 1), (segs[1][0], segs[1][-1] + 1)


def main(name):
    base = Image.open(ROOT / "video_base" / f"{name}_video_base.png").convert("RGB")
    W, H = base.size
    (d0, d1), (s0, s1) = parts(base)
    dog = base.crop((0, d0, W, d1))
    shadow = base.crop((0, s0, W, s1))
    bg = base.copy()
    bg.paste((255, 255, 255), (0, d0, W, s1))
    # 白い背景の上に「乗算」で重ねる(白は消え、色はそのまま残る)
    def put(c, im, x, y):
        w = Image.new("RGB", c.size, (255, 255, 255))
        w.paste(im, (x, y))
        return ImageChops.multiply(c, w)
    n = FPS * SEC
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(n):
            h = 0.5 - 0.5 * np.cos(2 * np.pi * HOPS * i / n)  # 0(下)〜1(上)。最初と最後は0
            c = bg.copy()
            k = 1 - 0.18 * h
            sw = round(W * k)
            sh = np.asarray(shadow.resize((sw, s1 - s0), Image.LANCZOS)).astype(float)
            sh = 255 - (255 - sh) * (1 - 0.45 * h)  # 上がるほど影をうすく
            c = put(c, Image.fromarray(sh.astype(np.uint8)), (W - sw) // 2, s0)
            c = put(c, dog, 0, d0 - round(LIFT * h))
            c.save(f"{tmp}/f{i:03d}.png")
        out = ROOT / "video_base" / f"{name}_bounce.mp4"
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(FPS), "-i", f"{tmp}/f%03d.png",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "12", str(out)], check=True)
    print("done:", out.name)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
