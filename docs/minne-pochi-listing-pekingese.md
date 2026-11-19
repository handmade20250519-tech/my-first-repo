# 出品文(STEP5) ペキニーズのぽち袋+ポストカード+あけおめ動画 データ版

新しく足す種類(2026-11-19)。はじめから墨絵の書き方の指示文(`minne-pochi-next-prompts.md` のペキニーズ)で作った。あるある: 王様歩き。

## 確かめること(出品前)
- 絵を確かめた: 金色にマスク(顔が黒い)のペキニーズが、胸を張って歩いている。床まで届く長い毛、巻いたしっぽ。漫画っぽさはない。もとの絵は templates/originals/pekingese.jpg(2000×2000)

## 商品画像
- ポストカードは縦向き(絵が少し横長なので縦のほうが大きく入る): `make_postcard.py <絵> pekingese full/letter --label "Pekingese"`。商品画像 shop/listing_pekingese_postcard.jpg、机の写真 shop/scene_pekingese_postcard_note.jpg。動画の下じき shop/video_base/pekingese_video_base.png
- ユーザーがGeminiで動画も作った(Canvaではなく)。横長(16:9)で届く見込み。届いたら、解像度・すかし(透かし)の有無・動きを確かめる
- 2026-11-19 ぽち袋のPDF(Pekingese.pdf)から listing_pekingese_1/3 と check/front_pekingese_blank.png を作った。6ページとも64×95mm。Geminiの動画は共有リンク(share.gemini.google)で届いたが、リンクからは動画ファイルを取り出せないので、mp4のダウンロードをお願いした
