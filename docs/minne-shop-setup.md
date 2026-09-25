# minneショップの立ち上げ

## 1. ショップアイコン

### 考え方
- 商品と同じ画風(水墨淡彩+少し漫画っぽく)にする。アイコンを見ただけで、商品の絵と同じ店だと分かるようにする。
- 犬と猫の両方を扱う店なので、**犬と猫を1匹ずつ**入れる。
- 商品の「あるある」とぽち袋をつなげて、**1つのぽち袋に犬と猫がぎゅうぎゅうに入って、顔だけ出している**絵にする(キジトラの「入れそうな所には入る」と同じ笑い)。
- アイコンは丸く切り取られて、とても小さく表示されることが多い。→ 絵は中央にまとめ、まわりに余白を取る。細かい描き込みは減らす。
- 文字は入れない。小さくて読めないうえ、AIは文字を崩しやすい。店名はショップ名の欄で伝わる。
- 背景は白ではなく、淡い生成り色にする。白だと、白い画面の中でアイコンの輪郭が消える。

### Gemini用の指示文
```
Create an original, warm and gently humorous painting for a small online shop icon (profile picture) of a Japanese shop that sells pet-themed pochi-bukuro gift envelopes.

SUBJECT: One small Japanese pochi-bukuro paper envelope standing upright, plain cream color with a small red noshi-style curl mark in its upper right corner. A shiba inu (red-orange coat with cream-white cheeks, small triangle ears) and a brown mackerel tabby cat (dark stripes, an M-shape on the forehead, small triangular ears, yellow-green almond-shaped cat eyes with narrow slit pupils) have both squeezed themselves into this one envelope, which is clearly far too small for two. Only their two heads and a front paw each poke out of the opening at the top, side by side, cheeks squished together. The dog looks proud and happy with its eyes closed in a smile; the cat looks satisfied and a little smug with half-closed eyes. The envelope bulges from being overstuffed. The envelope is fully opaque: nothing shows through it. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THE CAT MUST LOOK LIKE A CAT: small triangular pointed ears, a tiny pink triangle nose with no protruding muzzle, three thin whiskers on each cheek, a small cat mouth shaped like a soft "ω", a flat round cat face.

STYLE: A charming, slightly comic Japanese-style painting that mixes traditional ink-and-light-color painting with a playful manga feel, as if brush-painted on washi paper. Confident sumi ink outlines with natural brush variation in thickness; soft, transparent watercolor washes with gentle bleeding edges. Muted, natural, traditional Japanese colors. Cute, deformed proportions with big round heads. Simple and bold enough to stay readable when shown very small (about 1 cm). NO sweat drops. NOT a glossy digital anime look: no flat cel shading, no uniform digital outlines, no big shiny anime eyes.

COMPOSITION: Square. The envelope with the dog and cat sits in the exact center and fills about 65% of the canvas, with even empty space on all sides so that the whole design still fits when the image is cropped into a circle. Plain, soft warm off-white background (#F4EFE6) with no texture, no frame, no floor, no other objects.

TEXT: No text, letters, numbers, seals, signatures or watermarks anywhere.

OUTPUT: Highest available resolution, 1:1 aspect ratio. Crisp artwork.
```

### うまくいかないとき
- 丸く切ると耳が欠ける →「fills about 55% of the canvas」に下げる
- 犬が柴犬以外に見える →「a curled tail is not visible, but the red-orange coat and cream cheeks clearly show it is a shiba」を足す
- 小さくすると何の絵か分からない →「fewer details, larger heads, thicker outlines」を足す

### できたら確かめること
- スマホの画面で、1cmくらいの大きさに縮めて見ても、犬と猫だと分かるか
- 丸く切り取っても、耳や前足が欠けないか

### できたアイコン
- Geminiで作った絵(2000×2000px)を、700KB以下にするため1000×1000pxのJPEGにした(minneの上限700KB)。
- `shop/icon_zoom.jpg`(おすすめ・約120KB): 顔を大きく切り出した版。小さく表示しても犬と猫が分かる。
- `shop/icon_full.jpg`(約70KB): 元の構図のまま縮めた版。小さいと顔が見えにくい。
- `shop/icon_preview.png`: 丸く切ったときの見え方(上: 大きめ、下: 1cmくらい)。

## 2. 自己紹介文(プロフィール)

### 考え方
- 飼い主本人が作っていることを前に出す(犬、モルモット、カメ、アフリカヤマネ、ハムスター、セキセイインコ、キンカチョウと暮らしている)。「あるある」が本物だと信じてもらう根拠になる。
- AIを使っていることを、自己紹介でも隠さずに書く。自分が何をして、AIが何をしているかを分けて書く。
- リクエストを受け付けていることを書く(犬種・猫の柄の追加、多頭飼いの組み合わせ)。
- 飼っている動物の犬種や名前など、ユーザーから聞いていないことは書かない。

### 長い版
```
はじめまして。「うちの子あるある」です。

わが家には、犬のほかに、モルモット、カメ、アフリカヤマネ、ハムスター、セキセイインコ、キンカチョウがいます。
毎日いっしょに暮らしていると、「またそれやってる」と笑ってしまう瞬間がたくさんあります。

このショップでは、そんな犬種・猫の柄ごとの「あるある」を描いた、ぽち袋のデータを販売しています。
ご自宅で印刷して、切って、折って作るぽち袋です。お年玉やちょっとしたお礼を渡すとき、相手が「うちの子もこれやる!」と笑ってくれたらうれしいです。

■ 作り方について
テーマ(どの子の、どんな「あるある」を描くか)、場面、構図、色は私が考え、絵は画像生成AIを使って仕上げています。手描きの原画ではありません。
ぽち袋の型、文字の配置、作り方の説明書は私が作り、実際に何度も印刷して組み立てて確かめています。

■ リクエスト受付中
まだない犬種・猫の柄、多頭飼いの組み合わせなど、お気軽にメッセージでご相談ください。
```

### 短い版(文字数が限られるとき)
```
犬、モルモット、カメ、アフリカヤマネ、ハムスター、インコ、キンカチョウと暮らしています。
犬種・猫の柄ごとの「あるある」を描いた、印刷して作るぽち袋のデータを販売しています。
テーマ・場面・構図は私が考え、絵は画像生成AIで仕上げています。型と説明書は私が作り、試作して確かめています。
ない犬種・猫の柄のリクエストもお気軽にどうぞ。
```
