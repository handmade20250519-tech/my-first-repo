"""データ版に入れる「作り方とご利用について」(A4縦・3ページ)のPDFを作る。"""
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image, ImageOps

from make_pochi_template import FONT_PATH

OUT = Path(__file__).parent / "pochi_howto.pdf"
SHOP = "うちの子あるある"
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


STEPS = [
    ("1", "薄い線に沿って切り取ります。",
     "型の外にある短い線(折り目の目印)は切り落としてかまいません。先に次の2を済ませてから切ると楽です。"),
    ("2", "折り目をつけます。",
     "袋には折り線を印刷していません。切り取った型の角(くびれている所)どうしを定規で結び、なぞって軽く筋をつけてから折ります。型の外にある短い目印も、同じ位置を示しています。厚い紙は、インクの出ないボールペンで強めに筋をつけると、きれいに折れます。"),
    ("3", "左右をうしろへ折ります。",
     "①(左)を先に折り、灰色の細い帯(のりしろ)にスティックのりか両面テープを付けて、②(右)を重ねて貼ります。"),
    ("4", "下をうしろへ折り上げて貼ります。",
     "③(下)の裏側にスティックのりか両面テープを付けて、袋のうしろに貼ります。"),
    ("5", "お金を入れて、ふたを閉じます。",
     "④(上)を折って、袋の口に差し込みます。しっかり閉じたいときは、差し込まずにうしろへ折り、シールや両面テープで留めてください。"),
]

# 工程写真の枠(横4:3)。photos/step1.jpg〜step5.jpg(または .png)があれば差し込む
PHOTO_DIR = Path(__file__).parent / "photos"
PHOTO_W, PHOTO_H = 76 * mm, 57 * mm
CARD_H = PHOTO_H + 8 * mm


def find_photo(n):
    for ext in (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"):
        f = PHOTO_DIR / f"step{n}{ext}"
        if f.exists():
            return f
    return None


def photo(c, x, y, n):
    """x, yは枠の左下。写真があれば枠いっぱいに(はみ出しは中央で切って)入れる。無ければ差し替え用の枠を描く。"""
    f = find_photo(n)
    if f:
        im = Image.open(f)
        im = ImageOps.exif_transpose(im).convert("RGB")
        im = ImageOps.fit(im, (1520, 1140), Image.LANCZOS)
        c.drawImage(ImageReader(im), x, y, PHOTO_W, PHOTO_H)
        c.setStrokeColorRGB(*LINE)
        c.setLineWidth(0.5)
        c.rect(x, y, PHOTO_W, PHOTO_H, stroke=1, fill=0)
        return
    c.setFillColorRGB(0.96, 0.95, 0.93)
    c.setStrokeColorRGB(*LINE)
    c.setLineWidth(0.8)
    c.setDash(4, 3)
    c.rect(x, y, PHOTO_W, PHOTO_H, stroke=1, fill=1)
    c.setDash()
    text(c, x + PHOTO_W / 2, y + PHOTO_H / 2 + 4, f"工程写真 {n}", 11, LINE, center=True)
    text(c, x + PHOTO_W / 2, y + PHOTO_H / 2 - 12, f"photos/step{n}.jpg(横4:3)", 8, LINE, center=True)


def step_card(c, top, n, head, body):
    """topはカードの上端。左に写真、右に番号と説明。"""
    photo(c, 20 * mm, top - PHOTO_H, n)
    tx = 20 * mm + PHOTO_W + 7 * mm
    text(c, tx, top - 16, n, 16, ACCENT)
    text(c, tx + 8 * mm, top - 16, head, 10.5)
    lines(c, tx, top - 34, [body], 9, 13.5)


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
        "・貼るときは、スティックのり(固形のり)か両面テープをお使いください。液体のりは水分でインクがにじむことがあります(とくにインクジェットプリンター)。",
        "・PDFの中に、文字違いが6ページ入っています。使いたいページだけを印刷してください。",
        "     1: のしのみ   2: おとしだま   3: ありがとう",
        "     4: おめでとう   5: こころばかり   6: のしも文字もなし(手書き用)",
    ])

    y -= 10
    text(c, 20 * mm, y, "■ 組み立て方", 11.5)
    text(c, W / 2, 15 * mm, SHOP, 9, (0.5, 0.5, 0.5), center=True)
    for i, step in enumerate(STEPS[:2]):
        step_card(c, y - 10 - i * CARD_H, *step)


def page_steps(c):
    """組み立て方の続き(3〜5)。"""
    y = H - 25 * mm
    text(c, 20 * mm, y, "■ 組み立て方(つづき)", 11.5)
    for i, step in enumerate(STEPS[2:]):
        step_card(c, y - 10 - i * CARD_H, *step)
    y = y - 10 - 3 * CARD_H - 6
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
    page_steps(c)
    c.showPage()
    page2(c)
    c.showPage()
    c.save()
    print("done")
