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

### 犬メジャーセット(13種)
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
| ウエスト・ハイランド・ホワイト・テリア | 小さくても勇敢なテリア。穴掘りが大好きで、庭を掘ったあとは真っ白な顔と足が泥だらけ。それでも「大仕事をした」と得意顔 | A west highland white terrier standing proudly next to a small hole it has just dug in a little mound of soil, chest out, tail straight up like a carrot, looking extremely pleased with itself as if it just finished an important job. Its normally snow-white face, beard and front paws are now smudged with brown dirt, a little clump of soil on the tip of its nose, and a few small bits of dirt flying from the hole. Classic westie features: small sturdy terrier body, round chrysanthemum-like face framed by fluffy white hair, small pointed upright ears, dark eyes and black nose, short carrot-shaped tail held up. Coat color: pure white (with the dirt only on the face, beard and front paws). Because the dog is white on a white background, draw it with the soft dark-brown outline and very light cream shading so its shape stays clear. The soil mound is small and simple. |
| ジャック・ラッセル・テリア | 疲れ知らずのバネ。ボールを見ると、自分の体の何倍もの高さまで真上に跳び上がる。何時間遊んでも「もう一回!」 | A jack russell terrier launching itself straight up into the air like a spring, all four legs completely off the ground, body stretched, ears flapping, eyes locked with intense, laser-focused determination on a small ball floating just above its nose. Its face says "again! again!" even though it has clearly been playing for hours. A few simple vertical motion lines below its paws show how high it jumped. Classic jack russell features: small, compact, athletic terrier body, folded button ears, alert bright eyes, short upright tail, short smooth coat. Coat color: white body with tan and black patches on the head and ears. The ball is a plain, soft solid color. |
| ボーダー・コリー | 羊飼いの犬で、とにかく賢く働き者。羊がいなくても、おもちゃでも何でも集めて見張る。低く伏せて、あの鋭い「アイ(にらみ)」で管理中 | A border collie crouched low to the ground in its classic herding stalk: front legs bent, chest almost touching the floor, head lowered level with its shoulders, one front paw slightly lifted. It is giving an intense, unblinking herding "eye" stare at three small plain toy balls that it has carefully gathered into a neat little group in front of it, clearly in charge and not letting a single one escape. Serious workaholic face, ears half up, tail low. Classic border collie features: medium athletic body, alert semi-erect ears with tipped-over tips, medium-length coat with a fluffy ruff and feathered tail, black-and-white coat with a white blaze, white collar, white chest, white paws and white tail tip. The balls are plain, soft solid colors. |

### 犬レアセット(8種)
| 犬種 | あるある | [BREED LINE] に入れる一文 |
|---|---|---|
| ボルゾイ | 外では貴族のように優雅。家では仰向けで、長い足を四方に折り曲げた変な寝相。それでも顔だけは気品のある真顔 | A borzoi asleep upside down on its back in the typical sighthound "roach" pose: long thin legs folded and sticking up in four different awkward directions, long plumed tail curled around, silky coat spilling to the sides. Yet its long, narrow, aristocratic face remains perfectly calm, noble and serious, eyes gently closed, as if posing for a royal portrait. Classic borzoi features: very long narrow muzzle, small folded-back ears, long silky wavy coat, deep narrow chest, long legs. For this breed only, keep the long narrow muzzle and noticeably longer legs than the other animals, while the head stays cute and simplified. Coat color: white with soft light-gray patches. |
| グレート・デーン | 体は超大型なのに、心は小型犬。小さな犬用ベッドに無理やり丸まって、満足げ | A great dane that believes it is a small lap dog, squeezed into a tiny round dog bed meant for a small breed: only its bottom and one elbow actually fit inside, while its long legs, big chest and head spill out over every side. Despite the obvious mismatch it looks perfectly content and innocent, chin resting on the rim of the bed, eyes soft and sleepy, as if this is exactly where it belongs. Classic great dane features: very large, tall, sleek body, long legs, broad square muzzle, natural floppy ears (not cropped), short smooth coat. For this breed only, make the body and legs clearly larger and longer than the other animals, so the size contrast with the small bed reads instantly, while the face stays cute and simplified. Coat color: fawn with a black mask. The dog bed is a plain, soft solid color. |
| セント・バーナード | おっとりした優しい大型犬。暑さは苦手で、雪が大好き。雪の上に寝そべると、とろけるような至福の顔になり、よだれもひとしずく | A saint bernard lying on its belly on a small patch of fresh snow, as happy as can be in the cold: body completely relaxed and spread out, big head resting on its paws, heavy jowls drooping, eyes half closed in pure bliss, and one small comical drip of drool at the corner of its mouth. A single snowflake has landed on its nose and a few simple snowflakes drift around it. Classic saint bernard features: very large, heavy, gentle body, broad head with a short deep muzzle, loose jowls, medium drop ears, red-and-white coat with a white blaze down the face, white chest and paws, and a dark mask around the eyes. The snow patch is a small, simple pale mound, and the rest of the background stays plain white. |
| バーニーズ・マウンテン・ドッグ | 大きな体の、甘えん坊。撫でる手が止まると、大きな前足で「ちょいちょい」とつついて催促する | A bernese mountain dog sitting and leaning its big fluffy body slightly toward the viewer, raising one huge front paw mid-air in a gentle "pat, pat" gesture, as if tapping someone who has just stopped petting it. Head tilted, soft pleading eyes, ears relaxed, mouth closed in a sweet, patient little smile: "more, please." Classic bernese features: large sturdy body, long silky thick coat, broad head, triangular drop ears, bushy tail, and the distinct tricolor pattern: jet black body, rust-brown eyebrow dots, cheeks and legs, white blaze down the face, white muzzle and a white cross-shaped marking on the chest, white paw tips. |
| イタリアン・グレーハウンド | 毛が短くて大の寒がり。部屋でいちばん暖かい日だまりを見つける名人で、セーターを着たまま、その小さな日だまりの中で丸まって眠る | An italian greyhound wearing a cozy knitted sweater, fast asleep lying down on its side inside one small square patch of warm sunlight on the floor. Its whole body rests flat on the floor, curled into a tight round donut shape: back curved, long thin legs tucked in, thin tail wrapped around to its nose. Its head lies down resting on its own legs, fully relaxed, eyes gently closed as soft curved lines, mouth relaxed in a tiny peaceful smile, as if it has claimed the warmest spot in the house and drifted off to sleep. The dog is lying down, NOT sitting, NOT holding its leg, NOT upright. The sunlight patch is a simple soft pale-yellow square shape on the plain white background. Classic italian greyhound features: very slender, delicate body, long thin legs, long narrow muzzle, small folded-back rose ears, thin tail, very short smooth coat. For this breed only, keep the slender legs and long narrow muzzle, while the head stays cute and simplified. Coat color: soft blue-gray. The sweater is a plain, soft solid color. |
| アフガン・ハウンド | 猫のように気高くマイペース。ごはんのときは、長い耳の毛が器に入らないよう、筒状の「スヌード」をかぶせられる。それでも女王さまのように澄ました顔 | An afghan hound sitting upright with regal dignity in front of a small plain food bowl, wearing a snug knitted tube-shaped snood pulled over its head and long ears, the way owners keep those long silky ear feathers out of the bowl at mealtime. Nose held high, eyes half closed, a perfectly composed, queenly and slightly aloof expression, as if the snood were a royal crown. Long, flowing silky coat cascading down its body and legs like a gown, ring-curled tail tip. Classic afghan hound features: long narrow elegant head, long silky flowing coat, topknot of hair on the crown, curled tail tip. For this breed only, keep the long narrow head and the long flowing coat, while the face stays cute and simplified. Coat color: golden cream with a dark mask on the muzzle. The snood and bowl are plain, soft solid colors. |
| サモエド | いつもにっこり「サモエドスマイル」。ただし換毛期は抜け毛がすごく、「もう1匹作れる」ほどの毛の山ができる。それでも本人は満面の笑み | A samoyed sitting happily with its famous "samoyed smile": corners of the mouth turned up, eyes squeezed into joyful crescents. Right beside it sits a huge, soft heap of its own shed white fur, almost as big as the dog itself, as happens during shedding season, when owners joke they could make a second dog. The fur heap is just a fluffy mound with no face, no eyes and no legs. A few loose tufts of fur float in the air. The dog looks completely unbothered and proud. Classic samoyed features: thick fluffy pure white double coat, upright triangle ears, black nose and lips, plumed tail curled over the back. Because the dog is white on a white background, draw it with the soft dark-brown outline and very light cream shading so its shape stays clear. |
| ニューファンドランド | 水難救助の犬で、水が大好き。水を見ると「救助」に飛び込む。上がってくると、ふかふかの毛がぺたんこになって別の犬のように細く見えるのに、本人は任務を終えた誇らしげな顔 | A newfoundland dog that has just climbed out of the water after a proud "rescue mission": standing on a small simple puddle, holding a small floating ring toy gently in its mouth as if it has just saved it. Its usually huge fluffy coat is completely soaking wet and plastered flat against its body, making it look surprisingly slim and a little silly, with water dripping from its ears, chin and belly and a few water droplets around it. Its face is full of pride and satisfaction, chest out, tail swinging, like a hero returning from duty. Classic newfoundland features: very large sturdy body, broad massive head, short square muzzle, small drop ears, webbed paws, thick coat (flattened here because it is wet). Coat color: black. The ring toy and the puddle are plain, soft solid colors. |

### 猫用の共通指示文(猫に見えなかったため追加)
犬用の共通指示文は「鼻の長さ(muzzle length)」など犬向けの言葉が入っていて、猫が犬やクマのように描かれやすい。猫は、画風の部分(線の色、平らな色塗り、頭の大きいデフォルメ)はそのままにして、**猫らしさを決める特徴を必ず描く**指示を足したこの文を使う。

```
Create an original, warm and humorous illustration of a single cat for a Japanese gift envelope (pochi-bukuro).

SUBJECT: [BREED LINE]
The humor must feel affectionate and true to life, the kind of moment real cat owners instantly recognize. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THIS IS A CAT, NOT A DOG: always include clear cat features: small triangular pointed ears on top of the head, a tiny pink triangle nose right between the eyes with no protruding snout or muzzle, three thin whiskers on each cheek, a small cat mouth shaped like a soft "ω", a long flexible tail, and small round paws. Flat, round cat face.

STYLE: Cute, simplified cartoon illustration with deformed (chibi-like) proportions: a big round head, a small soft body, and simple dot or small oval eyes. Keep the coat color and markings accurate so the pattern or breed is recognizable, and exaggerate them slightly. Clean, smooth outlines in a soft dark brown, flat colors with gentle shading, warm and friendly palette. Simple shapes that stay readable when printed small (about 5 cm tall).

COMPOSITION: One cat only, centered, filling about 70% of the canvas height, with generous empty space around it. Plain pure white background, no floor, no shadow except a very light one under the cat, no props unless described above.

TEXT: No text, letters, numbers, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```

### 猫セット(10種)
| 毛柄・猫種 | あるある | [BREED LINE] に入れる一文 |
|---|---|---|
| 茶トラ | 人なつこくて食いしん坊と言われる。ごはんの時間が近づくと、空の器の前に座り、前足で器のふちをちょんと押さえて、無言の圧をかける | An orange tabby cat sitting perfectly upright in front of an empty food bowl, one front paw placed firmly on the rim of the bowl, staring straight at the viewer with a silent, heavy, expectant "it is time" look: eyes half-lidded and unblinking, mouth closed in a flat line. The humor is its calm, patient pressure. Round cheeks, slightly plump, friendly body. Classic orange tabby features: warm orange coat with darker orange stripes, an M-shape on the forehead, striped cheeks and legs, ringed tail, cream-white chin and chest. The bowl is a plain, soft solid color and clearly empty. |
| キジトラ | 「入れそうな所には入る」。小さすぎるぽち袋にも無理やり入り、顔だけ出して満足げ | A brown mackerel tabby cat that has squeezed its whole body into a small paper envelope that is clearly far too small. The envelope lies on its side with the open end facing the viewer. Only the cat's head and two front paws poke out of the opening; the rest of its body AND its tail are completely hidden inside the envelope. The envelope is made of thick, fully opaque paper: the cat's body, legs, stripes and tail must NOT show through it at all, with no see-through effect and no body outline drawn on the paper. The only sign of the cat inside is that the envelope bulges into a tight, round, overstuffed shape. The cat's eyes are half closed and it looks completely satisfied, as if the envelope was made for it. Classic brown tabby features (visible on the head and paws only): warm brown-gray coat with dark mackerel stripes, an M-shape on the forehead. The envelope is a plain, soft solid color with no writing and no pattern. |
| 三毛 | 気が強くてマイペース。香箱座りでくつろいでいるが、撫でようとすると横目で「今はだめ」 | A calico cat sitting in a neat "loaf" pose with all paws tucked under, looking relaxed, but giving a sharp sideways glance toward the viewer with one eyebrow raised, the tip of its tail flicking, clearly saying "not now." Classic calico features: white base coat with distinct patches of orange and black, especially on the head, back and tail. |
| 黒猫 | 丸まって寝ていると、真っ黒でどこが顔か分からない。おやつの袋の音がした瞬間、耳がぴんと立ち、金色の目だけがぱっちり開く | A black cat curled up asleep in a round "ammonite" curl, lying on its side with its long tail wrapped all the way around its body and the tip resting over its nose, front paws tucked in. Its head is still resting on its curled body, but both ears have just shot straight up and turned forward, and its two big round golden eyes have popped wide open, as if it has just heard the treat bag rustle. The body stays still and sleepy while only the ears and eyes are wide awake. The cat shape must stay clearly readable: the triangular ears, the round face, the wrapped tail and the tucked paws are each clearly separated by the outline and by soft charcoal-gray highlights on the black coat. White whiskers stand out against the black face. Classic black cat features: glossy solid black coat (drawn in deep charcoal with lighter gray highlights), golden-yellow eyes. |
| ハチワレ | 顔を床にうずめて眠る「ごめん寝」。まるで深々と謝っているように見える | A black-and-white tuxedo cat asleep in the famous "apology sleep" (gomen-ne) pose, seen from the front: it is crouched low with its round back curved up, and its face is pressed down into the floor between its two white front paws, as if bowing deeply to say sorry. Its forehead faces the viewer, so the black cap with the white upside-down V "hachiware" split running down between the eyes is clearly visible, along with the tips of its white whiskers peeking out on both sides. Both black triangular ears stick up on top, and its long black tail curls around beside its body. It looks completely peaceful and a little comical. Classic tuxedo cat features: black back, head and ears, white chest, white paws, and a symmetrical white "hachiware" split on the face. |
| サバトラ | 昼間はおとなしいのに、夜中になると突然走り回る「夜中の運動会」 | A silver mackerel tabby cat in the middle of a sudden midnight zoomies sprint, seen from the side and running toward the right: all four legs stretched out mid-gallop, back arched, ears pressed flat but still clearly triangular, tail puffed up like a bottle brush. Its head is turned toward the viewer, with huge round wild eyes and a small open "ω" mouth, clearly having no reason at all to be running. A few simple speed lines behind it show how fast it is going, and one small pale crescent moon in the upper corner hints that it is the middle of the night. Classic silver tabby features: pale silver-gray coat with crisp dark gray mackerel stripes, an M-shape on the forehead, ringed tail. |
| スコティッシュ・フォールド | 足を前に投げ出し、人間のおじさんのように座る「スコ座り」で、くつろぎきった顔 | A scottish fold cat sitting upright on its bottom like a small person relaxing on the floor, back legs stretched straight out in front, round belly showing, front paws resting on its belly, with a calm, completely relaxed, slightly sleepy half-closed-eye face, like an old man after a big meal. EXCEPTION TO THE EAR RULE BELOW: for this breed only, the ears are NOT upright; they are small and folded forward and down, lying flat against the very round head like a little cap, so the head looks almost perfectly round. Classic scottish fold features: very round head with folded-down ears, round eyes, round cheeks, plush dense coat. Coat color: soft gray-blue. |
| マンチカン | 好奇心旺盛。気になる物音がすると、短い後ろ足だけでミーアキャットのように立ち上がって見回す。立っても背はほとんど高くならない | A munchkin cat standing up on its very short hind legs like a meerkat to see what that sound was, body stretched as tall as it can go, tiny front legs dangling in front of its chest, ears perked forward, eyes wide and curious, with a serious, slightly comical face. Even standing at full height it is still only a little taller than when sitting. For this breed only, make the contrast clear: a normal-length body on noticeably extra-short legs, much shorter than the other cats. Classic munchkin features: extra-short legs, normal-length body, round face, upright triangular ears, long tail used for balance. Coat color: cream with light brown tabby stripes. |
| ラグドール | 名前は「ぬいぐるみ」の意味。抱っこされると力が抜けて、ぐにゃりと伸びる。どこに置かれても、そのままとろけている | A ragdoll cat draped completely limp over a small round cushion like a soft towel hung to dry: its front half hangs down the left side with front legs dangling, and its back half and fluffy tail hang down the right side. Its head hangs down but is turned toward the viewer, face upside-down-relaxed and blissful, eyes half open so the bright blue color still shows, a tiny contented "ω" mouth. Its whole body looks boneless and melted, as if it would stay like that forever. Classic ragdoll features: large fluffy body, semi-long silky coat, bright blue eyes, colorpoint pattern: creamy white body with darker seal-brown ears, face mask, legs and tail. The cushion is a plain, soft solid color. |
| ブリティッシュ・ショートヘア | 落ち着きすぎている。目の前で猫じゃらしを必死に振られても、目で追いもせず無表情。ぬいぐるみのような「動かないクマ」 | A british shorthair cat sitting upright and perfectly still like a plump teddy bear, looking straight ahead with a completely neutral, unimpressed, deadpan expression, while a small feather toy on a thin string dangles and swings right in front of its nose. The string simply enters from the top edge of the canvas (no person, no hand, no stick visible). A few small motion lines show the feather swinging busily, but the cat's eyes do not follow it at all and not a single whisker moves. Classic british shorthair features: very round face, full chubby cheeks, small rounded ears set wide apart, dense plush coat, stocky round body, short thick legs, thick tail, big round copper-orange eyes. Coat color: solid blue-gray. |

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

---

## データ版の売り方: 1種ずつ+セットの両方を出す

### ユーザーの提案
- データ販売なら、1種ずつダウンロードできるようにすれば、セットの大きさを気にしなくてよい

### 判断: 賛成。ただしセットもやめない
| | 1種ずつ | セット |
|---|---|---|
| 良い点 | 自分の犬種だけ欲しい飼い主に合う。商品名に犬種名が入るので、「トイプードル ぽち袋」のような検索に1つずつ引っかかる。在庫ゼロなので何種類出しても損をしない | ユーザーの調査で、**いろいろな犬種をまとめたセットに良いレビューがたくさん付いていた**(柴犬だけの商品はレビューが少なかった)。贈り物(ターゲットB)として選ばれやすい |
| 気になる点 | 出品の数が増え、1つずつ写真や説明文を用意する手間がかかる | 大きすぎると選びにくい |

→ **両方出す。** 1種ずつの価格を合計したより、セットを割安にする。

### 出品の組み立て(案)
1. **最初に出すもの:**
   - セット3つ(犬メジャー、犬レア、猫)
   - 1種ずつは、人気の上位5種(トイ・プードル、チワワ、ダックス、柴犬、ポメラニアン)だけ
2. **増やし方:** セットの中でよく反応がある犬種(お気に入りや問い合わせ)から、1種ずつの出品を足していく。
3. **セットの中身の大きさは気にしなくてよい。** メジャーセットは13種のままでよい。

### ダウンロード販売の決まり(minne)
- 1作品に1ファイル。複数のファイルはZIPにまとめる。
- 支払いはクレジットカードのみで、購入はWebからのみ。

### 価格(仮。minneで同じ種類のデータの価格を確かめてから決める)
- 1種ずつ: 200〜300円
- セット: 1種ずつの合計の半額前後(例: 13種で1,000〜1,200円)

### 訂正: セットの根拠はデータ版には当てはまらない
- ユーザーの指摘: 多犬種セットに付いていた良いレビューは、**出来上がったぽち袋(実物)**へのレビューで、ダウンロード版へのものではなかった。
- 実物のセットの評価を、データ版のセットにまで広げて根拠にしたのは誤り。**データ版でセットが売れるという証拠は無い。**

### 改めた判断: データ版は1種ずつだけで始める
- 最初は**1種ずつだけ**を出品する。セットは作らない。
- まずは人気上位の犬種と猫から出し、反応を見て増やす。
- 同じ人が何種類も続けて買う、または「まとめて欲しい」という問い合わせが来たら、そのときにセットを作る。
- 実物の多犬種セットのレビューは、**羽車で刷る印刷版**(1枚に多くの犬種が並ぶ柄)の根拠として残す。

### 犬の種類の増やし方(ユーザーが決定)
- 犬は、今ある犬種で出品を始める。**ほかの犬種は、リクエストがあったら作り足す。**
- 各出品の説明文の最後に「ほかの犬種もリクエストを受け付けています。minneの『質問』からお気軽にどうぞ」と書き、リクエストが届く入口を作る。
- リクエストの多さは、そのまま「その犬種が欲しい人がいる」証拠になる。記録しておく。

### 多頭飼いの人のリクエストにも応える(ユーザーが決定)
- 例: 「柴犬とキジトラ」「トイ・プードル2匹」など、1つのぽち袋に複数の子を入れたい人。
- **作り方:** 新しく絵を生成しない。すでにある1匹ずつの絵を、Canvaでぽち袋の型に並べるだけにする。画風がそろったまま、手間も少ない。
- **値段:** 1匹ずつの値段に、並べる手間の分を少し足す(例: 2匹なら1匹の値段×2に100円前後)。
- **確かめること:** minneのダウンロード販売は、出品のときにファイルを登録しておく仕組み。買う人ごとに作る組み合わせのデータを、どうやって渡すか(その人専用の出品ページを作る、など)を、minneのヘルプで確認する。minneの外でファイルを送るやり方は、規約に触れる可能性があるので避ける。
- **将来の発展:** 2匹が一緒に何かしている絵(猫が犬の背中で寝ている、など)は喜ばれそうだが、2匹を同時に生成すると画風や大きさがそろいにくい。リクエストが多ければ試す。

### 猫の「種類と性格」について(ユーザーの質問への回答メモ)
- **猫種(純血種)による違い:** 犬ほどはっきりしないが、ある程度は言われている。ラグドールは抱っこされても力を抜くおっとりした性格、ブリティッシュ・ショートヘアは落ち着いていて独立心が強い、など。
- **毛柄(雑種)による違い:** 「茶トラは甘えん坊」「三毛は気が強い」などは、日本でよく言われる「あるある」。カリフォルニア大学デービス校の研究(2015年、飼い主1,274人へのアンケート)では、三毛・サビ・白黒・グレー白のメス猫に攻撃的なふるまいが多く、茶トラは少ない傾向が報告された。ただし飼い主の自己申告なので、「三毛は気が強いはず」という思い込みが答えに影響している可能性があり、**毛色が性格を決めるという証拠ではない**([ナショナル ジオグラフィック](https://natgeo.nikkeibp.co.jp/atcl/news/25/073100424/)、[カラパイア](https://karapaia.com/archives/52205861.html))。
- **絵への生かし方:**
  - 毛柄の性格は「よく言われるあるある」として笑いに使う。出品文では「〜と言われる」と書き、事実のようには書かない。
  - 猫全般に共通するしぐさ(狭い所に入る、ごめん寝、夜中の運動会、香箱座り)は、毛柄に関係なく飼い主なら誰でも知っているので、どの毛柄に割り当ててもよい。

---

## 進捗
- 犬: メジャー13種・レア8種の指示文がそろった
- 猫: 10種の指示文がそろった。キジトラ(透けとしっぽを修正)と三毛は生成できたことを確認済み
- 次の作業:
  1. Canvaでぽち袋の展開図(切り線・折り線)を作り、絵を配置する
  2. 文字(ありがとう/おめでとう/おとしだま など)の入れ方を決める
  3. データ版の中身(PDF・PNG・作り方の説明)をまとめ、ZIPにする
  4. 出品文(STEP5)と価格を決める

---

## 文字の入れ方(決定: 基本は「のし」だけ)

### ユーザーの判断
- 日本のぽち袋によくある「のし」(わらびのし)を右上に入れる。
- 「お年玉」「お礼」などの文字を入れると、使える場面が限られるため。
- 文字は選べる形にしてもよい。

### 評価: 賛成
- のしは、お年玉・お礼・お祝い・心付けのどれにも使えるので、1枚で一年中使える。
- 右上に置くのは、のしの正式な位置と同じ。
- **注意(説明文に書く):** のしはお祝いごとの印なので、お見舞いやお悔やみには使わない。

### 文字を選べるようにする方法
- **データ版:** minneのダウンロード販売は1商品に1ファイル(ZIP)なので、選択肢を作るより、**ZIPの中に文字違いを全部入れる**ほうが簡単で、買う人にもうれしい。
  - のしだけ(基本)
  - おとしだま / ありがとう / おめでとう / こころばかり
  - 何も入れない版(のしも文字もなし。手書きしたい人向け)
- **文字の置き方:** のしは右上のまま。文字は袋の上部中央に、縦書きか横書きの小さな文字で置く(絵のじゃまをしない大きさ)。
- **印刷版(羽車で100枚刷るとき):** 1絵柄100枚なので、**のしだけの版**で刷る。文字違いで刷ると、在庫が文字の種類の数だけ増えるため。

## データ版の中身(決定)
- 1犬種・1猫柄につき1つのZIP。中身は「6ページのぽち袋PDF(のしのみ/おとしだま/ありがとう/おめでとう/こころばかり/のしも文字もなし)」と「作り方とご利用について.pdf」。
- 詳しい作り方は `templates/pochi/README.md`。説明書のPDFは `templates/pochi/pochi_howto.pdf`。

---

## 小動物(レアな子)も扱うか

### ユーザーの状況
- 犬のほかに、モルモット、カメ、アフリカヤマネ、ハムスターなどを飼っている。
- レアな子のグッズが少ないと感じている(本人の実感。まだminneの数字では確かめていない)。

### 判断: 犬猫に限らない。ただし主力は犬猫のまま、小動物は「強みの枠」として足す
- **犬猫が主力である理由:** 犬と猫を合わせて約1,570万頭(ペットフード協会 2025年)。買う人の数はここがいちばん多い。小動物の飼育数は今回の検索では信頼できる数字が見つからなかったが、犬猫よりずっと少ないと考えられる(推定)。
- **小動物を足す理由:**
  1. **需要に対して出品が少ない場所を狙う**という最初の方針にそのまま合う(出品が少ないかはminneで確かめる)。
  2. **ユーザー自身が飼っているので、本物の「あるある」が描ける。** この商品の価値は「わかってる」感なので、飼い主本人の目は、ほかの作家がまねしにくい強み。AIが描いた小動物の体つきが正しいかも、本人なら見分けられる。
  3. データ版なら、1種類増やす費用は絵を1枚作る手間だけ。売れなくても損がほとんどない。
  4. 珍しい動物ほど、飼い主は「アフリカヤマネ グッズ」のように名前でまっすぐ探す。出品が少なければ、検索で上に出やすい。
- **ショップ名「うちの子あるある」は、小動物にもそのまま合う。**

### 注意
- 「レアな子のグッズがない」は、今のところユーザー1人の実感。出品前にminneで確かめる:
  - 「モルモット」「ハムスター」「カメ」「アフリカヤマネ」(比べるために「うさぎ」「インコ」も)で検索し、それぞれの出品数と、上位作品のお気に入り数・レビュー件数を記録する。
  - 出品が少なく、それでもお気に入りが付いている動物から作る。
- 小動物は、犬猫の共通指示文(犬向けの言葉が入っている)では形が崩れやすい。種類ごとに、その動物の体つきを書いた共通指示文を用意する。

### ユーザーのminne調査(小動物・鳥)
| 検索語 | 件数 | 出品の中身(ユーザーの観察) |
|---|---|---|
| うさぎ | 104,226 | ありとあらゆる物にうさぎの模様。飽和 |
| インコ | 21,024 | うさぎと同様。放鳥時の遊具も多い |
| ハムスター | 12,240 | 種類が少ない(羊毛フェルトのマスコット、うちの子そっくりのフィギュア)。お気に入りも少ない |
| カメ | 9,231 | レジン封入が多い。マスコット、キーホルダー |
| モルモット | 1,602 | ハウス・ベッド(飼育用品)、羊毛フェルトのぬいぐるみ・マスコットが主 |
| キンカチョウ | 1,137 | マスコット、ステッカー、キーホルダー、ピンバッジ、スマホケース・キーケースへの模様の印刷など、紙や印刷の品が多い |
| アフリカヤマネ | 107 | とても少ない。ステッカー、ハウスに掛ける名札 |

### 読み取れること
- **件数には関係ない作品が混ざる:** 検索は説明文の言葉にも引っかかる。とくに「カメ」は「カメラ」にも当たるので、実際より多く出ている可能性が高い(「亀」でも確かめる)。
- **モルモット:** 出品は少なく、しかも飼育用品と手作りマスコットが中心で、**印刷物(紙もの、ステッカーなど)がほとんど無い**。印刷で作る商品の空きがいちばん大きい。ユーザーが飼っているので「あるある」も本物が描ける。→ **小動物の1番目にする。**
- **キンカチョウ:** 件数はモルモットより少ないのに、ステッカーやピンバッジ、印刷した小物がたくさん出ている。これは「キンカチョウの飼い主は印刷物を買う」という証拠。ただし、そのぶん印刷物の競争はすでにある。→ **2番目の候補。** ユーザーが飼っているので強みも使える。
- **ハムスター:** 件数は多いが、種類が偏っていてお気に入りも少ない。需要が弱い可能性があるので後回し。
- **アフリカヤマネ:** 空きは最大だが、買う人も極めて少ない。データ版なら損はないので、余力があれば作る。
- **まだ足りない証拠:** モルモットの上位作品のお気に入り数(数字)。出品後の反応で確かめる。

---

## モルモット(小動物の1番目)

### 共通指示文(モルモット用)
犬猫と同じ画風のまま、モルモットの体つきを書き足した。`[SCENE LINE]` を下の表の一文に差し替えて使う。

```
Create an original, warm and humorous illustration of a single guinea pig for a Japanese gift envelope (pochi-bukuro).

SUBJECT: [SCENE LINE]
The humor must feel affectionate and true to life, the kind of moment real guinea pig owners instantly recognize. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THIS IS A GUINEA PIG, NOT A HAMSTER, RABBIT OR MOUSE: a plump, loaf-shaped body that is wider than tall, NO visible tail at all, a big rounded blunt nose (Roman nose) with no pointed snout, small droopy petal-shaped ears on the sides of the head, round eyes set on the sides of the face, and tiny short legs mostly hidden under the body. No neck: the head flows straight into the body.

THE NOSE AND MOUTH ARE THE MOST IMPORTANT FEATURES (guinea pig fans love them, so they must be true to real anatomy):
- The whole muzzle is a big, soft, puffy rounded bulge, wide like a small bun, filling the lower center of the face. It is wider than the space between the eyes.
- The nose sits on the upper part of this bulge: a small pale pink area with two tiny comma-shaped slit nostrils, angled like an upside-down V.
- A short thin vertical line runs down from between the nostrils to the upper lip, which is split into two small rounded puffy lobes, one on each side of the line.
- Under the lobes, the mouth is a short, gently curved horizontal line with a small, soft, slightly pouting rounded lower lip below it. The mouth sits at the very bottom of the muzzle, close to the chin.
- NOT a cat face: no tiny triangle nose, no "ω" cat mouth, no rabbit "Y" mouth. Mouth almost closed: no wide-open mouth, no teeth, no tongue.

STYLE: Cute, simplified cartoon illustration with deformed (chibi-like) proportions: a big round head, a small soft body, short stubby legs, and simple dot or small oval eyes. Keep only the few features that make the animal instantly recognizable (body shape, ear shape, coat color and patches, coat texture) and exaggerate them slightly. Clean, smooth outlines in a soft dark brown, flat colors with gentle shading, warm and friendly palette. Simple shapes that stay readable when printed small (about 5 cm tall).

COMPOSITION: One guinea pig only, centered, filling about 70% of the canvas width, with generous empty space around it. Plain pure white background, no floor, no shadow except a very light one under the animal, no props unless described above.

TEXT: No text, letters, numbers, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```

※口元がモルモットのいちばんの可愛さ(ユーザーの指摘)。線だけで描かせると猫やうさぎの口になる。**鼻から口までが、ふっくら丸く盛り上がった大きなふくらみ**であることを必ず描かせる。
※横向きだと口元が隠れる。**口元を見せる絵は正面向き**にする。
※言葉だけで形が合わないときは、ユーザー自身のモルモットの写真を参考画像としてGeminiに渡す(自分の子の写真なので権利の問題はない)。まず正面の「顔の基準の絵」を1枚作り、以降の場面はその絵を参考画像にして顔をそろえる。

※犬猫は「画面の高さの70%」だが、モルモットは横長なので「幅の70%」にしている。

### あるある候補(仮。ユーザーの実体験で差し替える)
| あるある | [SCENE LINE] に入れる一文 |
|---|---|
| 野菜の袋の音でぷいーぷいー鳴く(口はほとんど開けない) | A short-haired guinea pig with tortoiseshell-and-white patches (orange, black and white), standing up on its hind legs with its head tilted slightly up, squeaking for food with its mouth almost closed (the lips only very slightly parted), a few small curved "sound lines" near its face, eyes shining with excitement. |
| ポップコーンジャンプ | A short-haired cream-and-white guinea pig in the middle of a happy "popcorning" jump: all four tiny feet off the ground, body twisted slightly in mid-air, eyes closed with joy, a few small motion lines under it. |
| 牧草をくわえたまま固まる | An Abyssinian guinea pig with messy swirled rosettes in its brown-and-white coat, frozen still with a long strand of hay sticking out of its mouth, staring straight ahead with a blank, serious face. |
| 袋から顔だけ出す | A long-haired (Peruvian-style) guinea pig with flowing silky hair, only its head and front paws poking out from the opening of an opaque paper envelope, hair spilling over the edge, looking out cautiously. The rest of the body is hidden inside the envelope. |

### 毛色・毛の種類の候補
- 短毛の三毛(オレンジ・黒・白)、クリーム×白、ヒマラヤン(白い体に黒い鼻と耳)
- アビシニアン(つむじがたくさんある)、長毛(ペルビアンやシェルティ)、テディ(もこもこ)
- **ユーザーの子の毛色を1枚目にする**のがいちばん強い(本人が「似ている」と判断できるため)。
