"""データ版に入れる「作り方とご利用について」(A4縦・3ページ)のPDFを作る。"""
import io
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
    ("1", "折り目をつけます(切る前に)。",
     "袋には折り線を印刷していません。写真のピンクの丸で囲んだ、型の外の短い線が折る位置の目印です。向かい合う目印どうしを定規で結び、爪楊枝や竹串の先でなぞって筋をつけます。紙が破れないよう、力を入れすぎないでください。"),
    ("2", "薄い線に沿って切り取ります。",
     "型の外にある目印は、一緒に切り落としてかまいません。切り取ったら、1でつけた筋に沿って折ります。"),
    ("3", "左右をうしろへ折ります。",
     "①(左)を先に折り、灰色の細い帯(のりしろ)にスティックのりか両面テープを付けて、②(右)を重ねて貼ります。"),
    ("4", "下をうしろへ折り上げて貼ります。",
     "③(下)の内側にスティックのりか両面テープを付けて(左の写真)、折り上げて袋のうしろに貼ります(右の写真)。"),
    ("5", "お金を入れて、ふたを閉じます。",
     "④(上)をうしろへ折り、シールや両面テープで留めてください。コピー用紙のような薄い紙なら、ふたを袋の口に差し込んで閉じることもできます。厚い紙は差し込みにくいので、シールで留めるのがおすすめです。"),
]

# 工程写真の枠(正方形)。photos/step1.jpg〜step5.jpg(または .png)があれば、縦横比を保って枠の中に収める。無い工程は文字だけにする
PHOTO_DIR = Path(__file__).parent / "photos"
PHOTO_W, PHOTO_H = 62 * mm, 62 * mm
CARD_H = PHOTO_H + 8 * mm


def find_photo(n):
    for ext in (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"):
        f = PHOTO_DIR / f"step{n}{ext}"
        if f.exists():
            return f
    return None


def photo_width(n):
    """高さは固定。横長の写真は枠を横に広げる(最大100mm)。縦長は正方形の枠に収める。"""
    im = ImageOps.exif_transpose(Image.open(find_photo(n)))
    return min(max(PHOTO_H * im.width / im.height, PHOTO_W), 100 * mm)


def photo(c, x, y, n):
    """x, yは枠の左下。写真を縦横比を保ったまま枠の中に収める(切り取らない)。"""
    w = photo_width(n)
    im = ImageOps.exif_transpose(Image.open(find_photo(n))).convert("RGB")
    bw, bh = int(900 * w / PHOTO_H), 900
    bg = Image.new("RGB", (bw, bh), (246, 244, 240))
    fit = ImageOps.contain(im, (bw, bh), Image.LANCZOS)
    bg.paste(fit, ((bw - fit.width) // 2, (bh - fit.height) // 2))
    buf = io.BytesIO()
    bg.save(buf, "JPEG", quality=85)  # JPEGのまま埋め込んで、PDFを軽くする
    buf.seek(0)
    c.drawImage(ImageReader(buf), x, y, w, PHOTO_H)
    c.setStrokeColorRGB(*LINE)
    c.setLineWidth(0.5)
    c.rect(x, y, w, PHOTO_H, stroke=1, fill=0)


def step_card(c, top, n, head, body):
    """topはカードの上端。写真があれば左に写真、右に番号と説明。無ければ説明だけ。"""
    if find_photo(n):
        photo(c, 20 * mm, top - PHOTO_H, n)
        tx = 20 * mm + photo_width(n) + 7 * mm
    else:
        tx = 20 * mm
    text(c, tx, top - 16, n, 16, ACCENT)
    text(c, tx + 8 * mm, top - 16, head, 10.5)
    lines(c, tx, top - 34, [body], 9, 13.5)
    return top - (CARD_H if find_photo(n) else 22 * mm)


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
    top = y - 10
    for step in STEPS[:2]:
        top = step_card(c, top, *step)


def page_steps(c):
    """組み立て方の続き(3〜5)。"""
    y = H - 25 * mm
    text(c, 20 * mm, y, "■ 組み立て方(つづき)", 11.5)
    top = y - 10
    for step in STEPS[2:]:
        top = step_card(c, top, *step)
    y = top - 6
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
