# 出品文(STEP5) ダルメシアンのぽち袋+ポストカード+あけおめ動画 データ版

2026-11-22 新しく足した犬種。絵の指示文は `minne-pochi-next-prompts.md` のダルメシアン。

## 商品名

## 説明文
```
```

## ZIPの名前
uchinoko-aruaru_dalmatian_pochi.zip(中身: x)

## 商品画像
- ポストカード(縦向き): `make_postcard.py templates/originals/dalmatian.jpg dalmatian full/letter --label "Dalmatian"`。商品画像 shop/listing_dalmatian_postcard.jpg、机の写真 shop/scene_dalmatian_postcard_note.jpg。Geminiに渡す横長の画像 shop/video_base/dalmatian_gemini_16x9.png
- 2026-11-22 ぽち袋のPDF(Dalmatian.pdf、templates/pdf/)から listing_dalmatian_1/3 と check/front_dalmatian_blank.png を作った。6ページとも64×95mm。袋の名前は青の書体
- 商品画像の並び: 1 listing_dalmatian_1.jpg → 2 listing_dalmatian_video.jpg → 3 listing_dalmatian_3.jpg → 4 listing_dalmatian_postcard.jpg → 5 scene_dalmatian_1_note.jpg → 6 scene_dalmatian_postcard_note.jpg → 7 listing_shiba_4.jpg

## 場面写真(Geminiのプロンプト)
袋は真っ白で作ってもらい、本物の絵はあとで `shop/make_scene_blank.py` で貼る(袋の表は check/front_dalmatian_blank.png)。
```
A warm, natural lifestyle photo, square 1:1. The entrance hall (genkan) of a cozy Japanese home in soft afternoon light, with a light-wood floor step and a few pairs of shoes neatly placed. The background is softly blurred.

On the wooden floor step in the front right, one small closed Japanese pochi-bukuro money envelope stands upright, propped against a small wooden box. We see only its FRONT side: one clean, flat, plain rectangle of matte white paper with crisp square corners. The flap is already closed and folded to the back, so NO flap, NO V-shaped fold, NO seam and NO fold lines are visible on the front. The rectangle is exactly 2:3 in width to height (6.4 cm wide, 9.5 cm tall), not narrower. The front is COMPLETELY BLANK: no drawing, no text, no pattern, no logo, no noshi mark. The envelope faces the camera straight on, flat and not tilted, with all four corners clearly visible and not covered by anything. It takes up about 25% of the image width, large and easy to see.

On the left, a real adult Dalmatian with a white coat and black spots sits on the floor, happily welcoming its family home, eyes softly narrowed and mouth open in a big, happy grin, tail wagging. Real dog, not a cartoon. The dog does not touch or cover the envelope.

Photorealistic, shallow depth of field, gentle shadows, calm muted colors. No people, no hands, no text anywhere in the image.
```
