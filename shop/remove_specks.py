"""Canvaの動画で、背景に飛ぶ小さな点(ごみのような点)を消す。fix_canva_video.py の前に使う。
絵のかたまりから少しはなれた、小さな濃い点だけを背景の色でぬりつぶす(絵の中の点や毛の線は消さない)。
使い方: python3 remove_specks.py <動画> <出力の動画> [--max 400] [--gap 25]
  --max: これより小さい(画素の数)かたまりを点とみなす  --gap: 絵からこれだけ(px)はなれた点だけ消す"""
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage


def clean(a, max_px=400, gap=25):
    g = a.min(axis=2)
    bg = np.median(a[g > np.percentile(g, 60)].reshape(-1, 3), axis=0)
    dark = g < bg.min() - 30
    lab, n = ndimage.label(ndimage.binary_dilation(dark, iterations=1))
    if n == 0:
        return a, 0
    sizes = ndimage.sum(dark, lab, index=np.arange(1, n + 1))
    big = np.isin(lab, np.nonzero(sizes >= max_px)[0] + 1)
    near = ndimage.binary_dilation(big, iterations=gap)
    small_ids = np.nonzero(sizes < max_px)[0] + 1
    specks = np.isin(lab, small_ids) & ~near
    specks = ndimage.binary_dilation(specks, iterations=3)
    out = a.copy()
    out[specks] = bg.astype(np.uint8)
    return out, int(specks.any())


def main(video, out, max_px=400, gap=25):
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", video, f"{tmp}/f%03d.png"], check=True)
        fps = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=r_frame_rate",
                              "-of", "csv=p=0", video], capture_output=True, text=True).stdout.strip()
        o = Path(tmp) / "o"
        o.mkdir()
        hit = 0
        for i, f in enumerate(sorted(Path(tmp).glob("f*.png"))):
            a, h = clean(np.asarray(Image.open(f).convert("RGB")), max_px, gap)
            hit += h
            Image.fromarray(a).save(o / f"f{i:03d}.png")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", fps, "-i", str(o / "f%03d.png"),
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "12", out], check=True)
    print(f"done: {out}(点を消したコマ {hit})")


if __name__ == "__main__":
    args = sys.argv[1:]
    opts = {}
    for key, name in (("--max", "max_px"), ("--gap", "gap")):
        if key in args:
            i = args.index(key)
            opts[name] = int(args[i + 1])
            del args[i:i + 2]
    if len(args) != 2:
        raise SystemExit(__doc__)
    main(*args, **opts)
