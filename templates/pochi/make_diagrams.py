"""説明書に添える組み立て図(線画)。寸法は make_pochi_template.py の型と同じ。"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from make_pochi_template import FLAP_L, FLAP_R, FRONT_W, FRONT_H, TOP, BOTTOM, OVERLAP, FONT_PATH

OUT = Path(__file__).parent / "diagrams"
K = 9                      # 1mmあたりのピクセル
INK = (60, 52, 46)
PAPER = (255, 255, 255)
BACK = (246, 243, 238)     # 紙の裏(うしろ側)
GLUE = (205, 205, 205)
RED = (200, 70, 55)
TAPE = (190, 225, 215)


def font(mm_size):
    return ImageFont.truetype(FONT_PATH, int(mm_size * K))


def arrow(d, pts, color=RED, width=4):
    d.line(pts, fill=color, width=width, joint="curve")
    (x0, y0), (x1, y1) = pts[-2], pts[-1]
    ang = math.atan2(y1 - y0, x1 - x0)
    L = 3.2 * K
    for s in (-1, 1):
        a = ang + math.pi + s * 0.45
        d.line([(x1, y1), (x1 + L * math.cos(a), y1 + L * math.sin(a))], fill=color, width=width)


def curve(p0, p1, p2, n=30):
    return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
             (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]) for t in (i / n for i in range(n + 1))]


def step3():
    """うしろから見た図。左: ①を折ってのりしろにテープ(②はまだ開いたまま)。右: ②を重ねて貼る(合わせ目は真ん中)。"""
    pw, ph, gap = 112, 180, 6
    img = Image.new("RGB", ((pw * 2 + gap) * K, ph * K), (255, 255, 255))
    d = ImageDraw.Draw(img)
    for panel in (0, 1):
        ox = (panel * (pw + gap) + 40) * K
        oy = 22 * K
        X = lambda v: ox + v * K
        Y = lambda v: oy + v * K
        # ふた④(上)と底③(下)は開いたまま
        d.polygon([(X(2), Y(0)), (X(62), Y(0)), (X(64), Y(TOP)), (X(0), Y(TOP))], fill=BACK, outline=INK, width=3)
        d.polygon([(X(0), Y(TOP + FRONT_H)), (X(64), Y(TOP + FRONT_H)), (X(61), Y(TOP + FRONT_H + BOTTOM)), (X(3), Y(TOP + FRONT_H + BOTTOM))],
                  fill=BACK, outline=INK, width=3)
        d.text((X(32), Y(TOP / 2)), "④", font=font(4), fill=(150, 140, 130), anchor="mm")
        d.text((X(32), Y(TOP + FRONT_H + BOTTOM / 2)), "③", font=font(4), fill=(150, 140, 130), anchor="mm")
        # 袋の本体(うしろから見ている)
        d.rectangle([X(0), Y(TOP), X(FRONT_W), Y(TOP + FRONT_H)], fill=BACK, outline=INK, width=3)
        # ①: 右から折られて、左端がのりしろ
        l1 = FRONT_W - FLAP_L
        d.rectangle([X(l1), Y(TOP), X(FRONT_W), Y(TOP + FRONT_H)], fill=PAPER, outline=INK, width=4)
        d.rectangle([X(l1 + 0.6), Y(TOP + 4), X(l1 + OVERLAP - 1.5), Y(TOP + FRONT_H - 4)], fill=GLUE)
        if panel == 0:
            # ②はまだ左に開いたまま
            d.polygon([(X(0), Y(TOP)), (X(-FLAP_R), Y(TOP + 3)), (X(-FLAP_R), Y(TOP + FRONT_H - 3)), (X(0), Y(TOP + FRONT_H))],
                      fill=BACK, outline=INK, width=3)
            d.text((X(-FLAP_R / 2), Y(TOP + 38)), "②", font=font(7), fill=(150, 140, 130), anchor="mm")
            d.rectangle([X(l1 + 1.5), Y(TOP + 6), X(l1 + OVERLAP - 2.5), Y(TOP + FRONT_H - 6)], fill=TAPE, outline=(120, 170, 155), width=2)
            d.text((X(l1 + 30), Y(TOP + 38)), "①", font=font(7), fill=INK, anchor="mm")
            d.text((X(l1 + 27), Y(TOP + 66)), "のりしろに\n両面テープ", font=font(4), fill=RED, anchor="lm")
            arrow(d, [(X(l1 + 26), Y(TOP + 66)), (X(l1 + OVERLAP), Y(TOP + 66))], width=4)
            d.text((X(16), Y(-10)), "1. ①を折って、のりしろにテープ", font=font(5), fill=INK, anchor="mm")
        else:
            d.text((X(52), Y(TOP + 38)), "①", font=font(7), fill=INK, anchor="mm")
            d.rectangle([X(0), Y(TOP), X(FLAP_R), Y(TOP + FRONT_H)], fill=PAPER, outline=INK, width=4)
            d.text((X(FLAP_R / 2), Y(TOP + 38)), "②", font=font(7), fill=INK, anchor="mm")
            arrow(d, curve((X(-18), Y(TOP + 64)), (X(-8), Y(TOP + 44)), (X(12), Y(TOP + 58))), width=5)
            d.line([(X(32), Y(TOP + FRONT_H + 1)), (X(32), Y(TOP + FRONT_H + 6))], fill=RED, width=4)
            d.text((X(32), Y(TOP + FRONT_H + BOTTOM + 8)), "合わせ目は まん中", font=font(4.5), fill=RED, anchor="mm")
            d.text((X(32), Y(-10)), "2. ②を重ねて貼る", font=font(5), fill=INK, anchor="mm")
    img.save(OUT / "step3.png")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    step3()
    print("done")
