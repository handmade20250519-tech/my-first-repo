# 出品文(STEP5) ベンガルのぽち袋+ポストカード+あけおめ動画 データ版

2026-11-27 新しく足した猫種。絵の指示文は `minne-pochi-next-prompts.md` のベンガル(最後の「立水栓」の指示文)。

## 商品名

## 説明文
```
```

## ZIPの名前
uchinoko-aruaru_bengal_pochi.zip(中身: x)

## 商品画像
- 絵: 1枚目は蛇口が宙に浮き、2枚目はたらいの水の上に猫が乗って見えたので、庭の立水栓の絵に作り直した(templates/originals/bengal.jpg。前の絵は bengal_v1_floating_faucet.jpg、bengal_v2_tub_pipe.jpg)
- ポストカード(縦向き): `make_postcard.py templates/originals/bengal.jpg bengal full/letter --label "Bengal"`。商品画像 shop/listing_bengal_postcard.jpg、机の写真 shop/scene_bengal_postcard_note.jpg。Geminiに渡す横長の画像 shop/video_base/bengal_gemini_16x9.png
- 2026-11-27 ぽち袋のPDF(Bengal.pdf、templates/pdf/。立水栓の絵)から listing_bengal_1/3 と check/front_bengal_blank.png を作った。6ページとも64×95mm。袋の名前は茶色の書体
- 2026-11-27 場面写真: templates/scenes/299.jpg(ユーザーがGeminiで作った)に front_bengal_pad.png(0.60)を貼った → shop/scene_bengal_1_note.jpg
- 商品画像の並び: 1 listing_bengal_1.jpg → 2 listing_bengal_video.jpg → 3 listing_bengal_3.jpg → 4 listing_bengal_postcard.jpg → 5 scene_bengal_1_note.jpg → 6 scene_bengal_postcard_note.jpg → 7 listing_shiba_4.jpg

## 場面写真(Geminiのプロンプト)
袋は真っ白で作ってもらい、本物の絵はあとで `shop/make_scene_blank.py` で貼る(袋の表は check/front_bengal_blank.png)。
```
A warm, natural lifestyle photo, square 1:1. A small, tidy Japanese garden corner in soft afternoon light, with a simple wooden garden standing water tap, a few flat stepping stones and some green plants. The background is softly blurred.

On a flat stepping stone in the front right, one small closed Japanese pochi-bukuro money envelope stands upright, propped against a small wooden box. We see only its FRONT side: one clean, flat, plain rectangle of matte white paper with crisp square corners. The flap is already closed and folded to the back, so NO flap, NO V-shaped fold, NO seam and NO fold lines are visible on the front. The rectangle is exactly 2:3 in width to height (6.4 cm wide, 9.5 cm tall), not narrower. The front is COMPLETELY BLANK: no drawing, no text, no pattern, no logo, no noshi mark. The envelope faces the camera straight on, flat and not tilted, with all four corners clearly visible and not covered by anything. It takes up about 25% of the image width, large and easy to see.

On the left, a real adult Bengal cat (golden coat with dark leopard-like rosettes) sits on the ground next to the standing tap, reaching one front paw toward a thin stream of water running from the faucet, watching it with a focused, serious face. Real cat, not a cartoon. The cat and the water do not touch or cover the envelope, and the envelope stays dry.

Photorealistic, shallow depth of field, gentle shadows, calm muted colors. No people, no hands, no text anywhere in the image.
```
