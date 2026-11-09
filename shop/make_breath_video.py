"""寝ている絵用: 絵をそのまま使って、寝息でおなかがゆっくりふくらむ5秒の動画を作る。
make_video_base.py の縦長の下じき画像から、絵(名前より上のかたまり)を、下のはしを支点にして縦に少しだけのび縮みさせる。
最後の場面が最初につながるので、くり返し再生しても切れ目が出ない。文字は入れない(このあと make_greeting_video.py で入れる)。
使い方: python3 make_breath_video.py <名前>   → video_base/<名前>_breath.mp4"""
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops

ROOT = Path(__file__).parent
FPS, SEC = 30, 5
BREATHS = 2    # 5秒で息をする回数
GROW = 0.035   # いちばんふくらんだときの、縦ののび(3.5%)
WIDEN = 0.008  # 横にも少しだけ広がる


def main(name):
    base = Image.open(ROOT / "video_base" / f"{name}_video_base.png").convert("RGB")
    W, H = base.size
    a = np.asarray(base.convert("L"))
    rows = np.nonzero((a < 240).sum(axis=1) > 3)[0]
    segs = np.split(rows, np.nonzero(np.diff(rows) > 5)[0] + 1)
    if len(segs) < 2:
        raise SystemExit("絵と名前が分かれていない。絵を確かめる")
    t0, t1 = segs[0][0] - 20, segs[-2][-1] + 1  # 名前(いちばん下)より上が絵
    art = base.crop((0, t0, W, t1))
    bg = base.copy()
    bg.paste((255, 255, 255), (0, t0, W, t1))
    n = FPS * SEC
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(n):
            h = 0.5 - 0.5 * np.cos(2 * np.pi * BREATHS * i / n)  # 0〜1。最初と最後は0
            aw, ah = round(W * (1 + WIDEN * h)), round(art.height * (1 + GROW * h))
            im = art.resize((aw, ah), Image.LANCZOS)
            w = Image.new("RGB", (W, H), (255, 255, 255))
            w.paste(im, ((W - aw) // 2, t1 - ah))  # 下のはし(床)はそのまま
            ImageChops.multiply(bg, w).save(f"{tmp}/f{i:03d}.png")
        out = ROOT / "video_base" / f"{name}_breath.mp4"
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(FPS), "-i", f"{tmp}/f%03d.png",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "12", str(out)], check=True)
    print("done:", out.name)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
