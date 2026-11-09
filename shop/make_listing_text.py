"""ぽち袋・ポストカード・あけおめ動画のセットの説明文(minneの説明文欄。2000文字まで)を作る。
docs/minne-pochi-listing-<名前>.md の「## 説明文」より上(商品名〜説明文)を、この形に入れかえる。

使い方(Pythonから):
    import make_listing_text as lt
    lt.update_doc("cat-sphynx", key="sphynx", title_jp="スフィンクス", catch="毛布でぬくぬく",
                  intro="…1段落目(最後の「〜にしました。」の前まで)…", aruaru="毛布のなかのしあわせ顔",
                  video="あけおめ動画は、…動画です。", pochi="Sphynx.pdf", yoko=True, ai_motion=True, cat=True,
                  name_note="袋の英字「Sphynx」は、…", tags="スフィンクス / 猫 / ぽち袋 / ポストカード / 猫好き")
"""
import re
from pathlib import Path

DOCS = Path(__file__).parent.parent / "docs"
LINK = "(ここにリンク)"
LINK_LEN = len("https://youtube.com/shorts/HNbCMiZjp0E")


def text(key, intro, aruaru, video, pochi, yoko, ai_motion, cat, name_note=""):
    pc_full = "(ポストカード・横向き・絵を大きく入れたもの)" if yoko else "(ポストカード・絵を大きく入れたもの、ハガキの大きさ)"
    pc_letter = ("(ポストカード・横向き・手紙用。すみに小さく絵を入れ、文字を書くところを広くとったもの)" if yoko
                 else "(ポストカード・手紙用。すみに小さく絵を入れ、文字を書くところを広くとったもの)")
    suffix = "_yoko" if yoko else ""
    size = "148×100mm(はがきと同じ大きさの横向きです)" if yoko else "100×148mm(はがきと同じ大きさです)"
    motion = "その絵にAIで動きをつけたもの" if ai_motion else "その絵をそのまま使い、デジタルで動きをつけたもの"
    theme = "猫の柄・猫種ごとの「あるある」" if cat else "犬種ごとの「あるある」"
    note = f"\n\n{name_note}" if name_note else ""
    return f"""{intro}
{aruaru}を、ぽち袋とポストカード、あけおめ動画にしました。

お年玉やちょっとしたお礼を渡すとき、袋を見た相手が「うちの子もこれやる!」と笑ってくれたら。そんな一枚になればうれしいです。
ポストカードは、飾ったり、お手紙に使ったりできます。
{video}LINEやメールで新年のあいさつとして送れます。
動画の見本(YouTube):{LINK}

絵は、墨と淡い水彩で描いたような、落ち着いた雰囲気に仕上げました。

※画像は『かんたん4ステップ』以外、AIで作ったイメージ画像です。袋の絵柄は実際の商品と同じです。{note}

━━━━━━━━━━
■ 中身(ZIPファイル1つ)
━━━━━━━━━━
・{pochi}(ぽち袋・A4横・6ページ)
 1ページに同じ袋が2つ入っています。使いたいページだけを印刷してください。
 1:のしも文字もなし(手書き用) 2:のしのみ 3:おとしだま
 4:ありがとう 5:おめでとう 6:こころばかり
・postcard_{key}_full{suffix}.pdf{pc_full}
・postcard_{key}_letter{suffix}.pdf{pc_letter}
・{key}_akeome.mp4(動くあけおめ動画。縦長・約5秒・音なし)
 「あけましておめでとうございます/今年もよろしくお願いします」の文字入り
・pochi_howto.pdf(作り方とご利用について、A4・3ページ)

ぽち袋の仕上がりの大きさ:64×95mm(一万円札を三つ折りにして入ります)
ポストカードの大きさ:{size}

━━━━━━━━━━
■ 作り方
━━━━━━━━━━
ご自宅のプリンターかコンビニのプリントで、A4に「実寸(100%)」で印刷し、切って、折って、貼ります。
はがき用紙やマット紙など、少し厚めの紙がおすすめです。
マーメイド紙は、ざらっとした質感が絵柄の和の雰囲気にぴったりでおすすめです。
貼るときは、スティックのり(固形のり)か両面テープをお使いください。液体のりは、水分でインクがにじむことがあります。
ふたは、シールや両面テープで留めてください。
詳しくは説明書をご覧ください。

ポストカードは、はがき用紙に「実寸(100%)」で印刷するだけで使えます。プリンターの用紙の設定は「はがき」を選んでください。

あけおめ動画は、スマホに保存してから、LINEやメールで送ってください。パソコンでダウンロードした場合は、動画のファイルをスマホに送って保存してください。

━━━━━━━━━━
■ ご注意
━━━━━━━━━━
・ご自身で使う分は、何枚でも印刷できます。あけおめ動画は、ご自身の新年のあいさつとして何人に送っていただいても、個人のSNSに投稿していただいてもかまいません(お店や会社の宣伝には使えません)。データを販売すること、印刷したものを販売することはできません。
・のしはお祝いごとの印です。お見舞いやお悔やみには、1ページ目(のしも文字もなし)をお使いください。
・作り方の画像は、柴犬のぽち袋で撮影したものです。組み立て方は同じです。

━━━━━━━━━━
■ 絵について
━━━━━━━━━━
この作品は、私がテーマ({theme})、場面、構図、色を考え、画像生成AIを使って絵を仕上げたデジタルアートです。あけおめ動画は、{motion}です。手描きの原画ではありません。
ぽち袋の型、文字の配置、作り方の説明書は、私が作りました。
墨や水彩で描いたように見えますが、デジタルで作った絵です。実際の筆・墨・絵の具・和紙は使っていません。

━━━━━━━━━━
■ ほかの犬種・猫の柄
━━━━━━━━━━
犬種・猫の柄ごとに、その子らしい「あるある」を描いた作品をどんどん出品予定です。
ない犬種・猫の柄は、メッセージでリクエストをお寄せください。"""


def update_doc(doc, key, title_jp, catch, tags, pochi, yoko, ai_motion, cat, intro, aruaru, video, name_note="",
               log=""):
    body = text(key, intro, aruaru, video, pochi, yoko, ai_motion, cat, name_note)
    n = len(body) - len(LINK) + LINK_LEN
    if n > 1990:
        raise SystemExit(f"説明文が長すぎる({n}文字)")
    p = DOCS / f"minne-pochi-listing-{doc}.md"
    s = p.read_text()
    start, end = s.index("## 商品名"), s.index("## 確かめること")
    new = f"""## 商品名
{title_jp}のぽち袋・ポストカード・あけおめ動画 {catch}｜お年玉・お礼に｜印刷して作るダウンロード版 のし付き6種(AIを用いた作品)
- minneの商品名の文字数の上限に入るか、出品の画面で確かめる。入らないときは「｜お年玉・お礼に」を外す

## 価格(仮)
500円

## 発送
なし(ダウンロード販売。購入後すぐにダウンロードできる)

## タグ(5つ)
{tags}

## 説明文
```
{body}
```

"""
    s = s[:start] + new + s[end:]
    s = re.sub(r"^# 出品文\(STEP5\) (.*?)のぽち袋\+ポストカード データ版", r"# 出品文(STEP5) \1のぽち袋+ポストカード+あけおめ動画 データ版",
               s, flags=re.M)
    suffix = "_yoko" if yoko else ""
    s = re.sub(rf"uchinoko-aruaru_{key}_pochi\.zip\(中身: [^\n]*",
               f"uchinoko-aruaru_{key}_pochi.zip(中身: {pochi}、postcard_{key}_full{suffix}.pdf、postcard_{key}_letter{suffix}.pdf、"
               f"{key}_akeome.mp4、pochi_howto.pdf。どれも名前を変えずに入れる)", s)
    if log:
        s = s.rstrip("\n") + "\n" + log + "\n"
    p.write_text(s)
    print(f"done: {p.name}(説明文 約{n}文字、リンク込み)")
    return body
