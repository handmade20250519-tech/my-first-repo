# 商品画像の並べかえ(1枚目をデザイン見本に)

理由: minneの一覧では1枚目の画像しか見えない。場面写真が1枚目だと袋が小さく、ぽち袋の商品だと分かりにくい(ユーザーと決めた)。
一覧での見え方の確認: shop/preview_first_images.jpg(24種の1枚目を一覧の大きさに縮めたもの)

## 新しい並び(全種類共通)
1. listing_<名前>_1.jpg(デザイン見本)
2. 場面写真(注記入り)
3. listing_<名前>_3.jpg(6種類)
4. listing_shiba_4.jpg(作り方)

## 種類ごとのチェック表
| 済 | 種類 | 1枚目 | 2枚目(場面写真) |
|---|---|---|---|
| □ | 柴犬 | listing_shiba_1.jpg | ユーザーが自分で作った場面写真(リポジトリにない) |
| □ | トイプードル | listing_toypoodle_1.jpg | ユーザーが自分で作った場面写真(リポジトリにない) |
| □ | ワイヤーダックス | listing_wire_1.jpg | ユーザーが自分で作った場面写真(リポジトリにない) |
| □ | フレンチブルドッグ | listing_frenchie_1.jpg | ユーザーが自分で作った場面写真(リポジトリにない) |
| □ | イタリアングレーハウンド | listing_italiangreyhound_1.jpg | ユーザーが自分で作った場面写真(リポジトリにない) |
| □ | 日本の雑種 | listing_japanesemix_1.jpg | scene_japanesemix_1_note.jpg |
| □ | マルプー | listing_maltipoo_1.jpg | ユーザーが自分で作った場面写真(リポジトリにない) |
| □ | チワプー | listing_chipoo_1.jpg | scene_chipoo_1_note.jpg |
| □ | グレートデーン | listing_greatdane_1.jpg | scene_greatdane_2_note.jpg |
| □ | ボーダーコリー | listing_bordercollie_1.jpg | scene_bordercollie_1_note.jpg / scene_bordercollie_2_note.jpg |
| □ | ジャックラッセルテリア | listing_jackrussell_1.jpg | scene_jackrussell_1_note.jpg |
| □ | ヨークシャーテリア | listing_yorkie_1.jpg | scene_yorkie_1_note.jpg |
| □ | アフガンハウンド | listing_afghan_1.jpg | scene_afghan_1_note.jpg |
| □ | ボルゾイ | listing_borzoi_1.jpg | scene_borzoi_1_note.jpg |
| □ | サモエド | listing_samoyed_1.jpg | scene_samoyed_1_note.jpg |
| □ | チワワ(新しく出品) | listing_chihuahua_1.jpg | scene_chihuahua_1_note.jpg |
| □ | キジトラ(書き直して出品) | listing_kijitora_1.jpg | scene_kijitora_1_note.jpg |
| □ | キャバリア(新しく出品) | listing_cavalier_1.jpg | scene_cavalier_1_note.jpg |
| □ | ハチワレ | listing_hachiware_1.jpg | ユーザーが自分で作った場面写真(リポジトリにない) |
| □ | アメリカンショートヘア | listing_americanshorthair_1.jpg | scene_americanshorthair_1_note.jpg |
| □ | 茶トラ | listing_chatora_1.jpg | scene_chatora_1_note.jpg |
| □ | マンチカン | listing_munchkin_1.jpg | scene_munchkin_2_note.jpg |
| □ | 黒猫 | listing_kuroneko_1.jpg | scene_kuroneko_1_note.jpg |
| □ | 三毛猫 | listing_mike_1.jpg | scene_mike_1_note.jpg |
| □ | ラグドール | listing_ragdoll_1.jpg | scene_ragdoll_1_note.jpg |
| □ | ブリティッシュショートヘア | listing_british_1.jpg | scene_british_1_note.jpg |
| □ | スコティッシュフォールド | listing_scottish_1.jpg | scene_scottish_1_note.jpg |

## 気づいたこと
- 一覧の大きさでは、表書き「おとしだま」の文字がいちばん目立ち、犬・猫が小さく見える種類がある(マルプー、チワプー、黒猫、スコティッシュなど)。並べかえのあと、アクセス数が増えなければ、犬・猫を大きく見せる1枚目専用の画像を作る
- 柴犬の1枚目も、ほかと同じ形に作り直した(shop/make_shiba_cover.py。もとのスクリーンショットがないので、listing_shiba_3.jpg から袋を切り出した)

## 1枚目の作り直し(マークの位置)
- minneの一覧では右下にハートボタンが重なり、「ダウンロード商品」のマークが欠けて見えた。マークを左上に移し、右下を空けた(ユーザーの依頼)
- 24種類まとめて `python3 shop/make_covers.py` で作り直した。袋の絵は listing_<名前>_3.jpg から切り出す
- 確認画像 shop/preview_first_images.jpg には、ハートボタンの位置を灰色の丸で入れた
