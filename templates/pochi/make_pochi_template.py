"""ぽち袋の展開図(A4横に2枚)を作る。

出力:
  pochi_guide_A4.png  Canvaで下敷きにする案内つきの型(300dpi)
  pochi_lines_A4.png  印刷用の線だけ(背景透明、300dpi)
  pochi_guide_A4.pdf  試し刷り用の案内つきの型(実寸)
  pochi_print_A4.png  売るデータ用。組み立てたあと線が目立たない版(背景透明、300dpi)
                      ・切り線ははっきりした灰色。型の外側だけに引くので、線の上を切れば袋に線が残らない
                      ・折り線は袋の上に引かず、型の外側に短い目印だけ
                      ・のりしろの印は、組み立てると②の下に隠れる①の端だけ
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = Path(__file__).parent
FONT_PATH = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
DPI = 300
PX = DPI / 25.4  # 1mmあたりのピクセル数

PAGE_W, PAGE_H = 297, 210
FLAP = 35      # 左右の折り返し(うしろで6mm重なる)
FRONT_W, FRONT_H = 64, 95
TOP, BOTTOM = 20, 25
NET_W, NET_H = FRONT_W + 2 * FLAP, TOP + FRONT_H + BOTTOM
GAP_X = (PAGE_W - 2 * NET_W) / 3
OFF_Y = (PAGE_H - NET_H) / 2 + 6
SAFE = 4       # おもての安全域
LID_IN = 2     # ふた④の付け根を左右それぞれ細くする幅。袋の口に差し込みやすくする(厚い紙で押し込むとしわになったため)
LID_TIP = 6    # ふた④の先を左右それぞれ細くする幅


def outline(ox, oy):
    """切り線(外形)の頂点。ox, oyは展開図の左上(mm)。"""
    fx0, fx1 = ox + FLAP, ox + FLAP + FRONT_W
    fy0, fy1 = oy + TOP, oy + TOP + FRONT_H
    return [
        (fx0 + LID_TIP, oy), (fx1 - LID_TIP, oy),     # ふた(上)。口に差し込めるよう袋より細い
        (fx1 - LID_IN, fy0), (fx1, fy0),
        (fx1 + FLAP, fy0 + 3), (fx1 + FLAP, fy1 - 3),  # 右の折り返し
        (fx1, fy1),
        (fx1 - 3, oy + NET_H), (fx0 + 3, oy + NET_H),  # 底
        (fx0, fy1),
        (ox, fy1 - 3), (ox, fy0 + 3),                  # 左の折り返し
        (fx0, fy0), (fx0 + LID_IN, fy0),
    ]


def folds(ox, oy):
    fx0, fx1 = ox + FLAP, ox + FLAP + FRONT_W
    fy0, fy1 = oy + TOP, oy + TOP + FRONT_H
    return [((fx0, fy0), (fx0, fy1)), ((fx1, fy0), (fx1, fy1)),
            ((fx0 + LID_IN, fy0), (fx1 - LID_IN, fy0)), ((fx0, fy1), (fx1, fy1))]


def nets():
    return [(GAP_X, OFF_Y), (2 * GAP_X + NET_W, OFF_Y)]


# ---------- PNG ----------
def p(v):
    return round(v * PX)


def dashed(draw, a, b, color, width, dash=2.0, gap=1.5):
    (x0, y0), (x1, y1) = a, b
    length = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    n, t = int(length // (dash + gap)) + 1, 0.0
    for _ in range(n):
        s, e = t, min(t + dash, length)
        if s >= length:
            break
        draw.line([(p(x0 + (x1 - x0) * s / length), p(y0 + (y1 - y0) * s / length)),
                   (p(x0 + (x1 - x0) * e / length), p(y0 + (y1 - y0) * e / length))],
                  fill=color, width=width)
        t += dash + gap


def draw_png(guide):
    size = (p(PAGE_W), p(PAGE_H))
    img = Image.new("RGBA", size, (255, 255, 255, 255 if guide else 0))
    d = ImageDraw.Draw(img)
    f_s = ImageFont.truetype(FONT_PATH, p(2.6))
    f_m = ImageFont.truetype(FONT_PATH, p(3.4))
    line = (150, 150, 150, 255)
    for ox, oy in nets():
        fx0, fy0 = ox + FLAP, oy + TOP
        if guide:
            glue = (225, 225, 225, 255)
            # のりしろ: 左の折り返しの外側6mm、底のふた全体
            d.rectangle([p(ox + 0.4), p(fy0 + 3.4), p(ox + 6), p(fy0 + FRONT_H - 3.4)], fill=glue)
            d.polygon([(p(fx0 + 0.4), p(fy0 + FRONT_H + 0.4)), (p(fx0 + FRONT_W - 0.4), p(fy0 + FRONT_H + 0.4)),
                       (p(fx0 + FRONT_W - 3.2), p(oy + NET_H - 0.4)), (p(fx0 + 3.2), p(oy + NET_H - 0.4))], fill=glue)
            # おもての安全域と、絵・文字の目安
            blue = (90, 150, 220, 255)
            sx0, sy0 = fx0 + SAFE, fy0 + SAFE
            sx1, sy1 = fx0 + FRONT_W - SAFE, fy0 + FRONT_H - SAFE
            for a, b in [((sx0, sy0), (sx1, sy0)), ((sx1, sy0), (sx1, sy1)),
                         ((sx1, sy1), (sx0, sy1)), ((sx0, sy1), (sx0, sy0))]:
                dashed(d, a, b, blue, 3, 1.2, 1.2)
            split = fy0 + 30
            dashed(d, (sx0, split), (sx1, split), blue, 2, 1.0, 1.5)
            d.text((p(fx0 + FRONT_W / 2), p(fy0 + 15)), "文字の範囲", font=f_m, fill=blue, anchor="mm")
            d.text((p(fx0 + FRONT_W / 2), p(fy0 + 62)), "絵を置く範囲", font=f_m, fill=blue, anchor="mm")
            gray = (110, 110, 110, 255)
            d.text((p(ox + FLAP / 2 + 3), p(fy0 + FRONT_H / 2)), "うしろへ折る\n①", font=f_s, fill=gray, anchor="mm", align="center")
            d.text((p(fx0 + FRONT_W + FLAP / 2), p(fy0 + FRONT_H / 2)), "うしろへ折る\n②", font=f_s, fill=gray, anchor="mm", align="center")
            d.text((p(ox + 3.2), p(fy0 + 12)), "の\nり", font=f_s, fill=gray, anchor="mm", align="center")
            d.text((p(fx0 + FRONT_W / 2), p(fy0 + FRONT_H + 12)), "のりしろ ③うしろへ折って貼る", font=f_s, fill=gray, anchor="mm")
            d.text((p(fx0 + FRONT_W / 2), p(oy + 10)), "ふた ④", font=f_s, fill=gray, anchor="mm")
        d.line([(p(x), p(y)) for x, y in outline(ox, oy)] + [(p(outline(ox, oy)[0][0]), p(outline(ox, oy)[0][1]))],
               fill=line, width=3)
        for a, b in folds(ox, oy):
            dashed(d, a, b, line, 3)
    if guide:
        d.text((p(PAGE_W / 2), p(9)),
               "ぽち袋の型(A4横・2枚どり) 仕上がり 64×95mm ── 実線=切る  点線=折る  灰色=のりしろ  青=Canvaでの配置の目安(印刷しない)",
               font=f_s, fill=(60, 60, 60, 255), anchor="mm")
        d.text((p(PAGE_W / 2), p(PAGE_H - 7)),
               "一万円札を三つ折り(約53×76mm)にして入る大きさ。①②の順に折り、①ののりしろに②を貼る。③を折り上げて貼る。④は袋の口に差し込む。",
               font=f_s, fill=(60, 60, 60, 255), anchor="mm")
    return img


# ---------- PDF ----------
def draw_pdf(path):
    pdfmetrics.registerFont(TTFont("IPAG", FONT_PATH))
    c = canvas.Canvas(str(path), pagesize=landscape(A4))
    H = PAGE_H

    def xy(x, y):
        return x * mm, (H - y) * mm

    c.setFont("IPAG", 7)
    c.drawCentredString(*xy(PAGE_W / 2, 9), "ぽち袋の型(A4横・2枚どり) 仕上がり 64×95mm ── 実線=切る 点線=折る 灰色=のりしろ")
    c.drawCentredString(*xy(PAGE_W / 2, PAGE_H - 7), "①②の順にうしろへ折り、①ののりしろに②を貼る。③を折り上げて貼る。④は袋の口に差し込む。")
    for ox, oy in nets():
        fx0, fy0 = ox + FLAP, oy + TOP
        c.setFillGray(0.88)
        c.rect(*xy(ox + 0.4, fy0 + FRONT_H - 3.4), (5.6) * mm, (FRONT_H - 6.8) * mm, stroke=0, fill=1)
        pth = c.beginPath()
        pth.moveTo(*xy(fx0 + 0.4, fy0 + FRONT_H + 0.4))
        for pt in [(fx0 + FRONT_W - 0.4, fy0 + FRONT_H + 0.4), (fx0 + FRONT_W - 3.2, oy + NET_H - 0.4), (fx0 + 3.2, oy + NET_H - 0.4)]:
            pth.lineTo(*xy(*pt))
        pth.close()
        c.drawPath(pth, stroke=0, fill=1)
        c.setStrokeGray(0.55)
        c.setLineWidth(0.6)
        c.setDash()
        pts = outline(ox, oy)
        pth = c.beginPath()
        pth.moveTo(*xy(*pts[0]))
        for pt in pts[1:]:
            pth.lineTo(*xy(*pt))
        pth.close()
        c.drawPath(pth, stroke=1, fill=0)
        c.setDash(5, 4)
        for a, b in folds(ox, oy):
            c.line(*xy(*a), *xy(*b))
        c.setFillGray(0.35)
        c.setFont("IPAG", 6)
        c.drawCentredString(*xy(ox + FLAP / 2 + 3, fy0 + FRONT_H / 2), "① うしろへ折る")
        c.drawCentredString(*xy(fx0 + FRONT_W + FLAP / 2, fy0 + FRONT_H / 2), "② うしろへ折る")
        c.drawCentredString(*xy(fx0 + FRONT_W / 2, fy0 + FRONT_H + 12), "③ のりしろ")
        c.drawCentredString(*xy(fx0 + FRONT_W / 2, oy + 10), "④ ふた")
    c.showPage()
    c.save()


def draw_print_png():
    """組み立てたときに線が目立たない、売るデータ用の版。"""
    img = Image.new("RGBA", (p(PAGE_W), p(PAGE_H)), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    cut = (120, 120, 120, 255)   # 切り線: 印刷してはっきり見える灰色(薄すぎて切る場所が分からなかったため濃くした)
    mark = (120, 120, 120, 255)
    for ox, oy in nets():
        fx0, fx1 = ox + FLAP, ox + FLAP + FRONT_W
        fy0, fy1 = oy + TOP, oy + TOP + FRONT_H
        # のりしろ(①の外側の端)。②を貼ると下に隠れるので、印刷しても見えない
        d.rectangle([p(ox + 0.6), p(fy0 + 3.6), p(ox + 5.5), p(fy1 - 3.6)], fill=(235, 235, 235, 255))
        # 切り線: 型の外側だけに引く。線の上を切れば、袋には線が残らない
        pts = [(p(x), p(y)) for x, y in outline(ox, oy)]
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ImageDraw.Draw(layer).line(pts + [pts[0]], fill=cut, width=p(0.8), joint="curve")
        inside = Image.new("L", img.size, 0)
        ImageDraw.Draw(inside).polygon(pts, fill=255)
        layer.putalpha(Image.composite(Image.new("L", img.size, 0), layer.getchannel("A"), inside))
        img.alpha_composite(layer)
        # 折り線の目印: 型の外側に短い線だけ(袋の上には線を引かない)
        L = 3.0
        ticks = [
            ((fx0, oy - 1), (fx0, oy - 1 - L)), ((fx1, oy - 1), (fx1, oy - 1 - L)),          # 左右の折り目(上端の外)
            ((fx0, oy + NET_H + 1), (fx0, oy + NET_H + 1 + L)), ((fx1, oy + NET_H + 1), (fx1, oy + NET_H + 1 + L)),
            ((ox - 1, fy0), (ox - 1 - L, fy0)), ((ox + NET_W + 1, fy0), (ox + NET_W + 1 + L, fy0)),  # 上下の折り目(左右の外)
            ((ox - 1, fy1), (ox - 1 - L, fy1)), ((ox + NET_W + 1, fy1), (ox + NET_W + 1 + L, fy1)),
        ]
        for a, b in ticks:
            d.line([(p(a[0]), p(a[1])), (p(b[0]), p(b[1]))], fill=mark, width=p(0.3))
    return img


if __name__ == "__main__":
    draw_print_png().save(OUT / "pochi_print_A4.png", dpi=(DPI, DPI))
    draw_png(True).convert("RGB").save(OUT / "pochi_guide_A4.png", dpi=(DPI, DPI))
    draw_png(False).save(OUT / "pochi_lines_A4.png", dpi=(DPI, DPI))
    draw_pdf(OUT / "pochi_guide_A4.pdf")
    print("done")
