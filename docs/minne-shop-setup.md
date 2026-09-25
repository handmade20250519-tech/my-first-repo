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

### 自己紹介文(255文字以内。minneの上限)
```
わが家は、犬、モルモット、カメ、アフリカヤマネ、ハムスター、セキセイインコ、キンカチョウが暮らす、にぎやかな家です。
誰かが何かをやらかすたびに「またそれやってる」と笑い、その子らしいしぐさを眺める時間がいちばん好きです。
そんな「うちの子あるある」を紙ものにして届けたくて、このショップを始めました。
絵は画像生成AIの力を借りて仕上げ、型や作り方は試作を重ねて整えています。
動物と暮らす方と「わかる!」を分け合えたらうれしいです。
```
文字数: 218文字(改行を含む)


## 3. 肩書き

### 考え方
- 今後、ぽち袋以外(カード、シール、ふた留めシール、SNS用の画像データなど)や、小動物・鳥にも広げる可能性がある。→ 商品の種類や「犬猫」に縛られない言葉にする。
- 「作家」「イラストレーター」は、手で描いていると受け取られやすい。絵はAIで仕上げているので避ける。
- ショップの強み(飼い主の目で見た「あるある」)が伝わる言葉にする。

### 候補
| 肩書き | 良い点 | 気になる点 |
|---|---|---|
| **動物あるある観察家**(おすすめ) | 商品の種類にも動物の種類にも縛られない。ショップ名とつながり、覚えてもらいやすい。自分がしていること(観察して、テーマを決める)を正直に表している | 何を売っているかは伝わらない(ショップ名と商品で伝わるので問題は小さい) |
| 動物と暮らす紙ものデザイナー | 何を作っているかが分かる | 紙以外の商品(画像データなど)に広げると合わなくなる |
| うちの子あるある係 | やわらかく、親しみやすい | ショップ名と重なる |

## 4. カバー画像

### 条件(minne)
- 1100×280px以上推奨(横:縦 = 約4:1のとても横長)、8MB以内、JPEG・PNG・GIF
- 仕上げは **2200×560px のJPEG** にする(推奨の2倍。高精細な画面でもぼやけない)
- スマホでは左右が切れる可能性がある(未確認)。→ 大事なものは中央に寄せる

### 考え方
- アイコン(1つの袋に柴犬とキジトラ)と同じ画風・同じ背景色(#F4EFE6)にして、並んだときにひと続きに見えるようにする。
- 「いろいろな犬種・猫の柄がいる店」だと、ひと目で伝える。→ **ぽち袋が横一列に並び、それぞれの袋から違う子が顔を出している**絵。
- 動物は5匹まで。多いとAIが崩しやすく、1匹ずつが小さくなる。
- 文字は入れない(入れるならCanvaで、店名だけを小さく)。

### 作り方A(おすすめ): 商品の絵をCanvaで並べる
- すでに作った商品の絵(背景を消したもの)を、2200×560pxのデザインに横一列に並べる。背景は #F4EFE6。
- 良い点: 商品とまったく同じ絵なので、カバーを見て商品を開いた人が「この絵だ」と分かる。AIの崩れを心配しなくてよい。
- 並べる子の例(左から): トイ・プードル、茶トラ、柴犬(中央)、キジトラ、ダックス。人気の犬種と猫の柄を交互に。

### 作り方B: Geminiで1枚の絵として作る
```
Create an original, warm and gently humorous painting for a wide banner (cover image) of a Japanese online shop that sells pet-themed pochi-bukuro gift envelopes.

SUBJECT: Five small Japanese pochi-bukuro paper envelopes standing upright in one neat horizontal row, evenly spaced, each plain cream color with a small red noshi-style curl mark in its upper right corner. From the opening at the top of each envelope, a different pet pokes out its head and front paws, squeezed in and looking pleased, as if each envelope were its own cozy bed. From left to right: a toy poodle with an apricot teddy-bear cut; an orange tabby cat; a red shiba inu with cream-white cheeks (in the center); a brown mackerel tabby cat; a black-and-tan smooth miniature dachshund with long floppy ears. Each animal has a different, affectionate expression (proud, sleepy, smug, curious, happy). The envelopes are fully opaque: nothing shows through them. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THE CATS MUST LOOK LIKE CATS: small triangular pointed ears, a tiny pink triangle nose with no protruding muzzle, three thin whiskers on each cheek, a small cat mouth shaped like a soft "ω", almond-shaped cat eyes with narrow slit pupils, a flat round cat face.

STYLE: A charming, slightly comic Japanese-style painting that mixes traditional ink-and-light-color painting with a playful manga feel, as if brush-painted on washi paper. Confident sumi ink outlines with natural brush variation in thickness; soft, transparent watercolor washes with gentle bleeding edges. Muted, natural, traditional Japanese colors. Cute, deformed proportions with big round heads. NO sweat drops. NOT a glossy digital anime look: no flat cel shading, no uniform digital outlines, no big shiny anime eyes.

COMPOSITION: Very wide horizontal banner. The row of five envelopes is centered and spans about 70% of the width, and the envelopes and animals fill about 60% of the height, leaving calm empty space above, below and at both ends. Keep every animal fully inside the central area. Plain, soft warm off-white background (#F4EFE6) with no texture, no frame, no floor, no other objects.

TEXT: No text, letters, numbers, seals, signatures or watermarks anywhere.

OUTPUT: Highest available resolution, 21:9 aspect ratio. Crisp artwork.
```
- Geminiの一番横長(21:9)で作り、あとで上下を切って4:1(2200×560px)にする。上下の余白を多めに取らせているのはそのため。

## 5. ショップ名のフォント
- ユーザーは Sniglet:800 を選んだ(太く丸みのある見た目)。
- 注意: Sniglet は英語用のフォントで、日本語の文字は入っていない。表示されている太字は、画面の標準の日本語書体に置き換わったもの。パソコンやスマホの種類によって見た目が変わることがある。

## 6. ショップ紹介文
- 自己紹介(人となり)とは分けて、**お店の中身**を書く。
- 代表的な「あるある」を3つ並べて、どんな店かを一瞬で伝える。
- 今はぽち袋だけだが、今後ほかの紙ものを増やしても書き換えやすいように、「紙もののお店」「今は〜を販売」という書き方にした。

```
犬種・猫の柄ごとの「あるある」を描いた、紙もののお店です。

拒否柴、へそ天のフレブル、ごめん寝のハチワレ…。
飼い主さんなら「うちの子もこれやる!」と笑ってしまう瞬間を、墨と淡い水彩で描いたような絵にしました。

今は、ご自宅で印刷して作る「ぽち袋」のデータを販売しています。
ダウンロードして、A4に印刷して、切って、折って、貼るだけ。のしや「おとしだま」「ありがとう」など、文字違いの6種類が入っています。

絵は画像生成AIを使って仕上げています。テーマや場面、型、作り方の説明書は、店主が考えて試作を重ねています。

まだない犬種・猫の柄は、リクエストをお待ちしています。多頭飼いの組み合わせのご相談もどうぞ。
```
文字数: 310文字(改行を含む)。minneの上限は未確認。
