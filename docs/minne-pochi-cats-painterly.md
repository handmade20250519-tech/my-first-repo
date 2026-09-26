# 猫のぽち袋 指示文(絵画風・確定版)

犬と同じ画風(**水墨淡彩+少し漫画っぽく**)。各猫の見出しの下の文を、そのまま全部コピーしてGeminiに貼る。

## 犬の版との違い
- **汗が出た対策(2回目):** 「汗を描かない」と書いても、茶トラに汗が出た(ユーザー確認)。「汗」という言葉自体がAIに汗を思い出させている可能性があるので、「汗」という言葉を消した。代わりに「漫画の記号はSUBJECTに書いたものだけ。顔・頭・頭のまわりには何も描かない」と書いた
- 犬と同じく、絵の下に英語の名前を筆文字で小さく入れる(毛柄は Orange Tabby、Brown Tabby、Calico、Black Cat、Tuxedo Cat、Silver Tabby)。生成後につづりを必ず確かめる
- 画風の段落の前に、猫らしさを必ず描かせる段落(THIS IS A CAT, NOT A DOG)を入れている
- **汗のしずくを描かない**指示を入れた(犬の絵でほとんどの顔に汗が付いたため。ユーザーの指摘)。漫画の記号は、動きの線ときらりだけ
- キジトラは、目が猫らしく見えなかった(ユーザーの指摘)ので、猫の目の形(アーモンド形、緑の瞳、縦に細い瞳孔、細い墨のアイライン)をはっきり書いた → **うまくいった(ユーザー確認)**。ほかの猫で目が猫らしくないときも、同じ目の指定を足す
- キジトラは、しっぽを袋の中に隠すので、猫らしさの段落から「長いしっぽ」を外してある
- スコティッシュ・フォールドは、耳を折れた形にする例外を一文の中に書いてある
- 前の画風の言葉を外した: 小道具の「平らな色」→「淡い水彩の色」、黒猫の「輪郭と灰色のハイライト」→「墨の輪郭と灰色の淡い塗り」、ブリティッシュ・ショートヘアとサバトラの「大きな目」→「丸い目」

## 共通指示文(ひな形)
新しい種類を足すときは、[BREED LINE] に場面の一文、[NAME] に英語の名前(2か所)を入れる。
```
Create an original, warm and gently humorous painting of a single cat for a Japanese gift envelope (pochi-bukuro).

SUBJECT: [BREED LINE]
The humor must feel affectionate and true to life, the kind of moment real cat owners instantly recognize. Even in this painterly style, the coat pattern or breed must be clear at a glance. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THIS IS A CAT, NOT A DOG: always include clear cat features: small triangular pointed ears on top of the head, a tiny pink triangle nose right between the eyes with no protruding snout or muzzle, three thin whiskers on each cheek, a small cat mouth shaped like a soft "ω", a long flexible tail, and small round paws. Flat, round cat face.

STYLE: A charming, slightly comic Japanese-style painting that mixes traditional ink-and-light-color painting with a playful manga feel, as if brush-painted on washi paper. Confident sumi ink outlines, a little bolder than a formal painting, with natural brush variation in thickness; soft, transparent watercolor washes with gentle bleeding edges; fur suggested with a few light brush strokes. Muted, natural, traditional Japanese colors. More deformed, cute proportions: the head about one third of the body height, a round soft body, short stubby legs. Clear, simple, expressive face with a comical expression (for example proudly closed eyes, a faint pink blush on the cheeks). Do not add any extra manga symbols or marks: the only marks allowed are the ones described in SUBJECT. Keep the face, the head and the space around the head completely clean, with nothing drawn near them. NOT a glossy digital anime look: no flat cel shading, no uniform digital outlines, no big shiny anime eyes. Keep the painting simple and readable when printed small (about 5 cm tall).

COMPOSITION: One cat only, centered, filling about 70% of the canvas height, with generous empty space around it. Plain pure white background with no paper texture, no frame, no floor; only a very faint pale ink wash shadow under the cat. No props unless described above.

TEXT: Write only the name "[NAME]" once, in small, simple, neat hand-lettered brush letters in soft dark sumi ink, centered just below the cat, about 6% of the canvas height, on a single line. Spell it exactly: [NAME]. No other text, letters, numbers, seals, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```

## 茶トラ
あるある: 人なつこくて食いしん坊と言われる。ごはんの時間が近づくと、空の器の前に座り、前足で器のふちをちょんと押さえて、無言の圧をかける

```
Create an original, warm and gently humorous painting of a single cat for a Japanese gift envelope (pochi-bukuro).

SUBJECT: An orange tabby cat sitting perfectly upright in front of an empty food bowl, one front paw placed firmly on the rim of the bowl, staring straight at the viewer with a silent, heavy, expectant "it is time" look: eyes half-lidded and unblinking, mouth closed in a flat line. The humor is its calm, patient pressure. Round cheeks, slightly plump, friendly body. Classic orange tabby features: warm orange coat with darker orange stripes, an M-shape on the forehead, striped cheeks and legs, ringed tail, cream-white chin and chest. The bowl is a plain, soft watercolor color and clearly empty.
The humor must feel affectionate and true to life, the kind of moment real cat owners instantly recognize. Even in this painterly style, the coat pattern or breed must be clear at a glance. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THIS IS A CAT, NOT A DOG: always include clear cat features: small triangular pointed ears on top of the head, a tiny pink triangle nose right between the eyes with no protruding snout or muzzle, three thin whiskers on each cheek, a small cat mouth shaped like a soft "ω", a long flexible tail, and small round paws. Flat, round cat face.

STYLE: A charming, slightly comic Japanese-style painting that mixes traditional ink-and-light-color painting with a playful manga feel, as if brush-painted on washi paper. Confident sumi ink outlines, a little bolder than a formal painting, with natural brush variation in thickness; soft, transparent watercolor washes with gentle bleeding edges; fur suggested with a few light brush strokes. Muted, natural, traditional Japanese colors. More deformed, cute proportions: the head about one third of the body height, a round soft body, short stubby legs. Clear, simple, expressive face with a comical expression (for example proudly closed eyes, a faint pink blush on the cheeks). Do not add any extra manga symbols or marks: the only marks allowed are the ones described in SUBJECT. Keep the face, the head and the space around the head completely clean, with nothing drawn near them. NOT a glossy digital anime look: no flat cel shading, no uniform digital outlines, no big shiny anime eyes. Keep the painting simple and readable when printed small (about 5 cm tall).

COMPOSITION: One cat only, centered, filling about 70% of the canvas height, with generous empty space around it. Plain pure white background with no paper texture, no frame, no floor; only a very faint pale ink wash shadow under the cat. No props unless described above.

TEXT: Write only the name "Orange Tabby" once, in small, simple, neat hand-lettered brush letters in soft dark sumi ink, centered just below the cat, about 6% of the canvas height, on a single line. Spell it exactly: Orange Tabby. No other text, letters, numbers, seals, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```

## キジトラ
あるある: 「入れそうな所には入る」。小さすぎるぽち袋にも無理やり入り、顔だけ出して満足げ

```
Create an original, warm and gently humorous painting of a single cat for a Japanese gift envelope (pochi-bukuro).

SUBJECT: A brown mackerel tabby cat that has squeezed its whole body into a small paper envelope that is clearly far too small. The envelope lies on its side with the open end facing the viewer. Only the cat's head and two front paws poke out of the opening; the rest of its body AND its tail are completely hidden inside the envelope. The far end of the envelope is closed and smooth: NO tail, NO back legs and NO fur stick out anywhere around the envelope. The envelope is made of thick, fully opaque paper: the cat's body, legs, stripes and tail must NOT show through it at all, with no see-through effect and no body outline drawn on the paper. The only sign of the cat inside is that the envelope bulges into a tight, round, overstuffed shape. It looks completely satisfied, as if the envelope was made for it. CAT EYES (important): real cat eyes, not dog or human eyes: almond-shaped eyes that are wider than tall and tilt slightly upward at the outer corners, with yellow-green irises, narrow vertical slit pupils, and a thin dark sumi line around each eye like natural eyeliner. The eyes are narrowed in a relaxed, contented cat "slow blink": the upper lids come halfway down in a soft straight line, but the green iris and slit pupil are still clearly visible. No round dot eyes, no closed curved-line eyes, no eyebrows, no human-like eyelashes. Classic brown tabby features (visible on the head and paws only): warm brown-gray coat with dark mackerel stripes, an M-shape on the forehead. The envelope is a plain, soft watercolor color with no writing and no pattern.
The humor must feel affectionate and true to life, the kind of moment real cat owners instantly recognize. Even in this painterly style, the coat pattern or breed must be clear at a glance. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THIS IS A CAT, NOT A DOG: always include clear cat features: small triangular pointed ears on top of the head, a tiny pink triangle nose right between the eyes with no protruding snout or muzzle, three thin whiskers on each cheek, a small cat mouth shaped like a soft "ω", and small round paws (the tail stays hidden inside the envelope). Flat, round cat face.

STYLE: A charming, slightly comic Japanese-style painting that mixes traditional ink-and-light-color painting with a playful manga feel, as if brush-painted on washi paper. Confident sumi ink outlines, a little bolder than a formal painting, with natural brush variation in thickness; soft, transparent watercolor washes with gentle bleeding edges; fur suggested with a few light brush strokes. Muted, natural, traditional Japanese colors. More deformed, cute proportions: the head about one third of the body height, a round soft body, short stubby legs. Clear, simple, expressive face with a comical expression (for example proudly closed eyes, a faint pink blush on the cheeks). Do not add any extra manga symbols or marks: the only marks allowed are the ones described in SUBJECT. Keep the face, the head and the space around the head completely clean, with nothing drawn near them. NOT a glossy digital anime look: no flat cel shading, no uniform digital outlines, no big shiny anime eyes. Keep the painting simple and readable when printed small (about 5 cm tall).

COMPOSITION: One cat only, centered, filling about 70% of the canvas height, with generous empty space around it. Plain pure white background with no paper texture, no frame, no floor; only a very faint pale ink wash shadow under the cat. No props unless described above.

TEXT: Write only the name "Brown Tabby" once, in small, simple, neat hand-lettered brush letters in soft dark sumi ink, centered just below the cat, about 6% of the canvas height, on a single line. Spell it exactly: Brown Tabby. No other text, letters, numbers, seals, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```

## 三毛
あるある: 気が強くてマイペース。香箱座りでくつろいでいるが、撫でようとすると横目で「今はだめ」

```
Create an original, warm and gently humorous painting of a single cat for a Japanese gift envelope (pochi-bukuro).

SUBJECT: A calico cat sitting in a neat "loaf" pose with all paws tucked under, looking relaxed, but giving a sharp sideways glance toward the viewer with one eyebrow raised, the tip of its tail flicking (the cat has exactly ONE tail: it wraps neatly around the side of the loaf-shaped body toward the front paws, lying on the floor, and only its very tip is lifted and flicking, shown with two small motion lines; nothing rises from behind its back), clearly saying "not now." Classic calico features: white base coat with distinct patches of orange and black, especially on the head, back and tail.
The humor must feel affectionate and true to life, the kind of moment real cat owners instantly recognize. Even in this painterly style, the coat pattern or breed must be clear at a glance. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THIS IS A CAT, NOT A DOG: always include clear cat features: small triangular pointed ears on top of the head, a tiny pink triangle nose right between the eyes with no protruding snout or muzzle, three thin whiskers on each cheek, a small cat mouth shaped like a soft "ω", a long flexible tail, and small round paws. Flat, round cat face.

STYLE: A charming, slightly comic Japanese-style painting that mixes traditional ink-and-light-color painting with a playful manga feel, as if brush-painted on washi paper. Confident sumi ink outlines, a little bolder than a formal painting, with natural brush variation in thickness; soft, transparent watercolor washes with gentle bleeding edges; fur suggested with a few light brush strokes. Muted, natural, traditional Japanese colors. More deformed, cute proportions: the head about one third of the body height, a round soft body, short stubby legs. Clear, simple, expressive face with a comical expression (for example proudly closed eyes, a faint pink blush on the cheeks). Do not add any extra manga symbols or marks: the only marks allowed are the ones described in SUBJECT. Keep the face, the head and the space around the head completely clean, with nothing drawn near them. NOT a glossy digital anime look: no flat cel shading, no uniform digital outlines, no big shiny anime eyes. Keep the painting simple and readable when printed small (about 5 cm tall).

COMPOSITION: One cat only, centered, filling about 70% of the canvas height, with generous empty space around it. Plain pure white background with no paper texture, no frame, no floor; only a very faint pale ink wash shadow under the cat. No props unless described above.

TEXT: Write only the name "Calico" once, in small, simple, neat hand-lettered brush letters in soft dark sumi ink, centered just below the cat, about 6% of the canvas height, on a single line. Spell it exactly: Calico. No other text, letters, numbers, seals, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```

## 黒猫
あるある: 丸まって寝ていると、真っ黒でどこが顔か分からない。おやつの袋の音がした瞬間、耳がぴんと立ち、金色の目だけがぱっちり開く

```
Create an original, warm and gently humorous painting of a single cat for a Japanese gift envelope (pochi-bukuro).

SUBJECT: A black cat curled up asleep in a round "ammonite" curl, lying on its side with its long tail wrapped all the way around its body and the tip resting over its nose, front paws tucked in. Its head is still resting on its curled body, but both ears have just shot straight up and turned forward, and its two round golden eyes have popped wide open, as if it has just heard the treat bag rustle. The body stays still and sleepy while only the ears and eyes are wide awake. The cat shape must stay clearly readable: the triangular ears, the round face, the wrapped tail and the tucked paws are each clearly separated by the sumi ink outline and by soft charcoal-gray watercolor highlights on the black coat. White whiskers stand out against the black face. Classic black cat features: glossy solid black coat (painted in deep charcoal ink with lighter gray washes for highlights), golden-yellow eyes.
The humor must feel affectionate and true to life, the kind of moment real cat owners instantly recognize. Even in this painterly style, the coat pattern or breed must be clear at a glance. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THIS IS A CAT, NOT A DOG: always include clear cat features: small triangular pointed ears on top of the head, a tiny pink triangle nose right between the eyes with no protruding snout or muzzle, three thin whiskers on each cheek, a small cat mouth shaped like a soft "ω", a long flexible tail, and small round paws. Flat, round cat face.

STYLE: A charming, slightly comic Japanese-style painting that mixes traditional ink-and-light-color painting with a playful manga feel, as if brush-painted on washi paper. Confident sumi ink outlines, a little bolder than a formal painting, with natural brush variation in thickness; soft, transparent watercolor washes with gentle bleeding edges; fur suggested with a few light brush strokes. Muted, natural, traditional Japanese colors. More deformed, cute proportions: the head about one third of the body height, a round soft body, short stubby legs. Clear, simple, expressive face with a comical expression (for example proudly closed eyes, a faint pink blush on the cheeks). Do not add any extra manga symbols or marks: the only marks allowed are the ones described in SUBJECT. Keep the face, the head and the space around the head completely clean, with nothing drawn near them. NOT a glossy digital anime look: no flat cel shading, no uniform digital outlines, no big shiny anime eyes. Keep the painting simple and readable when printed small (about 5 cm tall).

COMPOSITION: One cat only, centered, filling about 70% of the canvas height, with generous empty space around it. Plain pure white background with no paper texture, no frame, no floor; only a very faint pale ink wash shadow under the cat. No props unless described above.

TEXT: Write only the name "Black Cat" once, in small, simple, neat hand-lettered brush letters in soft dark sumi ink, centered just below the cat, about 6% of the canvas height, on a single line. Spell it exactly: Black Cat. No other text, letters, numbers, seals, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```

## ハチワレ
あるある: 顔を床にうずめて眠る「ごめん寝」。まるで深々と謝っているように見える

```
Create an original, warm and gently humorous painting of a single cat for a Japanese gift envelope (pochi-bukuro).

SUBJECT: A black-and-white tuxedo cat asleep in the famous "apology sleep" (gomen-ne) pose, seen from the front: it is crouched low with its round back curved up, and its face is pressed down into the floor between its two white front paws, as if bowing deeply to say sorry. Its forehead faces the viewer, so the black cap with the white upside-down V "hachiware" split running down between the eyes is clearly visible, along with the tips of its white whiskers peeking out on both sides. Both black triangular ears stick up on top, and its long black tail curls around beside its body. It looks completely peaceful and a little comical. Classic tuxedo cat features: black back, head and ears, white chest, white paws, and a symmetrical white "hachiware" split on the face.
The humor must feel affectionate and true to life, the kind of moment real cat owners instantly recognize. Even in this painterly style, the coat pattern or breed must be clear at a glance. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THIS IS A CAT, NOT A DOG: always include clear cat features: small triangular pointed ears on top of the head, a tiny pink triangle nose right between the eyes with no protruding snout or muzzle, three thin whiskers on each cheek, a small cat mouth shaped like a soft "ω", a long flexible tail, and small round paws. Flat, round cat face.

STYLE: A charming, slightly comic Japanese-style painting that mixes traditional ink-and-light-color painting with a playful manga feel, as if brush-painted on washi paper. Confident sumi ink outlines, a little bolder than a formal painting, with natural brush variation in thickness; soft, transparent watercolor washes with gentle bleeding edges; fur suggested with a few light brush strokes. Muted, natural, traditional Japanese colors. More deformed, cute proportions: the head about one third of the body height, a round soft body, short stubby legs. Clear, simple, expressive face with a comical expression (for example proudly closed eyes, a faint pink blush on the cheeks). Do not add any extra manga symbols or marks: the only marks allowed are the ones described in SUBJECT. Keep the face, the head and the space around the head completely clean, with nothing drawn near them. NOT a glossy digital anime look: no flat cel shading, no uniform digital outlines, no big shiny anime eyes. Keep the painting simple and readable when printed small (about 5 cm tall).

COMPOSITION: One cat only, centered, filling about 70% of the canvas height, with generous empty space around it. Plain pure white background with no paper texture, no frame, no floor; only a very faint pale ink wash shadow under the cat. No props unless described above.

TEXT: Write only the name "Tuxedo Cat" once, in small, simple, neat hand-lettered brush letters in soft dark sumi ink, centered just below the cat, about 6% of the canvas height, on a single line. Spell it exactly: Tuxedo Cat. No other text, letters, numbers, seals, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```

## サバトラ
あるある: 昼間はおとなしいのに、夜中になると突然走り回る「夜中の運動会」

```
Create an original, warm and gently humorous painting of a single cat for a Japanese gift envelope (pochi-bukuro).

SUBJECT: A silver mackerel tabby cat in the middle of a sudden midnight zoomies sprint, seen from the side and running toward the right: all four legs stretched out mid-gallop, back arched, ears pressed flat but still clearly triangular, tail puffed up like a bottle brush. Its head is turned toward the viewer, with round wild eyes and a small open "ω" mouth, clearly having no reason at all to be running. A few simple brush-drawn speed lines behind it show how fast it is going, and one small pale crescent moon in the upper corner hints that it is the middle of the night. Classic silver tabby features: pale silver-gray coat with crisp dark gray mackerel stripes, an M-shape on the forehead, ringed tail.
The humor must feel affectionate and true to life, the kind of moment real cat owners instantly recognize. Even in this painterly style, the coat pattern or breed must be clear at a glance. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THIS IS A CAT, NOT A DOG: always include clear cat features: small triangular pointed ears on top of the head, a tiny pink triangle nose right between the eyes with no protruding snout or muzzle, three thin whiskers on each cheek, a small cat mouth shaped like a soft "ω", a long flexible tail, and small round paws. Flat, round cat face.

STYLE: A charming, slightly comic Japanese-style painting that mixes traditional ink-and-light-color painting with a playful manga feel, as if brush-painted on washi paper. Confident sumi ink outlines, a little bolder than a formal painting, with natural brush variation in thickness; soft, transparent watercolor washes with gentle bleeding edges; fur suggested with a few light brush strokes. Muted, natural, traditional Japanese colors. More deformed, cute proportions: the head about one third of the body height, a round soft body, short stubby legs. Clear, simple, expressive face with a comical expression (for example proudly closed eyes, a faint pink blush on the cheeks). Do not add any extra manga symbols or marks: the only marks allowed are the ones described in SUBJECT. Keep the face, the head and the space around the head completely clean, with nothing drawn near them. NOT a glossy digital anime look: no flat cel shading, no uniform digital outlines, no big shiny anime eyes. Keep the painting simple and readable when printed small (about 5 cm tall).

COMPOSITION: One cat only, centered, filling about 70% of the canvas height, with generous empty space around it. Plain pure white background with no paper texture, no frame, no floor; only a very faint pale ink wash shadow under the cat. No props unless described above.

TEXT: Write only the name "Silver Tabby" once, in small, simple, neat hand-lettered brush letters in soft dark sumi ink, centered just below the cat, about 6% of the canvas height, on a single line. Spell it exactly: Silver Tabby. No other text, letters, numbers, seals, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```

## スコティッシュ・フォールド
あるある: 足を前に投げ出し、人間のおじさんのように座る「スコ座り」で、くつろぎきった顔

```
Create an original, warm and gently humorous painting of a single cat for a Japanese gift envelope (pochi-bukuro).

SUBJECT: A scottish fold cat sitting upright on its bottom like a small person relaxing on the floor, back legs stretched straight out in front, round belly showing, front paws resting on its belly, with a calm, completely relaxed, slightly sleepy half-closed-eye face, like an old man after a big meal. EXCEPTION TO THE EAR RULE BELOW: for this breed only, the ears are NOT upright; they are small and folded forward and down, lying flat against the very round head like a little cap, so the head looks almost perfectly round. Classic scottish fold features: very round head with folded-down ears, round eyes, round cheeks, plush dense coat. Coat color: soft gray-blue.
The humor must feel affectionate and true to life, the kind of moment real cat owners instantly recognize. Even in this painterly style, the coat pattern or breed must be clear at a glance. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THIS IS A CAT, NOT A DOG: always include clear cat features: small triangular pointed ears on top of the head, a tiny pink triangle nose right between the eyes with no protruding snout or muzzle, three thin whiskers on each cheek, a small cat mouth shaped like a soft "ω", a long flexible tail, and small round paws. Flat, round cat face.

STYLE: A charming, slightly comic Japanese-style painting that mixes traditional ink-and-light-color painting with a playful manga feel, as if brush-painted on washi paper. Confident sumi ink outlines, a little bolder than a formal painting, with natural brush variation in thickness; soft, transparent watercolor washes with gentle bleeding edges; fur suggested with a few light brush strokes. Muted, natural, traditional Japanese colors. More deformed, cute proportions: the head about one third of the body height, a round soft body, short stubby legs. Clear, simple, expressive face with a comical expression (for example proudly closed eyes, a faint pink blush on the cheeks). Do not add any extra manga symbols or marks: the only marks allowed are the ones described in SUBJECT. Keep the face, the head and the space around the head completely clean, with nothing drawn near them. NOT a glossy digital anime look: no flat cel shading, no uniform digital outlines, no big shiny anime eyes. Keep the painting simple and readable when printed small (about 5 cm tall).

COMPOSITION: One cat only, centered, filling about 70% of the canvas height, with generous empty space around it. Plain pure white background with no paper texture, no frame, no floor; only a very faint pale ink wash shadow under the cat. No props unless described above.

TEXT: Write only the name "Scottish Fold" once, in small, simple, neat hand-lettered brush letters in soft dark sumi ink, centered just below the cat, about 6% of the canvas height, on a single line. Spell it exactly: Scottish Fold. No other text, letters, numbers, seals, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```

## マンチカン
あるある: 好奇心旺盛。気になる物音がすると、短い後ろ足だけでミーアキャットのように立ち上がって見回す。立っても背はほとんど高くならない

```
Create an original, warm and gently humorous painting of a single cat for a Japanese gift envelope (pochi-bukuro).

SUBJECT: A munchkin cat standing up on its very short hind legs like a meerkat to see what that sound was, body stretched as tall as it can go, tiny front legs dangling in front of its chest, ears perked forward, eyes wide and curious, with a serious, slightly comical face. Even standing at full height it is still only a little taller than when sitting. For this breed only, make the contrast clear: a normal-length body on noticeably extra-short legs, much shorter than in the usual cute style. Classic munchkin features: extra-short legs, normal-length body, round face, upright triangular ears, long tail used for balance. Coat color: cream with light brown tabby stripes.
The humor must feel affectionate and true to life, the kind of moment real cat owners instantly recognize. Even in this painterly style, the coat pattern or breed must be clear at a glance. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THIS IS A CAT, NOT A DOG: always include clear cat features: small triangular pointed ears on top of the head, a tiny pink triangle nose right between the eyes with no protruding snout or muzzle, three thin whiskers on each cheek, a small cat mouth shaped like a soft "ω", a long flexible tail, and small round paws. Flat, round cat face.

STYLE: A charming, slightly comic Japanese-style painting that mixes traditional ink-and-light-color painting with a playful manga feel, as if brush-painted on washi paper. Confident sumi ink outlines, a little bolder than a formal painting, with natural brush variation in thickness; soft, transparent watercolor washes with gentle bleeding edges; fur suggested with a few light brush strokes. Muted, natural, traditional Japanese colors. More deformed, cute proportions: the head about one third of the body height, a round soft body, short stubby legs. Clear, simple, expressive face with a comical expression (for example proudly closed eyes, a faint pink blush on the cheeks). Do not add any extra manga symbols or marks: the only marks allowed are the ones described in SUBJECT. Keep the face, the head and the space around the head completely clean, with nothing drawn near them. NOT a glossy digital anime look: no flat cel shading, no uniform digital outlines, no big shiny anime eyes. Keep the painting simple and readable when printed small (about 5 cm tall).

COMPOSITION: One cat only, centered, filling about 70% of the canvas height, with generous empty space around it. Plain pure white background with no paper texture, no frame, no floor; only a very faint pale ink wash shadow under the cat. No props unless described above.

TEXT: Write only the name "Munchkin" once, in small, simple, neat hand-lettered brush letters in soft dark sumi ink, centered just below the cat, about 6% of the canvas height, on a single line. Spell it exactly: Munchkin. No other text, letters, numbers, seals, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```

## ラグドール
あるある: 名前は「ぬいぐるみ」の意味。抱っこされると力が抜けて、ぐにゃりと伸びる。どこに置かれても、そのままとろけている

```
Create an original, warm and gently humorous painting of a single cat for a Japanese gift envelope (pochi-bukuro).

SUBJECT: A ragdoll cat draped completely limp over a small round cushion like a soft towel hung to dry: its front half hangs down the left side with front legs dangling, and its back half and fluffy tail hang down the right side. Its head hangs down but is turned toward the viewer, face upside-down-relaxed and blissful, eyes half open so the bright blue color still shows, a tiny contented "ω" mouth. Its whole body looks boneless and melted, as if it would stay like that forever. Classic ragdoll features: large fluffy body, semi-long silky coat, bright blue eyes, colorpoint pattern: creamy white body with darker seal-brown ears, face mask, legs and tail. The cushion is a plain, soft watercolor color.
The humor must feel affectionate and true to life, the kind of moment real cat owners instantly recognize. Even in this painterly style, the coat pattern or breed must be clear at a glance. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THIS IS A CAT, NOT A DOG: always include clear cat features: small triangular pointed ears on top of the head, a tiny pink triangle nose right between the eyes with no protruding snout or muzzle, three thin whiskers on each cheek, a small cat mouth shaped like a soft "ω", a long flexible tail, and small round paws. Flat, round cat face.

STYLE: A charming, slightly comic Japanese-style painting that mixes traditional ink-and-light-color painting with a playful manga feel, as if brush-painted on washi paper. Confident sumi ink outlines, a little bolder than a formal painting, with natural brush variation in thickness; soft, transparent watercolor washes with gentle bleeding edges; fur suggested with a few light brush strokes. Muted, natural, traditional Japanese colors. More deformed, cute proportions: the head about one third of the body height, a round soft body, short stubby legs. Clear, simple, expressive face with a comical expression (for example proudly closed eyes, a faint pink blush on the cheeks). Do not add any extra manga symbols or marks: the only marks allowed are the ones described in SUBJECT. Keep the face, the head and the space around the head completely clean, with nothing drawn near them. NOT a glossy digital anime look: no flat cel shading, no uniform digital outlines, no big shiny anime eyes. Keep the painting simple and readable when printed small (about 5 cm tall).

COMPOSITION: One cat only, centered, filling about 70% of the canvas height, with generous empty space around it. Plain pure white background with no paper texture, no frame, no floor; only a very faint pale ink wash shadow under the cat. No props unless described above.

TEXT: Write only the name "Ragdoll" once, in small, simple, neat hand-lettered brush letters in soft dark sumi ink, centered just below the cat, about 6% of the canvas height, on a single line. Spell it exactly: Ragdoll. No other text, letters, numbers, seals, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```

## ブリティッシュ・ショートヘア
あるある: 落ち着きすぎている。目の前で猫じゃらしを必死に振られても、目で追いもせず無表情。ぬいぐるみのような「動かないクマ」

```
Create an original, warm and gently humorous painting of a single cat for a Japanese gift envelope (pochi-bukuro).

SUBJECT: A british shorthair cat sitting upright and perfectly still like a plump teddy bear, looking straight ahead with a completely neutral, unimpressed, deadpan expression (DEADPAN FACE: round eyes fully open and staring blankly straight ahead, the mouth a small short straight flat line, NOT smiling, NOT an upturned "ω" smile, no blush on the cheeks), while a small feather toy on a thin string dangles and swings right in front of its nose. The string simply enters from the top edge of the canvas (no person, no hand, no stick visible). A few small motion lines show the feather swinging busily, but the cat's eyes do not follow it at all and not a single whisker moves. Classic british shorthair features: very round face, full chubby cheeks, small rounded ears set wide apart, dense plush coat, stocky round body, short thick legs, thick tail, round copper-orange eyes. Coat color: solid blue-gray.
The humor must feel affectionate and true to life, the kind of moment real cat owners instantly recognize. Even in this painterly style, the coat pattern or breed must be clear at a glance. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THIS IS A CAT, NOT A DOG: always include clear cat features: small triangular pointed ears on top of the head, a tiny pink triangle nose right between the eyes with no protruding snout or muzzle, three thin whiskers on each cheek, a small cat mouth (for this cat, a straight flat line, not smiling), a long flexible tail, and small round paws. Flat, round cat face.

STYLE: A charming, slightly comic Japanese-style painting that mixes traditional ink-and-light-color painting with a playful manga feel, as if brush-painted on washi paper. Confident sumi ink outlines, a little bolder than a formal painting, with natural brush variation in thickness; soft, transparent watercolor washes with gentle bleeding edges; fur suggested with a few light brush strokes. Muted, natural, traditional Japanese colors. More deformed, cute proportions: the head about one third of the body height, a round soft body, short stubby legs. Clear, simple face; for this cat the humor is its completely blank, deadpan expression. Do not add any extra manga symbols or marks: the only marks allowed are the ones described in SUBJECT. Keep the face, the head and the space around the head completely clean, with nothing drawn near them. NOT a glossy digital anime look: no flat cel shading, no uniform digital outlines, no big shiny anime eyes. Keep the painting simple and readable when printed small (about 5 cm tall).

COMPOSITION: One cat only, centered, filling about 70% of the canvas height, with generous empty space around it. Plain pure white background with no paper texture, no frame, no floor; only a very faint pale ink wash shadow under the cat. No props unless described above.

TEXT: Write only the name "British Shorthair" once, in small, simple, neat hand-lettered brush letters in soft dark sumi ink, centered just below the cat, about 6% of the canvas height, on a single line. Spell it exactly: British Shorthair. No other text, letters, numbers, seals, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```

## アメリカン・ショートヘア
あるある: 狩猟の血が騒ぐ。丸めた紙のボールを見つけると、低く伏せてお尻をフリフリ。飛びかかる直前の真剣な顔

```
Create an original, warm and gently humorous painting of a single cat for a Japanese gift envelope (pochi-bukuro).

SUBJECT: An American shorthair cat seen from the side, crouched very low in a hunting pose, facing right toward a small crumpled paper ball on the white background. Front paws and chest pressed to the floor, eyes wide and completely focused on the ball, ears pointed forward. Its round bottom is raised and wiggling from side to side just before pouncing, shown with a few short curved motion lines around the hips; the tail stretches straight back with the tip twitching. Classic American shorthair features: sturdy, muscular body, round face with full cheeks, and a silver classic tabby coat: bold black swirls on a bright silver base, with a large round "bullseye" swirl pattern clearly visible on its side, a black "M" marking on the forehead, black rings on the tail and stripes on the legs.
The humor must feel affectionate and true to life, the kind of moment real cat owners instantly recognize. Even in this painterly style, the coat pattern or breed must be clear at a glance. Original design only: do NOT depict any existing character, mascot or brand, and do NOT imitate any specific artist's style.

THIS IS A CAT, NOT A DOG: always include clear cat features: small triangular pointed ears on top of the head, a tiny pink triangle nose right between the eyes with no protruding snout or muzzle, three thin whiskers on each cheek, a small cat mouth shaped like a soft "ω", a long flexible tail, and small round paws. Flat, round cat face.

STYLE: A charming, slightly comic Japanese-style painting that mixes traditional ink-and-light-color painting with a playful manga feel, as if brush-painted on washi paper. Confident sumi ink outlines, a little bolder than a formal painting, with natural brush variation in thickness; soft, transparent watercolor washes with gentle bleeding edges; fur suggested with a few light brush strokes. Muted, natural, traditional Japanese colors. More deformed, cute proportions: the head about one third of the body height, a round soft body, short stubby legs. Clear, simple, expressive face with a comical expression (for example proudly closed eyes, a faint pink blush on the cheeks). Do not add any extra manga symbols or marks: the only marks allowed are the ones described in SUBJECT. Keep the face, the head and the space around the head completely clean, with nothing drawn near them. NOT a glossy digital anime look: no flat cel shading, no uniform digital outlines, no big shiny anime eyes. Keep the painting simple and readable when printed small (about 5 cm tall).

COMPOSITION: One cat only, centered, filling about 70% of the canvas height, with generous empty space around it. Plain pure white background with no paper texture, no frame, no floor; only a very faint pale ink wash shadow under the cat. No props unless described above.

TEXT: Write only the name "American Shorthair" once, in small, simple, neat hand-lettered brush letters in soft dark sumi ink, centered just below the cat, about 6% of the canvas height, on a single line. Spell it exactly: American Shorthair. No other text, letters, numbers, seals, signatures or watermarks anywhere.

OUTPUT: Highest available resolution (4K), 1:1 aspect ratio. Crisp, print-ready artwork.
```
