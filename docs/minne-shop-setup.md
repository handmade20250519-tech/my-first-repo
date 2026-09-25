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

### 考え方(ユーザーの指示で書き直し)
- 商品の紹介は、それぞれの商品説明に書く。自己紹介は**人となりが分かる文章**にする。
- 何を作っているかは大まかに一言だけ。AIを使っていることは、隠さずに短く触れる。
- ユーザーから聞いた事実だけで書く(たくさんの動物と暮らしている、紙が好きでマーメイド紙をよく使う、試作をくり返している)。

### 自己紹介文
```
はじめまして。

わが家は、犬、モルモット、カメ、アフリカヤマネ、ハムスター、セキセイインコ、キンカチョウが暮らす、ちょっとにぎやかな家です。
朝から晩まで、誰かが何かをやらかしていて、そのたびに「またそれやってる」と笑ってしまいます。
種類も性格もばらばらなのに、どの子にも「この子らしいなあ」と思うしぐさがあって、それを眺めている時間がいちばん好きです。

紙も好きで、手ざわりのいい紙を見つけると、つい何か作りたくなります。

そんな「うちの子あるある」を、紙ものにして届けたいと思って、このショップを始めました。
絵は画像生成AIの力を借りて仕上げ、型や作り方は、自分で何度も試作しながら整えています。

動物と暮らす方と、「わかる!」を分け合えたらうれしいです。
```
