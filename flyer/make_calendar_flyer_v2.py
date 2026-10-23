"""HANNO CATS カレンダー2027 のチラシ 第2版(A4縦・カラー片面)。
ユーザーがAIで作ってみたチラシの雰囲気(上に大きな題名、葉っぱと木の飾り、値段の帯、赤い丸の限定)に寄せ、
写真と絵は本物のまま、文字はここで直接入れる。
使い方: python3.13 make_calendar_flyer_v2.py
"""
import math
import random
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
OUT = HERE / "hanno_cats_calendar_flyer_A4_v2.pdf"
pdfmetrics.registerFont(TTFont("G", "/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf"))

PAPER = HexColor("#F5EEDD")
BROWN = HexColor("#4E3220")
GREEN = HexColor("#3E6B3F")
LEAF = HexColor("#5E8F4E")
LEAF2 = HexColor("#86AE6A")
TREE = HexColor("#2F5E3C")
RED = HexColor("#C8372D")
YELLOW = HexColor("#F7E3A1")
PINK = HexColor("#F6C9B8")
SAGE = HexColor("#E3ECCF")
INK = HexColor("#33302C")

INSTAGRAM = "https://www.instagram.com/r.fukadaya/"
W, H = A4
M = 10 * mm
c = canvas.Canvas(str(OUT), pagesize=A4)
c.setTitle("HANNO CATS カレンダー 2027 チラシ")
random.seed(3)


def text(x, y, s, size, color=INK, anchor="l", bold=0.0):
    """bold>0 で、文字のふちを同じ色でなぞって太く見せる(太字の和文フォントがないため)"""
    t = c.beginText()
    t.setFont("G", size)
    w = c.stringWidth(s, "G", size)
    x0 = {"l": x, "c": x - w / 2, "r": x - w}[anchor]
    t.setTextOrigin(x0, y)
    c.setFillColor(color)
    c.setStrokeColor(color)
    if bold:
        c.setLineWidth(bold)
        c.setLineJoin(1)
        t.setTextRenderMode(2)
    else:
        t.setTextRenderMode(0)  # 前の太字の設定が残らないように
    t.textOut(s)
    c.drawText(t)
    return w


def leaf(x, y, ang, s, col):
    c.saveState()
    c.translate(x, y)
    c.rotate(ang)
    p = c.beginPath()
    p.moveTo(0, 0)
    p.curveTo(s * 0.35, s * 0.28, s * 0.75, s * 0.25, s, 0)
    p.curveTo(s * 0.75, -s * 0.25, s * 0.35, -s * 0.28, 0, 0)
    c.setFillColor(col)
    c.drawPath(p, stroke=0, fill=1)
    c.restoreState()


def sprig(x, y, ang, length, n=5, size=5.5 * mm):
    """茎に葉っぱが左右交互につく小枝"""
    c.saveState()
    c.translate(x, y)
    c.rotate(ang)
    c.setStrokeColor(LEAF)
    c.setLineWidth(0.9)
    c.line(0, 0, length, 0)
    for i in range(n):
        t = (i + 0.6) / (n + 0.4) * length
        side = 1 if i % 2 == 0 else -1
        leaf(t, 0, side * 50, size * (0.8 + 0.2 * (i % 3) / 2), LEAF if i % 2 else LEAF2)
    leaf(length, 0, 0, size, LEAF)
    c.restoreState()


def tree(x, y, h, col=TREE):
    """三角を重ねた木。x, y は根元"""
    c.setFillColor(HexColor("#6B4A2E"))
    c.rect(x - h * 0.05, y, h * 0.1, h * 0.15, stroke=0, fill=1)
    for k, (yy, ww) in enumerate([(0.12, 0.62), (0.4, 0.5), (0.66, 0.36)]):
        p = c.beginPath()
        p.moveTo(x - h * ww / 2, y + h * yy)
        p.lineTo(x + h * ww / 2, y + h * yy)
        p.lineTo(x, y + h * min(1.0, yy + 0.42))
        p.close()
        c.setFillColor(col)
        c.drawPath(p, stroke=0, fill=1)


def mountain(x, y, w, col=TREE):
    """題名の間に入れる小さな山の印"""
    p = c.beginPath()
    p.moveTo(x - w / 2, y)
    p.lineTo(x - w * 0.12, y + w * 0.62)
    p.lineTo(x + w * 0.05, y + w * 0.38)
    p.lineTo(x + w * 0.2, y + w * 0.5)
    p.lineTo(x + w / 2, y)
    p.close()
    c.setFillColor(col)
    c.drawPath(p, stroke=0, fill=1)
    tree(x - w * 0.18, y, w * 0.42, HexColor("#4F7F4A"))
    tree(x + w * 0.16, y, w * 0.34, HexColor("#4F7F4A"))


def paw(x, y, s, col=BROWN):
    c.setFillColor(col)
    c.ellipse(x - s * 0.32, y - s * 0.28, x + s * 0.32, y + s * 0.18, stroke=0, fill=1)
    for dx, dy in [(-0.42, 0.32), (-0.15, 0.5), (0.15, 0.5), (0.42, 0.32)]:
        c.circle(x + dx * s, y + dy * s, s * 0.13, stroke=0, fill=1)


def framed(path, x, y, w, frame=2.4 * mm, angle=0.0):
    """白いふちと影のついた写真。x, y は写真の左下。高さを返す"""
    im = Image.open(path).convert("RGB")
    h = w * im.height / im.width
    c.saveState()
    c.translate(x + w / 2, y + h / 2)
    c.rotate(angle)
    c.setFillColor(HexColor("#00000022"), alpha=0.18)
    c.rect(-w / 2 - frame + 1.2 * mm, -h / 2 - frame - 1.4 * mm, w + 2 * frame, h + 2 * frame, stroke=0, fill=1)
    c.setFillColor(white, alpha=1)
    c.rect(-w / 2 - frame, -h / 2 - frame, w + 2 * frame, h + 2 * frame, stroke=0, fill=1)
    c.drawImage(ImageReader(im), -w / 2, -h / 2, w, h)
    c.restoreState()
    return h


def ribbon(x, y, w, h, col):
    """両はしが少し切れこんだ帯。x は真ん中、y は下端"""
    n = 2.5 * mm
    p = c.beginPath()
    p.moveTo(x - w / 2, y)
    p.lineTo(x + w / 2, y)
    p.lineTo(x + w / 2 - n, y + h / 2)
    p.lineTo(x + w / 2, y + h)
    p.lineTo(x - w / 2, y + h)
    p.lineTo(x - w / 2 + n, y + h / 2)
    p.close()
    c.setFillColor(col)
    c.drawPath(p, stroke=0, fill=1)


# ---------- 背景 ----------
c.setFillColor(PAPER)
c.rect(0, 0, W, H, stroke=0, fill=1)
# 紙のような小さな点
for _ in range(900):
    c.setFillColor(HexColor("#D9CDB4"), alpha=random.uniform(0.15, 0.45))
    c.circle(random.uniform(0, W), random.uniform(0, H), random.uniform(0.15, 0.45), stroke=0, fill=1)
c.setFillAlpha(1)

# ---------- 1) 題名 ----------
ty = H - M - 17 * mm
c.setFont("G", 40)
wl = c.stringWidth("HANNO", "G", 40)
wr = c.stringWidth("CATS", "G", 40)
gap = 18 * mm
x0 = W / 2 - (wl + gap + wr) / 2
text(x0, ty, "HANNO", 40, BROWN, bold=1.6)
mountain(x0 + wl + gap / 2, ty - 0.5 * mm, 15 * mm)
text(x0 + wl + gap, ty, "CATS", 40, BROWN, bold=1.6)
text(W / 2, ty - 15 * mm, "カレンダー 2027", 30, BROWN, "c", bold=1.2)
paw(W / 2 - 52 * mm, ty - 10 * mm, 5 * mm)
paw(W / 2 + 52 * mm, ty - 10 * mm, 5 * mm)

# 説明の帯
ry = ty - 30 * mm
ribbon(W / 2, ry, 150 * mm, 11 * mm, YELLOW)
text(W / 2, ry + 3.4 * mm, "飯能の山を旅するネコたちの卓上カレンダー", 14, BROWN, "c", bold=0.4)

# ---------- 2) 表紙 ----------
cw = 158 * mm
cover_h = cw * 792 / 1125
cover_y = ry - 6 * mm - cover_h
framed(IMG / "cover.jpg", (W - cw) / 2, cover_y, cw, frame=2.8 * mm, angle=-1.2)

# ---------- 3) 値段・限定 ----------
py = cover_y - 21 * mm
# 限定18部(赤い丸、左)
sx, sy, r = M + 23 * mm, py + 3 * mm, 17 * mm
c.setFillColor(RED)
c.circle(sx, sy, r, stroke=0, fill=1)
c.setStrokeColor(white)
c.setLineWidth(1.2)
c.circle(sx, sy, r - 1.8 * mm, stroke=1, fill=0)
text(sx, sy + 3.5 * mm, "限定", 14, white, "c", bold=0.5)
text(sx, sy - 8 * mm, "18部", 24, white, "c", bold=0.8)
# 値段の帯
bx = W / 2 + 14 * mm
c.setFillColor(PINK)
c.roundRect(bx - 50 * mm, py - 4 * mm, 100 * mm, 18 * mm, 9 * mm, stroke=0, fill=1)
c.setFont("G", 34)
pw = c.stringWidth("1,200", "G", 34)
c.setFont("G", 16)
ew = c.stringWidth("円(税込)", "G", 16)
px0 = bx - (pw + 1.5 * mm + ew) / 2
text(px0, py, "1,200", 34, BROWN, bold=1.0)
text(px0 + pw + 1.5 * mm, py, "円(税込)", 16, BROWN, bold=0.5)
# 強調の線
c.setStrokeColor(RED)
c.setLineWidth(1.2)
for ang in (150, 180, 210):
    a = math.radians(ang)
    c.line(bx - 53 * mm + 4 * mm * math.cos(a), py + 5 * mm + 4 * mm * math.sin(a),
           bx - 53 * mm + 8 * mm * math.cos(a), py + 5 * mm + 8 * mm * math.sin(a))
text(bx, py - 10 * mm, "卓上カレンダー  B6サイズ  /  1月〜12月", 10.5, INK, "c")

# ---------- 4) お店 ----------
top = py - 17 * mm
bottom = M + 4 * mm
# 左: お店の情報
iw = 92 * mm
c.setFillColor(SAGE)
c.roundRect(M + 3 * mm, bottom, iw, top - bottom, 5 * mm, stroke=0, fill=1)
ix = M + 9 * mm
iy = top - 10 * mm
# 歩く人の印のかわりに、足あと
paw(ix + 2.5 * mm, iy + 1.5 * mm, 4.2 * mm, GREEN)
w1 = text(ix + 7 * mm, iy, "飯能駅から徒歩", 13, BROWN, bold=0.4)
text(ix + 7 * mm + w1 + 0.5 * mm, iy, "5", 19, RED, bold=0.7)
c.setFont("G", 19)
text(ix + 7 * mm + w1 + 0.5 * mm + c.stringWidth("5", "G", 19) + 0.5 * mm, iy, "分", 13, BROWN, bold=0.4)
c.setDash(1, 2)
c.setStrokeColor(GREEN)
c.setLineWidth(0.8)
c.line(ix, iy - 4.5 * mm, M + 3 * mm + iw - 6 * mm, iy - 4.5 * mm)
c.setDash()
text(ix, iy - 12 * mm, "くらしの循環センター", 13, BROWN, bold=0.4)
text(ix, iy - 19 * mm, "フカダヤ内", 13, BROWN, bold=0.4)
text(ix, iy - 26 * mm, "sopo-studio にて販売中", 13, BROWN, bold=0.4)
text(ix, iy - 34.5 * mm, "住所   飯能市仲町6-11", 9.5, INK)
text(ix, iy - 40 * mm, "営業   11:00〜18:00", 9.5, INK)
text(ix, iy - 45.5 * mm, "定休日   月曜日・火曜日", 9.5, INK)
# QR(左の箱の右下)
q = qrcode.QRCode(border=1, box_size=10)
q.add_data(INSTAGRAM)
qimg = q.make_image(fill_color="black", back_color="white").convert("RGB")
qs = 17 * mm
qx, qy = M + 3 * mm + iw - 6 * mm - qs, bottom + 5 * mm
c.drawImage(ImageReader(qimg), qx, qy, qs, qs)
text(qx - 2 * mm, qy + 9 * mm, "Instagram", 8.5, INK, "r")
text(qx - 2 * mm, qy + 4.5 * mm, "@r.fukadaya", 8.5, INK, "r")

# 右: 販売しているBOXの写真
bw = W - M - 5 * mm - (M + 3 * mm + iw + 8 * mm)
bh_max = top - bottom - 10 * mm
bw = min(bw, bh_max * 1125 / 844)
bh = bw * 844 / 1125
bxl = W - M - 5 * mm - bw
byl = bottom + 9 * mm
framed(IMG / "box.jpg", bxl, byl, bw, frame=2 * mm, angle=1.5)
text(bxl + bw / 2, bottom + 1.5 * mm, "↑ この棚に置いています", 9, BROWN, "c")

# ---------- 飾り(葉っぱ・木) ----------
for (x, y, a, L) in [(4 * mm, H - 40 * mm, 70, 30 * mm), (6 * mm, H - 105 * mm, 60, 26 * mm),
                     (3 * mm, H - 160 * mm, 75, 28 * mm), (W - 4 * mm, H - 45 * mm, 110, 30 * mm),
                     (W - 5 * mm, H - 115 * mm, 115, 26 * mm), (W - 3 * mm, H - 165 * mm, 105, 26 * mm),
                     (M + 2 * mm, H - M - 2 * mm, -40, 22 * mm), (W - M - 2 * mm, H - M - 2 * mm, -140, 22 * mm)]:
    sprig(x, y, a, L)
tree(M + 6 * mm, ty - 14 * mm, 15 * mm)
tree(M + 14 * mm, ty - 14 * mm, 10 * mm, HexColor("#4F7F4A"))
tree(W - M - 7 * mm, ty - 14 * mm, 15 * mm)
tree(W - M - 15 * mm, ty - 14 * mm, 10 * mm, HexColor("#4F7F4A"))

c.showPage()
c.save()
print(OUT)
