"""HANNO CATS カレンダー2027 のチラシ(A4縦・カラー片面)を作る。
使い方: python3.13 make_calendar_flyer.py
出力: hanno_cats_calendar_flyer_A4.pdf(印刷用)と、確認用の PNG
"""
from pathlib import Path

import qrcode
from PIL import Image
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

HERE = Path(__file__).parent
IMG = HERE / "img"
OUT = HERE / "hanno_cats_calendar_flyer_A4.pdf"
pdfmetrics.registerFont(TTFont("G", "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf"))  # 英数字が等幅でない版(見た目が自然)

CREAM = HexColor("#F6F0E4")
GREEN = HexColor("#2F4A35")
BROWN = HexColor("#5A3A22")
RED = HexColor("#B8322A")
INK = HexColor("#33302C")
LINE = HexColor("#C9BBA3")

INSTAGRAM = "https://www.instagram.com/r.fukadaya/"

W, H = A4
M = 12 * mm  # 印刷で切れないよう、まわりに12mmあける
c = canvas.Canvas(str(OUT), pagesize=A4)
c.setTitle("HANNO CATS CALENDAR 2027 チラシ")

# 背景
c.setFillColor(CREAM)
c.rect(0, 0, W, H, stroke=0, fill=1)


def text(x, y, s, size, color=INK, anchor="l"):
    c.setFont("G", size)
    c.setFillColor(color)
    {"l": c.drawString, "c": c.drawCentredString, "r": c.drawRightString}[anchor](x, y, s)


def photo(path, x, y, w, frame=2.2 * mm, crop=None):
    """写真を白いふち付きで置く。y は写真の下端。高さを返す。"""
    im = Image.open(path).convert("RGB")
    if crop:
        im = im.crop(crop)
    h = w * im.height / im.width
    c.setFillColor(white)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.4)
    c.rect(x - frame, y - frame, w + 2 * frame, h + 2 * frame, stroke=1, fill=1)
    c.drawImage(ImageReader(im), x, y, w, h)
    return h


# 上から順に高さを決める(A4の縦297mmに収める)
# 1) 上: キャッチコピー
y = H - M - 8 * mm
text(W / 2, y, "飯能の山を旅するネコたちの、卓上カレンダー", 15, GREEN, "c")

# 2) 表紙(大きく)
cw = 172 * mm
cover_h = cw * 792 / 1125
cover_y = y - 5 * mm - cover_h
photo(IMG / "cover.jpg", (W - cw) / 2, cover_y, cw, frame=0)

# 限定18部のスタンプ(表紙の右下に重ねる)
sx, sy, r = (W + cw) / 2 - 6 * mm, cover_y + 4 * mm, 14 * mm
c.setFillColor(RED)
c.circle(sx, sy, r, stroke=0, fill=1)
c.setStrokeColor(white)
c.setLineWidth(1)
c.circle(sx, sy, r - 1.6 * mm, stroke=1, fill=0)
text(sx, sy + 2.5 * mm, "限定", 11, white, "c")
text(sx, sy - 6.5 * mm, "18部", 19, white, "c")

# 3) 中: 12か月の絵 + 値段など
top = cover_y - 7 * mm
mw = 56 * mm
photo(IMG / "months.jpg", M + 4 * mm, top - mw, mw)  # 正方形
rx = M + 4 * mm + mw + 10 * mm
text(rx, top - 7 * mm, "HANNO CATS CALENDAR 2027", 13, BROWN)
text(rx, top - 15 * mm, "卓上カレンダー(B6サイズ)・1月〜12月", 11, INK)
text(rx, top - 21.5 * mm, "毎月ちがう飯能の景色を、ネコたちが旅します", 9.5, INK)
c.setFont("G", 38)
pw = c.stringWidth("1,200", "G", 38)
text(rx, top - 40 * mm, "1,200", 38, RED)
text(rx + pw + 1.5 * mm, top - 40 * mm, "円", 18, RED)
text(rx + pw + 1.5 * mm, top - 33.5 * mm, "(税込)", 9.5, RED)
text(rx, top - 50 * mm, "限定18部・なくなり次第、終了です", 10, INK)

# 4) 下: 販売場所(BOXの写真 + お店の情報 + QR)
by = M
band_top = top - mw - 7 * mm
band_h = band_top - by
c.setFillColor(GREEN)
c.roundRect(M, by, W - 2 * M, band_h, 4 * mm, stroke=0, fill=1)
text(M + 7 * mm, band_top - 8.5 * mm, "販売中のお店", 13, white)
# BOXの写真(カレンダーが置いてある棚)。下にキャプションの余白を残して、入る大きさにする
avail_h = band_h - 12 * mm - 11 * mm
bw = min(76 * mm, avail_h * 1125 / 844)
box_h = bw * 844 / 1125
px = M + 7 * mm
py = band_top - 12 * mm - box_h
photo(IMG / "box.jpg", px, py, bw, frame=1.3 * mm)
text(px + bw / 2, py - 6.5 * mm, "↑ この棚に置いています", 9, white, "c")
# お店の情報
ix = px + bw + 9 * mm
iy = band_top - 17 * mm
text(ix, iy, "飯能駅から徒歩5分", 11.5, white)
text(ix, iy - 9 * mm, "くらしの循環センター", 13.5, white)
text(ix, iy - 16.5 * mm, "フカダヤ内 sopo-studio", 13.5, white)
c.setStrokeColor(HexColor("#7E9783"))
c.setLineWidth(0.6)
c.line(ix, iy - 21 * mm, W - M - 7 * mm, iy - 21 * mm)
text(ix, iy - 27.5 * mm, "住所   飯能市仲町6-11", 10, white)
text(ix, iy - 34 * mm, "営業   11:00〜18:00", 10, white)
text(ix, iy - 40.5 * mm, "定休日   月曜日・火曜日", 10, white)
# Instagram の QR コード
q = qrcode.QRCode(border=2, box_size=10)
q.add_data(INSTAGRAM)
qimg = q.make_image(fill_color="black", back_color="white").convert("RGB")
qs = 21 * mm
# 住所などの行の右側に置く(下に置くと住所に重なるため)
qx, qy = W - M - 7 * mm - qs, iy - 44 * mm
c.drawImage(ImageReader(qimg), qx, qy, qs, qs)
text(qx - 3 * mm, qy + 12 * mm, "Instagram", 9.5, white, "r")
text(qx - 3 * mm, qy + 6.5 * mm, "@r.fukadaya", 9.5, white, "r")

c.showPage()
c.save()
print(OUT)
