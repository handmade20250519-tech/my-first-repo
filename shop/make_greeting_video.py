"""Canvaで作った動く絵(縦長のMP4)に、あいさつの文字を入れる(MP4とGIF)。
上のあいた所に1行目、名前の下のあいた所に2行目を入れる。文字は最初から最後まで出したまま
(LINEなどで最初の1コマが見本として表示されるため、そこにも文字が入っているほうがよい)。

使い方: python3 make_greeting_video.py <動画> <名前> [言葉の種類…]   (言葉の種類を省くと matome だけ)
作るもの: greeting/<名前>_akeome.mp4(売るもの。ZIPにこの名前のまま入れる)と .gif、
         YouTubeにのせる見本 greeting/<名前>_akeome_mihon.mp4(「見本」の文字入り。そのまま使われないように)
         matome 以外の種類は <名前>_akeome_<種類>.mp4
文字の書体は Klee One(fonts/KleeOne-SemiBold.ttf。OFLで商用可)。"""
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
FONT = ROOT / "fonts" / "KleeOne-SemiBold.ttf"
INK = (60, 55, 50)
STYLES = {  # (1行目, 大きさ), (2行目, 大きさ)。大きさは画面の幅に対する割合
    "teinei": (("あけましておめでとうございます", 0.058), ("本年もよろしくお願いいたします", 0.048)),
    "casual": (("あけおめ！", 0.095), ("今年もよろしくね", 0.06)),
    # だれに送っても失礼にならない言葉(ユーザーが決めた。販売はこの1種類)
    "matome": (("あけましておめでとうございます", 0.058), ("今年もよろしくお願いします", 0.052)),
}
TOP_Y = 0.065     # 1行目の上(画面の高さに対する割合)。絵の上はしは 0.15 くらい
BOTTOM_Y = 0.885  # 2行目の上。名前の下はしは 0.85 くらい
GIF_W, GIF_FPS = 400, 10


def mihon(size):
    """見本の文字(うすい灰色。絵のまん中に大きく、ななめに)"""
    w, h = size
    m = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(m)
    d.text((w / 2, h / 2), "見本", font=ImageFont.truetype(str(FONT), int(w * 0.28)), fill=(120, 120, 120, 95), anchor="mm")
    return m.rotate(20, resample=Image.BICUBIC)


def overlay(size, style):
    w, h = size
    (t1, s1), (t2, s2) = STYLES[style]
    ov = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.text((w / 2, h * TOP_Y), t1, font=ImageFont.truetype(str(FONT), int(w * s1)), fill=INK, anchor="ma")
    d.text((w / 2, h * BOTTOM_Y), t2, font=ImageFont.truetype(str(FONT), int(w * s2)), fill=INK, anchor="ma")
    return ov


def main(video, name, styles=("matome",)):
    out = ROOT / "greeting"
    out.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", video, str(tmp / "f%03d.png")], check=True)
        fps = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=r_frame_rate",
                              "-of", "csv=p=0", video], capture_output=True, text=True).stdout.strip()
        frames = sorted(tmp.glob("f*.png"))
        size = Image.open(frames[0]).size
        mk = mihon(size)
        for style in styles:
            base = f"{name}_akeome" if style == "matome" else f"{name}_akeome_{style}"
            ov = overlay(size, style)
            sd = tmp / style
            md = tmp / (style + "_mihon")
            sd.mkdir()
            md.mkdir()
            for f in frames:
                im = Image.open(f).convert("RGBA")
                im.alpha_composite(ov)
                im.convert("RGB").save(sd / f.name)
                im.alpha_composite(mk)
                im.convert("RGB").save(md / f.name)
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", fps, "-i", str(md / "f%03d.png"),
                            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "23", "-movflags", "+faststart", "-an",
                            str(out / f"{base}_mihon.mp4")], check=True)
            mp4 = out / f"{base}.mp4"
            # 音は入れない(もとの動画は無音)
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", fps, "-i", str(sd / "f%03d.png"),
                            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-movflags", "+faststart", "-an",
                            str(mp4)], check=True)
            gif = out / f"{base}.gif"
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(mp4), "-vf",
                            f"fps={GIF_FPS},scale={GIF_W}:-1:flags=lanczos,hqdn3d=4:4:6:6,split[a][b];[a]palettegen=max_colors=64:stats_mode=diff[p];[b][p]paletteuse=dither=none:diff_mode=rectangle",
                            "-loop", "0", str(gif)], check=True)
            Image.open(sd / frames[len(frames) // 2].name).save(out / f"{base}_still.jpg", quality=88)
            for p in (mp4, gif):
                print(f"done: {p.name}({p.stat().st_size // 1024}KB)")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2], tuple(sys.argv[3:]) or ("matome",))
