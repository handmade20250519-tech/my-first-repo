"""Canvaで動かした動画の、よくある困りごとを直す(文字を入れる前に使う)。
- 最初の数コマだけ背景が白く、そのあと背景がうすい色(灰色・ピンク)になる → 最初のコマを外し、背景を白にそろえる
- 途中で名前の文字が消える → 下じき画像と同じ場所に、名前を毎コマ入れ直す(--label)
使い方: python3 fix_canva_video.py <動画> <名前> [--skip 2] [--label "Papillon"] [--keep-bg]
       --keep-bg: 背景の色をそのままにする(白い雪が降る動画など、白にすると消えてしまうもの)
       → video_base/<名前>_canva_fixed.mp4(このあと make_greeting_video.py に渡す)"""
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

import make_postcard as mp
import make_video_base as vb

ROOT = Path(__file__).parent


def name_rows(name):
    """下じき画像で、名前の文字がある高さ(いちばん下のかたまり)"""
    a = np.asarray(Image.open(ROOT / "video_base" / f"{name}_video_base.png").convert("L"))
    rows = np.nonzero((a < 240).sum(axis=1) > 3)[0]
    segs = np.split(rows, np.nonzero(np.diff(rows) > 5)[0] + 1)
    return segs[-1][0], segs[-1][-1]


def main(video, name, skip=2, label=None, keep_bg=False):
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", video, f"{tmp}/f%03d.png"], check=True)
        fps = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=r_frame_rate",
                              "-of", "csv=p=0", video], capture_output=True, text=True).stdout.strip()
        frames = sorted(Path(tmp).glob("f*.png"))[skip:]
        # 背景の色: 動画のまん中あたりのコマの、左上のすみ
        mid = np.asarray(Image.open(frames[len(frames) // 2]).convert("RGB")).astype(float)
        # 4すみ(と上下のまん中)のうち、いちばん明るい所を背景とする(しっぽなどが入っているすみをさけるため)
        H, W = mid.shape[:2]
        spots = [(40, 40), (40, W - 120), (H - 120, 40), (H - 120, W - 120), (40, W // 2 - 40), (H // 2, 40)]
        bg = max((np.median(mid[y:y + 80, x:x + 80].reshape(-1, 3), axis=0) for y, x in spots), key=lambda c: c.mean())
        fill = tuple(int(v) for v in bg) if keep_bg else (255, 255, 255)
        if keep_bg:
            bg = np.array([255.0, 255.0, 255.0])
        print("背景の色:", fill, "(そのまま)" if keep_bg else "→ 白にそろえる")
        if label:
            r0, r1 = name_rows(name)
            font = ImageFont.truetype(str(mp.FONT), vb.LABEL_PX)
        out_dir = Path(tmp) / "out"
        out_dir.mkdir()
        for i, f in enumerate(frames):
            a = np.clip(np.asarray(Image.open(f).convert("RGB")).astype(float) * 255 / bg, 0, 255)
            im = Image.fromarray(a.astype(np.uint8))
            if label:
                d = ImageDraw.Draw(im)
                d.rectangle((0, r0 - 25, im.width, r1 + 25), fill=fill)
                d.text((im.width / 2, r0 - 2), label, font=font, fill=mp.INK, anchor="ma")
            im.save(out_dir / f"f{i:03d}.png")
        out = ROOT / "video_base" / f"{name}_canva_fixed.mp4"
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", fps, "-i", str(out_dir / "f%03d.png"),
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "12", str(out)], check=True)
    print("done:", out.name)


if __name__ == "__main__":
    args = sys.argv[1:]
    opts = {}
    if "--keep-bg" in args:
        args.remove("--keep-bg")
        opts["keep_bg"] = True
    for key in ("--skip", "--label"):
        if key in args:
            i = args.index(key)
            opts[key[2:]] = int(args[i + 1]) if key == "--skip" else args[i + 1]
            del args[i:i + 2]
    if len(args) != 2:
        raise SystemExit(__doc__)
    main(*args, **opts)
