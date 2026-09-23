"""データ版に入れる「作り方とご利用について」(A4縦・2ページ)のPDFを作る。"""
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from make_pochi_template import FLAP, FRONT_W, FRONT_H, TOP, BOTTOM, NET_W, NET_H, FONT_PATH

OUT = Path(__file__).parent / "pochi_howto.pdf"
SHOP = "(ショップ名)"
W, H = A4
pdfmetrics.registerFont(TTFont("IPAG", FONT_PATH))

INK = (0.25, 0.22, 0.2)
LINE = (0.6, 0.6, 0.6)
ACCENT = (0.8, 0.25, 0.2)


def text(c, x, y, s, size=10, color=INK, center=False):
    c.setFillColorRGB(*color)
    c.setFont("IPAG", size)
    (c.drawCentredString if center else c.drawString)(x, y, s)


NO_HEAD = "、。)」』ー・%"  # 行の先頭に来てはいけない文字


def wrap(s, width, size, indent=""):
    """幅widthに収まるように折り返す(行頭禁則つき)。"""
    rows, row = [], ""
    for i, ch in enumerate(s):
        row += ch
        nxt = s[i + 1] if i + 1 < len(s) else ""
        if pdfmetrics.stringWidth(row + nxt, "IPAG", size) > width and nxt and nxt not in NO_HEAD:
            rows.append(row)
            row = indent
    rows.append(row)
    return rows


def lines(c, x, y, rows, size=9.5, lead=15, width=170 * mm):
    out = []
    for r in rows:
        indent = "   " if r.startswith("・") else ""
        out += wrap(r, width - (x - 20 * mm), size, indent)
    for i, r in enumerate(out):
        text(c, x, y - i * lead, r, size)
    return y - len(out) * lead


def net(c, x, y, s, fold=None, glue=None, shade_front=False):
    """展開図を縮尺sで描く。x, yは左下(pt)。"""
    def P(px, py):  # 型の座標(mm、左上原点)→PDF座標
        return x + px * s, y + (NET_H - py) * s
    fx0, fx1 = FLAP, FLAP + FRONT_W
    fy0, fy1 = TOP, TOP + FRONT_H
    pts = [(fx0 + 3, 0), (fx1 - 3, 0), (fx1, fy0), (NET_W, fy0 + 3), (NET_W, fy1 - 3), (fx1, fy1),
           (fx1 - 3, NET_H), (fx0 + 3, NET_H), (fx0, fy1), (0, fy1 - 3), (0, fy0 + 3), (fx0, fy0)]
    if glue:
        c.setFillColorRGB(0.88, 0.88, 0.88)
        for gx0, gy0, gx1, gy1 in glue:
            a, b = P(gx0, gy1), P(gx1, gy0)
            c.rect(a[0], a[1], b[0] - a[0], b[1] - a[1], stroke=0, fill=1)
    if shade_front:
        c.setFillColorRGB(0.97, 0.93, 0.88)
        a, b = P(fx0, fy1), P(fx1, fy0)
        c.rect(a[0], a[1], b[0] - a[0], b[1] - a[1], stroke=0, fill=1)
    c.setStrokeColorRGB(*LINE)
    c.setLineWidth(0.8)
    c.setDash()
    pth = c.beginPath()
    pth.moveTo(*P(*pts[0]))
    for q in pts[1:]:
        pth.lineTo(*P(*q))
    pth.close()
    c.drawPath(pth, stroke=1, fill=0)
    if fold:
        c.setStrokeColorRGB(*ACCENT)
        c.setDash(3, 2)
        for (ax, ay), (bx, by) in fold:
            c.line(*P(ax, ay), *P(bx, by))
        c.setDash()
    return P


def page1(c):
    text(c, W / 2, H - 25 * mm, "ぽち袋の作り方", 18, center=True)
    text(c, W / 2, H - 33 * mm, "仕上がり 64×95mm ・ 一万円札を三つ折りにして入る大きさです", 9.5, center=True)

    y = H - 48 * mm
    text(c, 20 * mm, y, "■ 印刷するとき", 11.5)
    y = lines(c, 24 * mm, y - 16, [
        "・用紙は A4、向きは「横」。",
        "・倍率は「実寸(100%)」または「拡大・縮小しない」を選んでください。「用紙に合わせる」にすると大きさが変わります。",
        "・紙は、普通紙より少し厚い紙(はがき用紙、マット紙など、厚さ0.15〜0.25mmほど)がおすすめです。",
        "・ふちなし印刷でなくても大丈夫です。型は用紙の端から離してあります。",
        "・PDFの中に、文字違いが6ページ入っています。使いたいページだけを印刷してください。",
        "     1: のしのみ   2: おとしだま   3: ありがとう",
        "     4: おめでとう   5: こころばかり   6: のしも文字もなし(手書き用)",
    ])

    y -= 10
    text(c, 20 * mm, y, "■ 組み立て方", 11.5)
    steps = [
        ("1", "薄い線に沿って切り取ります。",
         "型の外にある短い線(折り目の目印)は切り落としてかまいません。先に次の2を済ませてから切ると楽です。"),
        ("2", "折り目をつけます。",
         "袋には折り線を印刷していません。型の外にある向かい合う目印どうしを定規で結び、なぞって軽く筋をつけてから折ります。"),
        ("3", "左右をうしろへ折ります。",
         "①(左)を先に折り、灰色の細い帯(のりしろ)にのりを付けて、②(右)を重ねて貼ります。"),
        ("4", "下をうしろへ折り上げて貼ります。",
         "③(下)の裏側にのりを付けて、袋のうしろに貼ります。"),
        ("5", "お金を入れて、ふたを閉じます。",
         "④(上)を折り、シールなどで留めてください。"),
    ]
    for i, (n, head, body) in enumerate(steps):
        top = y - 14 - i * 64
        text(c, 20 * mm, top, n, 16, ACCENT)
        text(c, 28 * mm, top, head, 10.5)
        lines(c, 28 * mm, top - 14, [body], 9, 12.5, width=113 * mm)
        fx0, fx1 = FLAP, FLAP + FRONT_W
        fy0, fy1 = TOP, TOP + FRONT_H
        fold = None
        glue = None
        if n == "2":
            fold = [((fx0, fy0), (fx0, fy1)), ((fx1, fy0), (fx1, fy1)), ((fx0, fy0), (fx1, fy0)), ((fx0, fy1), (fx1, fy1))]
        if n == "3":
            fold = [((fx0, fy0), (fx0, fy1)), ((fx1, fy0), (fx1, fy1))]
            glue = [(0.5, fy0 + 3.5, 5.5, fy1 - 3.5)]
        if n == "4":
            fold = [((fx0, fy1), (fx1, fy1))]
        if n == "5":
            fold = [((fx0, fy0), (fx1, fy0))]
        mini = 0.42
        P = net(c, W - 20 * mm - NET_W * mini, top - NET_H * mini + 8, mini, fold, glue, shade_front=True)
        c.setFillColorRGB(*INK)
        c.setFont("IPAG", 6.5)
        c.drawCentredString(*P(FLAP / 2, TOP + FRONT_H / 2), "①")
        c.drawCentredString(*P(FLAP + FRONT_W + FLAP / 2, TOP + FRONT_H / 2), "②")
        c.drawCentredString(*P(FLAP + FRONT_W / 2, TOP + FRONT_H + BOTTOM / 2), "③")
        c.drawCentredString(*P(FLAP + FRONT_W / 2, TOP / 2 + 2), "④")
    y = y - 14 - len(steps) * 64
    lines(c, 20 * mm, y, ["※ 絵柄によっては、しっぽなどが袋のうしろへ回り込むデザインになっています。折り目はそのままで大丈夫です。"], 8.5, 12)
    text(c, W / 2, 15 * mm, SHOP, 9, (0.5, 0.5, 0.5), center=True)


def page2(c):
    text(c, W / 2, H - 25 * mm, "ご利用について", 18, center=True)
    y = H - 42 * mm
    blocks = [
        ("■ できること", [
            "・ご自身で印刷して、使ったり、人に渡したりすること。",
            "・完成したぽち袋の写真をSNSに載せること(ショップ名を添えていただけるとうれしいです)。",
        ]),
        ("■ できないこと", [
            "・データそのものを、ほかの人に渡したり、インターネットで公開したりすること。",
            "・データや、印刷したぽち袋を販売すること(フリマアプリ、ハンドメイドサイトなどを含みます)。",
            "・絵を切り抜いて、ほかの商品やロゴなどに使うこと。",
        ]),
        ("■ のしについて", [
            "・のしは、お祝いごとの印です。お年玉、お礼、お祝い、心付けなどにお使いください。",
            "・お見舞いやお悔やみには使いません。その場合は6ページ目(のしも文字もなし)をお使いください。",
        ]),
        ("■ 絵について", [
            "・この絵は、作者がコンセプトや構図を考え、画像生成AIを使って仕上げたデジタルアートです。",
            "・お使いの画面やプリンターによって、色の見え方が少し変わることがあります。",
        ]),
        ("■ お問い合わせ", [
            "・うまく印刷できない、組み立て方が分からないなどのときは、minneのメッセージからお気軽にどうぞ。",
            "・ほかの犬種・猫の柄のリクエストも受け付けています。",
        ]),
    ]
    for head, rows in blocks:
        text(c, 20 * mm, y, head, 11.5)
        y = lines(c, 24 * mm, y - 17, rows, 9.5, 15) - 12
    text(c, W / 2, 15 * mm, SHOP, 9, (0.5, 0.5, 0.5), center=True)


if __name__ == "__main__":
    c = canvas.Canvas(str(OUT), pagesize=A4)
    page1(c)
    c.showPage()
    page2(c)
    c.showPage()
    c.save()
    print("done")
