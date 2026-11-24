# 出品文(STEP5) 豆柴のぽち袋+ポストカード+あけおめ動画 データ版

2026-11-24 新しく足した犬種(黒の豆柴)。絵の指示文は `minne-pochi-next-prompts.md` の豆柴(黒)。

## 商品名

## 説明文
```
```

## ZIPの名前
uchinoko-aruaru_mameshiba_pochi.zip(中身: x)

## 商品画像
- ポストカード(縦向き): `make_postcard.py templates/originals/mameshiba.jpg mameshiba full/letter --label "Mame Shiba"`。商品画像 shop/listing_mameshiba_postcard.jpg、机の写真 shop/scene_mameshiba_postcard_note.jpg。Geminiに渡す横長の画像 shop/video_base/mameshiba_gemini_16x9.png
- 2026-11-24 ぽち袋のPDF(MameShiba.pdf、templates/pdf/)から listing_mameshiba_1/3 と check/front_mameshiba_blank.png を作った。6ページとも64×95mm。袋の名前は黒の書体
- 2026-11-24 場面写真: templates/scenes/290.jpg(ユーザーがGeminiで作った)に front_mameshiba_pad.png(0.61)を貼った → shop/scene_mameshiba_1_note.jpg
- 商品画像の並び: 1 listing_mameshiba_1.jpg → 2 listing_mameshiba_video.jpg → 3 listing_mameshiba_3.jpg → 4 listing_mameshiba_postcard.jpg → 5 scene_mameshiba_1_note.jpg → 6 scene_mameshiba_postcard_note.jpg → 7 listing_shiba_4.jpg

## 場面写真(Geminiのプロンプト)
袋は真っ白で作ってもらい、本物の絵はあとで `shop/make_scene_blank.py` で貼る(袋の表は check/front_mameshiba_blank.png)。
```
A warm, natural lifestyle photo, square 1:1. A cozy Japanese room with tatami mats and a low wooden shelf, in soft afternoon light. The background is softly blurred.

On the tatami in the front right, one small closed Japanese pochi-bukuro money envelope stands upright, propped against a small wooden box. We see only its FRONT side: one clean, flat, plain rectangle of matte white paper with crisp square corners. The flap is already closed and folded to the back, so NO flap, NO V-shaped fold, NO seam and NO fold lines are visible on the front. The rectangle is exactly 2:3 in width to height (6.4 cm wide, 9.5 cm tall), not narrower. The front is COMPLETELY BLANK: no drawing, no text, no pattern, no logo, no noshi mark. The envelope faces the camera straight on, flat and not tilted, with all four corners clearly visible and not covered by anything. It takes up about 25% of the image width, large and easy to see.

On the left, a real adult black-and-tan Mame Shiba (a small Shiba Inu with tan eyebrow spots, a cream-white chest and a curled tail) sits neatly on the tatami and tilts its head to one side with curiosity, as if someone just called its name. Real dog, not a cartoon, not a puppy. The dog does not touch or cover the envelope.

Photorealistic, shallow depth of field, gentle shadows, calm muted colors. No people, no hands, no text anywhere in the image.
```
- 2026-11-24 あけおめ動画1回目: Geminiが絵を拡大して、耳の先と前足の先が切れた(shop/video_base/mameshiba_gemini_raw_v1_zoomed.mp4)。横長の画像を渡し、「カメラ固定・ズームしない・全身を入れる」と足して作り直しをお願いした
- 2026-11-24 あけおめ動画2回目: 20秒になって届いたが、はじめの10秒は1回目とまったく同じ(同じ会話の中で頼んだので、1回目の動画をのばした形になった)。後半も拡大されたままで切れている(shop/video_base/mameshiba_gemini_raw_v2_extended.mp4)。犬をさらに小さく置いた横長の画像 shop/video_base/mameshiba_gemini_16x9_small.png(犬の高さ55%)を作り、新しい会話で作り直すようお願いした
