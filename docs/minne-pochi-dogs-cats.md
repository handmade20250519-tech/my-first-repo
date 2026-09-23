# 「犬のこと、わかってるね」ぽち袋 設計書

## 狙い(STEP3の回答)
- 買う人: **B 犬好き・猫好きの友人や家族への、ちょっとした贈り物**(A 飼い主本人が使う場合も含む)
- ユーモア: 犬種ごとの「あるある」のしぐさ。のんきな犬種はへそ天、神経質な犬種は真剣な顔など、「犬のことをわかっているな」と感じさせる笑い
- セット: 犬メジャーセット/犬レアセット/猫セットの3つ

## ターゲットの判断: Bで良い。Cは今回のぽち袋には合わない
- **B(贈り物)にしておけば、A(自分で使う)も自然に取れる。** 贈り物として選ばれる見た目にしておけば、自分用に買う人も困らない。
- **C(トリミングサロン・動物病院)は、ぽち袋とは合わない。** お店がお客さんにお金を包んで渡す場面はほとんどない。お店に合うのは、来店のお礼カードや誕生日カードのほう。→ Cは、ぽち袋が売れてから「お店用メッセージカード」として別に考える。
- **Bで作るときの決まりごと:** 開けた瞬間に笑えること。犬種がひと目で分かること。袋が並んでいるだけで楽しいこと。

## 犬種を選んだ根拠
- 犬: ジャパンケネルクラブの2025年の犬籍登録で、1位トイ・プードル(69,342頭)、2位チワワ。小型犬の人気が続いている([JKC 犬種別犬籍登録頭数](https://www.jkc.or.jp/registr-statistics/)、[みんなのブリーダー](https://www.min-breeder.com/magazine/15594))。
- 猫: アニコム損保の2026年猫種ランキングは1位スコティッシュ・フォールド。上位10種は前年と同じ([アニコム損保](https://www.anicom-sompo.co.jp/news-release/2025/20260219/))。一方で、日本の飼い猫の約75%は雑種という紹介もある([Flowens Cat](https://cat.flowens.jp/blog/neko-ninki-ranking))。→ **猫セットは、毛柄(茶トラ、三毛など)を中心に、人気の猫種を少し混ぜる。**

---

## STEP4 デザイン設計

### コンセプト
**犬好きの友だちに渡す、「うちの子もそれやる!」と笑える一枚**

### 全体のルール
| 項目 | 内容 |
|---|---|
| 絵柄 | **デフォルメしたイラスト**(ユーザーの希望で変更)。頭を大きく、体と足を短く、目は点か小さな楕円。犬種の見分けどころ(耳の形、毛の色と模様、鼻の長さ、しっぽ)だけを残して少し強調する。やわらかい焦げ茶の線と、平らな色塗り |
| 背景 | 無地の白。1枚に1匹だけ描く(あとでCanvaでぽち袋の型に並べるため) |
| 大きさ | どの犬も猫も、画面の中で同じくらいの大きさにそろえる |
| ユーモア | 犬種・猫種の「あるある」を1つだけ描く。やりすぎず、愛情のある笑いにする |
| 袋の形を生かす | 胴長のダックスは袋の横いっぱい、猫は袋の中に入っている、など。袋の形とあるあるを重ねる |
| 文字 | 絵の中には入れない。「ありがとう」「おめでとう」「おとしだま」などは、**Canvaで後から入れる**(AIは文字を崩しやすいため。データ版では買った人が書き換えられる) |

### 作り方の流れ
1. Geminiで、1匹ずつ白い背景の絵を作る(下の共通指示文+犬種ごとの一文)
2. Canvaで背景を消し、ぽち袋の展開図(切り線・折り線入り)に配置する
3. 文字をCanvaで入れる
4. データ版: A4に展開図を並べたPDF+作り方の説明をZIPにしてダウンロード販売
5. 印刷版(反応を見てから): 全員が1枚に並ぶ柄を1つ作り、羽車で100枚刷る

### Gemini(Nano Banana Pro)用 共通指示文
`[BREED LINE]` の部分を、下の表の一文に差し替えて使う。

```
Create an original, warm and humorous illustration of a single animal for a Japanese gift envelope (pochi-bukuro).

SUBJECT: [BREED LINE]
The humor must feel affectionate and true to life, the kind of moment real owners of this breed instantly recognize. Even in the simplified style, the breed must be clear at a glance. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

STYLE: Cute, simplified cartoon illustration with deformed (chibi-like) proportions: a big round head, a small soft body, short stubby legs, and simple dot or small oval eyes. Keep only the few features that make the breed instantly recognizable (ear shape, coat color and markings, muzzle length, tail) and exaggerate them slightly. Clean, smooth outlines in a soft dark brown, flat colors with gentle shading, warm and friendly palette. Simple shapes that stay readable when printed small (about 5 cm tall).

COMPOSITION: One animal only, centered, filling about 70% of the canvas height, with generous empty space around it. Plain pure white background, no floor, no shadow except a very light one under the animal, no props unless described above.

TEXT: No text, letters, numbers, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```

### 犬メジャーセット(10種)
| 犬種 | あるある | [BREED LINE] に入れる一文 |
|---|---|---|
| トイ・プードル | 賢くて、ほめられるのが大好き。トリミング帰りは、つま先立ちで跳ねるように歩き、「見て見て」と得意顔 | A toy poodle just back from the groomer, prancing on the tips of its toes with a light, bouncy step, one front paw lifted mid-stride. Chin raised high, eyes closed in a smug little smile, clearly waiting to be told how beautiful it is. Freshly trimmed teddy-bear cut: round fluffy head, round muzzle, fluffy round ears, tidy round legs, small pom-pom tail. A tiny ribbon clipped on one ear, as groomers often add. Coat color: soft apricot, with tight curly texture shown by small simple curls along the outline. |
| チワワ | 体はいちばん小さいのに、気持ちは番犬。何かに向かって勇ましく吠えるけれど、足はぷるぷる震えている | A tiny chihuahua bravely standing its ground and barking at something off the edge of the canvas, as if it were a big guard dog: chest puffed out, head held high, mouth open in a small bark, huge ears standing straight up, eyes wide and fierce. At the same time its little legs are trembling, shown by a few small shake lines around the legs, and its tail is tucked slightly. Brave on top, nervous underneath. Classic chihuahua features: round apple-shaped head, very large upright ears, short pointed muzzle, large round shiny eyes (this breed may have bigger eyes than the other animals), tiny delicate body, short smooth coat. Coat color: white with light fawn patches. |
| ミニチュア・ダックスフンド(スムースヘアード) | アナグマ猟の名残で、毛布に潜りたがる。長い胴の形の山ができ、顔だけ出して満足げ | A smooth-haired miniature dachshund burrowed deep under a small soft blanket, as dachshunds love to do. The blanket forms one long, low tunnel-shaped bump that clearly shows its extremely long body, with just the tip of the tail sticking out at the far end. Only its head pokes out of the near end, long nose resting on its paws, eyes content and proud of its cozy den. Classic smooth dachshund features: short sleek shiny coat in black and tan (glossy black with tan eyebrow dots, tan muzzle and tan paws), long floppy ears, long muzzle. The blanket is a plain, soft solid color. Wide horizontal composition inside the square: the long bump spans about 80% of the canvas width. |
| 柴犬 | 散歩の帰り道、踏ん張って動かない(拒否柴) | A red shiba inu refusing to walk: front legs stiffly braced forward, body leaning far back, bottom lowered toward the ground. A leash from its collar is pulled tight and runs straight out of the right edge of the canvas (no person visible). Ears pinned back, eyes squeezed into narrow flat lines, chin tucked, cheeks puffed, a firm "absolutely not" face. Classic shiba features: red-orange coat with cream-white urajiro markings on the cheeks, chest and belly, small triangle ears, tightly curled tail. |
| ポメラニアン | 好奇心いっぱいで元気。うれしいと、その場でくるくる回る。回るたびに毛がふくらんで、まん丸のかたまりになる | A pomeranian spinning in excited little circles on the spot, as poms do when something wonderful is about to happen. Its fluffy coat has puffed out into an almost perfect round ball of fur, with tiny paws and a small, beaming fox-like face with a wide open-mouthed happy grin. A few simple curved motion lines circling around it show the spin, and a few loose tufts of fluff float in the air. Classic pomeranian features: very full double coat forming a ruff around the neck, small upright pointed ears nearly hidden in the fluff, short fox-like muzzle, plumed tail curled over the back. Coat color: warm cream. |
| フレンチ・ブルドッグ | のんきで甘えん坊。どこでもへそ天で爆睡し、後ろ足はカエル足、舌をちょろっと出していびきをかく | A french bulldog fast asleep on its back in a completely carefree belly-up pose: front paws curled on its chest, back legs splayed wide like a frog, round belly up. Its head is tilted to one side, a tiny tip of pink tongue sticking out, cheeks squished, and a small round nose bubble at one nostril to show deep, snoring sleep. A few small wavy snore lines above its face (lines only, no letters, no "Z"). Classic french bulldog features: large upright bat ears (flopped slightly to the sides in sleep), short flat face with wrinkles over the nose, compact muscular body, very short tail. Coat color: dark brindle with a white patch on the chest. |
| ゴールデン・レトリーバー | 人が大好きで、運ぶのが得意。帰ってくると必ず「おみやげ」をくわえて出迎え、うれしすぎてお尻ごとしっぽを振る | A golden retriever greeting its person at the door with a "welcome home present": a single slipper held gently in its mouth, presented proudly. Its whole rear end is wiggling with joy, tail wagging so hard it is shown with a few curved motion lines, eyes squeezed into happy crescents, ears bouncing. Classic golden retriever features: soft wavy golden coat with feathering on the ears, chest, legs and tail, friendly broad head, medium drop ears, long plumed tail. Coat color: warm golden. The slipper is a plain, soft solid color. |
| シベリアン・ハスキー | おしゃべりで大げさ。「だめ」と言われると、ひっくり返って「ウーワウー」と口答えする | A siberian husky throwing a dramatic little tantrum after being told "no": flopped over on its side and back, legs kicking in the air, head thrown back, mouth open in a long complaining "awoo-woo" talking-back howl, eyebrows raised in exaggerated outrage. A few small curved sound lines near its mouth (lines only, no letters). Classic husky features: black and white coat with the distinctive white face mask and dark cap, upright triangle ears, fluffy sickle-shaped tail, small oval eyes in light icy blue. |
| ウェルシュ・コーギー・ペンブローク | 食いしん坊で抜け目ない。後ろ足をぺたんと伸ばした「カエル足ふせ」で、食パンのようなお尻を見せながら、振り返って「おやつは?」と圧をかける | A pembroke welsh corgi lying flat on its belly in the famous "sploot": both short back legs stretched straight out behind like a frog, showing off its big round fluffy rear shaped like a soft loaf of bread, with no tail. It is looking back over its shoulder toward the viewer with a hopeful, slightly demanding "treat, please?" face, eyebrows raised, ears perked. Classic pembroke corgi features: very short legs, long low body, large upright pointed ears, fox-like face, red-and-white coat with a white blaze, white chest and white paws, cream-white fluffy rear. |
| ビーグル | 鼻がすべて。においを見つけると、呼んでも聞こえないふりで、鼻を地面につけたままジグザグに追いかける | A beagle completely absorbed in following a scent: nose glued to the ground, body low, trotting along a zigzag trail of small dotted lines on the white background that leads off the edge of the canvas. Eyes half closed in blissful concentration, clearly pretending not to hear anyone calling its name. One long ear has flipped inside out from the rush, the other drags near the ground. Tail held straight up like a flag with a bright white tip. Classic beagle features: tricolor coat (black saddle on the back, tan head and sides, white muzzle, chest, legs and tail tip), long soft drop ears, gentle hound face. |

### 犬レアセット(8種)
| 犬種 | あるある | [BREED LINE] に入れる一文 |
|---|---|---|
| ボルゾイ | 外では貴族のように優雅。家では仰向けで、長い足を四方に折り曲げた変な寝相。それでも顔だけは気品のある真顔 | A borzoi asleep upside down on its back in the typical sighthound "roach" pose: long thin legs folded and sticking up in four different awkward directions, long plumed tail curled around, silky coat spilling to the sides. Yet its long, narrow, aristocratic face remains perfectly calm, noble and serious, eyes gently closed, as if posing for a royal portrait. Classic borzoi features: very long narrow muzzle, small folded-back ears, long silky wavy coat, deep narrow chest, long legs. For this breed only, keep the long narrow muzzle and noticeably longer legs than the other animals, while the head stays cute and simplified. Coat color: white with soft light-gray patches. |
| グレート・デーン | 自分を小型犬だと思って、人の膝に乗ろうとする | A great dane trying to sit on a small cushion far too small for it, its huge body overflowing, with an innocent face as if it thinks it is a small dog. |
| セント・バーナード | よだれを垂らして、のんびり寝そべる | A saint bernard lying down calmly with a sleepy, gentle face and a small, comical drip of drool from its jowls. |
| バーニーズ・マウンテン・ドッグ | 大きな体で、甘えて仰向け | A bernese mountain dog rolling on its back, big fluffy body twisted, paws curled, begging for a belly rub with a sweet face. |
| イタリアン・グレーハウンド | 寒がりで、セーターを着て震える | An italian greyhound wearing a cozy knitted sweater, thin legs trembling slightly, with a delicate, slightly worried face. |
| アフガン・ハウンド | 長い毛がなびいて、前が見えていない | An afghan hound with long silky hair flowing dramatically over its face so it can barely see, holding a proud, elegant pose. |
| サモエド | いつもにっこり、口角が上がった顔 | A samoyed with its famous smile, corners of the mouth turned up, fluffy white coat, sitting happily with eyes squinting in joy. |
| ニューファンドランド | 水が大好き。濡れてぺたんこ | A newfoundland dog completely soaking wet, its thick fur flattened, looking proud and satisfied as if it just had a great swim. |

### 猫セット(10種)
| 毛柄・猫種 | あるある | [BREED LINE] に入れる一文 |
|---|---|---|
| 茶トラ | 人なつこく、へそ天で撫でを待つ | An orange tabby cat lying on its back with its belly up, paws curled, looking relaxed and friendly. |
| キジトラ | 箱(袋)に入って、満足げ | A brown mackerel tabby cat sitting snugly inside a small paper envelope that is clearly too small, with a satisfied face. |
| 三毛 | 前足を折りたたんだ香箱座りで、じっと見る | A calico cat sitting in a neat "loaf" pose with paws tucked under, calmly and knowingly staring forward. |
| 黒猫 | 暗いところで、目だけ光っている | A black cat curled up so its body blends into a dark shadow, with only its two bright round eyes clearly visible. |
| ハチワレ | 顔を前足に押しつけた「ごめん寝」 | A black-and-white tuxedo cat sleeping with its face pressed down into its paws in an apologetic-looking pose. |
| サバトラ | 液体のように、狭いところにぴったり収まる | A silver mackerel tabby cat poured like liquid into a round bowl, its body perfectly filling the shape. |
| スコティッシュ・フォールド | 足を投げ出して座る「スコ座り」 | A scottish fold cat sitting upright like a person with its back legs stretched out in front and its belly showing, looking calm. |
| マンチカン | 短い足で、精いっぱい立ち上がる | A munchkin cat standing up on its short hind legs, stretching as tall as it can, with a curious, determined face. |
| ラグドール | 抱っこされると、ぐにゃりと力が抜ける | A ragdoll cat completely limp and relaxed, draped as if being held (no person visible), eyes half closed in bliss. |
| ブリティッシュ・ショートヘア | まん丸の顔で、無表情に座る | A british shorthair cat with a very round face sitting still, looking straight ahead with a completely neutral, unimpressed expression. |

### 生成のコツ
- デフォルメしすぎて犬種が分からなくなったら、その犬種の見分けどころを一文足す(例: 「long body and very short legs」「curled tail and triangle ears」)。
- 人間のようなポーズや表情になりすぎたら「animal-like pose, no human clothing, no human gestures」を足す(イタグレのセーターなど、指示したものは除く)。
- 犬種の特徴が弱いときは、その犬種の見分けどころ(ダックスの胴、コーギーの短い足など)を一文足す。
- 画風は「デフォルメしたイラスト」で確定(ユーザーが決定)。
- 画風がばらつかないよう、**共通指示文は変えずに、[BREED LINE]だけ差し替える**。同じチャットで続けて作ると画風がそろいやすい。

---

## この先
- セットごとの価格、データ版の中身(展開図の枚数・サイズ)、出品文(STEP5)は、試作の絵を見てから決める。
- 印刷版は、データ版で売れたセットだけを、羽車で「全員が1枚に並ぶ柄」として100枚刷る。
