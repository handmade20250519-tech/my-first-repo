"""Geminiに「白紙の袋」で作ってもらった場面写真に、本物の袋の絵を貼る。
白紙の袋の明るさ(影・紙のざらつき)をそのまま絵にかけるので、光が自然になる。
使い方: python3 make_scene_blank.py greatdane_1"""
import os
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).parent))
import make_listing_variants as mv

if os.environ.get("IMG_DIR"):  # この会話で受け取った画像の場所
    mv.D = Path(os.environ["IMG_DIR"])

HERE = Path(__file__).parent
# 名前: (場面の画像, [(貼る絵, 袋の四隅[左上・右上・右下・左下]), ...])
SCENES = {
    "greatdane_2": ("154.jpg", [
        # 左にうしろ、右におもて(ユーザーの案)。うしろの右端のしっぽと、おもての左端のおしりがつながって見える
        (HERE / "check/back_greatdane_final.png", [(203, 265), (470, 265), (472, 683), (201, 683)]),
        (HERE / "check/front_greatdane_final.png", [(502, 265), (765, 265), (770, 683), (500, 683)]),
    ]),
    "chipoo_1": ("165.jpg", [  # Geminiで袋を小さくした版(164.jpgは袋が大きすぎた)
        ("160.jpg", [(517, 548), (757, 548), (760, 936), (515, 939)]),
    ]),
    "chin_1": ("224.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.56)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_chin_pad.png)
        (HERE / "check/front_chin_pad.png", [(942, 774), (1095, 774), (1095, 1049), (941, 1049)]),
    ]),
    "maltipoo_1": ("213.jpg", [
        # 作り直した絵。Geminiの袋が本物より細長い(幅:高さ=0.61)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_maltipoo_pad.png)
        (HERE / "check/front_maltipoo_pad.png", [(947, 748), (1112, 748), (1113, 1020), (947, 1020)]),
    ]),
    "frenchbulldog_1": ("210.jpg", [
        # 作り直した絵。Geminiの袋が本物より細長い(幅:高さ=0.59)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_frenchbulldog_pad.png)
        (HERE / "check/front_frenchbulldog_pad.png", [(967, 735), (1120, 735), (1121, 995), (967, 995)]),
    ]),
    "bichon_1": ("204.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.57)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_bichon_pad.png)
        (HERE / "check/front_bichon_pad.png", [(940, 742), (1097, 742), (1098, 1017), (939, 1017)]),
    ]),
    "chashiro_1": ("203.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.60)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_chashiro_pad.png)
        (HERE / "check/front_chashiro_pad.png", [(975, 733), (1130, 733), (1131, 990), (975, 990)]),
    ]),
    "papillon_1": ("198.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.58)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_papillon_pad.png)
        (HERE / "check/front_papillon_pad.png", [(928, 774), (1089, 774), (1090, 1053), (928, 1053)]),
    ]),
    "sphynx_1": ("194.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.60)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_sphynx_pad.png)
        (HERE / "check/front_sphynx_pad.png", [(930, 681), (1118, 681), (1118, 994), (930, 993)]),
    ]),
    "newfoundland_1": ("191.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.62)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_newfoundland_pad.png)
        (HERE / "check/front_newfoundland_pad.png", [(959, 766), (1120, 766), (1121, 1028), (959, 1027)]),
    ]),
    "italiangreyhound_1": ("188.jpg", [
        # 作り直した絵。Geminiの袋が本物より細長い(幅:高さ=0.64)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_italiangreyhound_pad.png)
        (HERE / "check/front_italiangreyhound_pad.png", [(957, 709), (1146, 712), (1145, 1010), (953, 1006)]),
    ]),
    "toypoodle_1": ("186.jpg", [
        # 作り直した絵(うれしい顔)。Geminiの袋が本物より細長い(幅:高さ=0.63)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_toypoodle_pad.png)
        (HERE / "check/front_toypoodle_pad.png", [(916, 721), (1129, 723), (1131, 1069), (911, 1064)]),
    ]),
    "bernese_1": ("181.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.61)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_bernese_pad.png)
        (HERE / "check/front_bernese_pad.png", [(945, 785), (1113, 786), (1115, 1064), (946, 1063)]),
    ]),
    "hachiware_1": ("177.jpg", [
        # 作り直した絵(ごめん寝)。Geminiの袋が本物より太い(幅:高さ=0.72、本物は0.67)。絵がのびないように、
        # 左右に紙の白を足した(check/front_hachiware_pad.png)
        (HERE / "check/front_hachiware_pad.png", [(911, 695), (1154, 695), (1153, 1036), (907, 1033)]),
    ]),
    "wire_1": ("176.jpg", [
        # 本物のワイヤーダックスが写った場面(ユーザーが前に作った場面写真は、袋の絵がGeminiの描いたものだったので作り直した)。
        # 袋の表は、PDFがないので listing_wire_3.jpg の無地の袋から切り出した(check/front_wire_blank.png)。形は本物とほぼ同じ(0.68)
        (HERE / "check/front_wire_blank.png", [(961, 725), (1158, 726), (1158, 1018), (959, 1015)]),
    ]),
    "british_postcard": ("174.jpg", [
        # 横向きのポストカードの机の写真(templates/scenes/174.jpg)を使い回す
        (HERE / "check/postcard_british_full_yoko.png", [(320, 295), (877, 294), (878, 660), (322, 663)]),
        (HERE / "check/postcard_british_letter_yoko.png", [(440, 757), (1039, 812), (1002, 1069), (275, 983)]),
    ]),
    "samoyed_postcard": ("174.jpg", [
        # 横向きのポストカードの机の写真(templates/scenes/174.jpg)を使い回す
        (HERE / "check/postcard_samoyed_full_yoko.png", [(320, 295), (877, 294), (878, 660), (322, 663)]),
        (HERE / "check/postcard_samoyed_letter_yoko.png", [(440, 757), (1039, 812), (1002, 1069), (275, 983)]),
    ]),
    "frenchbulldog_postcard": ("174.jpg", [
        # 横向きのポストカードの机の写真(templates/scenes/174.jpg)を使い回す
        (HERE / "check/postcard_frenchbulldog_full_yoko.png", [(320, 295), (877, 294), (878, 660), (322, 663)]),
        (HERE / "check/postcard_frenchbulldog_letter_yoko.png", [(440, 757), (1039, 812), (1002, 1069), (275, 983)]),
    ]),
    "stbernard_postcard": ("174.jpg", [
        # 横向きのポストカードの机の写真(templates/scenes/174.jpg)を使い回す
        (HERE / "check/postcard_stbernard_full_yoko.png", [(320, 295), (877, 294), (878, 660), (322, 663)]),
        (HERE / "check/postcard_stbernard_letter_yoko.png", [(440, 757), (1039, 812), (1002, 1069), (275, 983)]),
    ]),
    "corgi_postcard": ("174.jpg", [
        # 横向きのポストカードの机の写真(templates/scenes/174.jpg)を使い回す
        (HERE / "check/postcard_corgi_full_yoko.png", [(320, 295), (877, 294), (878, 660), (322, 663)]),
        (HERE / "check/postcard_corgi_letter_yoko.png", [(440, 757), (1039, 812), (1002, 1069), (275, 983)]),
    ]),
    "bichon_postcard": ("174.jpg", [
        # 横向きのポストカードの机の写真(templates/scenes/174.jpg)を使い回す
        (HERE / "check/postcard_bichon_full_yoko.png", [(320, 295), (877, 294), (878, 660), (322, 663)]),
        (HERE / "check/postcard_bichon_letter_yoko.png", [(440, 757), (1039, 812), (1002, 1069), (275, 983)]),
    ]),
    "chashiro_postcard": ("174.jpg", [
        # 横向きのポストカードの机の写真(templates/scenes/174.jpg)を使い回す
        (HERE / "check/postcard_chashiro_full_yoko.png", [(320, 295), (877, 294), (878, 660), (322, 663)]),
        (HERE / "check/postcard_chashiro_letter_yoko.png", [(440, 757), (1039, 812), (1002, 1069), (275, 983)]),
    ]),
    "sphynx_postcard": ("174.jpg", [
        # 横向きのポストカードの机の写真(ワイヤーダックスと同じ)を使い回す
        (HERE / "check/postcard_sphynx_full_yoko.png", [(320, 295), (877, 294), (878, 660), (322, 663)]),
        (HERE / "check/postcard_sphynx_letter_yoko.png", [(440, 757), (1039, 812), (1002, 1069), (275, 983)]),
    ]),
    "italiangreyhound_postcard": ("174.jpg", [
        # 横向きのポストカードの机の写真(ワイヤーダックスと同じ)を使い回す
        (HERE / "check/postcard_italiangreyhound_full_yoko.png", [(320, 295), (877, 294), (878, 660), (322, 663)]),
        (HERE / "check/postcard_italiangreyhound_letter_yoko.png", [(440, 757), (1039, 812), (1002, 1069), (275, 983)]),
    ]),
    "hachiware_postcard": ("174.jpg", [
        # 横向きのポストカードの机の写真(ワイヤーダックスと同じ写真)を使い回す。四隅とKEEPも同じ
        (HERE / "check/postcard_hachiware_full_yoko.png", [(320, 295), (877, 294), (878, 660), (322, 663)]),
        (HERE / "check/postcard_hachiware_letter_yoko.png", [(440, 757), (1039, 812), (1002, 1069), (275, 983)]),
    ]),
    "wire_postcard": ("174.jpg", [
        # 横向きのポストカード2種の場面。立てたカード(絵いっぱい)は全体が見えていて、木のスタンドがその手前にある(KEEPでスタンドを戻す)
        (HERE / "check/postcard_wire_full_yoko.png", [(320, 295), (877, 294), (878, 660), (322, 663)]),
        # 机に置いたカード(手紙用)。奥のふちがカードの上
        (HERE / "check/postcard_wire_letter_yoko.png", [(440, 757), (1039, 812), (1002, 1069), (275, 983)]),
    ]),
    "chin_postcard": ("172.jpg", [
        # 縦向きのポストカードの机の写真(templates/scenes/172.jpg)を使い回す
        (HERE / "check/postcard_chin_full_visible.png", [(255, 232), (604, 232), (608, 707), (257, 707)]),
        (HERE / "check/postcard_chin_letter.png", [(724, 708), (1084, 752), (977, 1098), (502, 1002)]),
    ]),
    "akita_postcard": ("172.jpg", [
        # 縦向きのポストカードの机の写真(templates/scenes/172.jpg)を使い回す
        (HERE / "check/postcard_akita_full_visible.png", [(255, 232), (604, 232), (608, 707), (257, 707)]),
        (HERE / "check/postcard_akita_letter.png", [(724, 708), (1084, 752), (977, 1098), (502, 1002)]),
    ]),
    "mike_postcard": ("172.jpg", [
        # 縦向きのポストカードの机の写真(templates/scenes/172.jpg)を使い回す
        (HERE / "check/postcard_mike_full_visible.png", [(255, 232), (604, 232), (608, 707), (257, 707)]),
        (HERE / "check/postcard_mike_letter.png", [(724, 708), (1084, 752), (977, 1098), (502, 1002)]),
    ]),
    "maltipoo_postcard": ("172.jpg", [
        # 縦向きのポストカードの机の写真(templates/scenes/172.jpg)を使い回す
        (HERE / "check/postcard_maltipoo_full_visible.png", [(255, 232), (604, 232), (608, 707), (257, 707)]),
        (HERE / "check/postcard_maltipoo_letter.png", [(724, 708), (1084, 752), (977, 1098), (502, 1002)]),
    ]),
    "golden_postcard": ("172.jpg", [
        # 縦向きのポストカードの机の写真(templates/scenes/172.jpg)を使い回す
        (HERE / "check/postcard_golden_full_visible.png", [(255, 232), (604, 232), (608, 707), (257, 707)]),
        (HERE / "check/postcard_golden_letter.png", [(724, 708), (1084, 752), (977, 1098), (502, 1002)]),
    ]),
    "maltese_postcard": ("172.jpg", [
        # 縦向きのポストカードの机の写真(柴犬と同じ)を使い回す
        (HERE / "check/postcard_maltese_full_visible.png", [(255, 232), (604, 232), (608, 707), (257, 707)]),
        (HERE / "check/postcard_maltese_letter.png", [(724, 708), (1084, 752), (977, 1098), (502, 1002)]),
    ]),
    "schnauzer_postcard": ("172.jpg", [
        # 縦向きのポストカードの机の写真(柴犬と同じ)を使い回す
        (HERE / "check/postcard_schnauzer_full_visible.png", [(255, 232), (604, 232), (608, 707), (257, 707)]),
        (HERE / "check/postcard_schnauzer_letter.png", [(724, 708), (1084, 752), (977, 1098), (502, 1002)]),
    ]),
    "whitecat_postcard": ("172.jpg", [
        # 縦向きのポストカードの机の写真(柴犬と同じ)を使い回す
        (HERE / "check/postcard_whitecat_full_visible.png", [(255, 232), (604, 232), (608, 707), (257, 707)]),
        (HERE / "check/postcard_whitecat_letter.png", [(724, 708), (1084, 752), (977, 1098), (502, 1002)]),
    ]),
    "papillon_postcard": ("172.jpg", [
        # 縦向きのポストカードの机の写真(柴犬と同じ)を使い回す
        (HERE / "check/postcard_papillon_full_visible.png", [(255, 232), (604, 232), (608, 707), (257, 707)]),
        (HERE / "check/postcard_papillon_letter.png", [(724, 708), (1084, 752), (977, 1098), (502, 1002)]),
    ]),
    "chatora_postcard": ("172.jpg", [
        # 縦向きのポストカードの机の写真(柴犬と同じ)を使い回す
        (HERE / "check/postcard_chatora_full_visible.png", [(255, 232), (604, 232), (608, 707), (257, 707)]),
        (HERE / "check/postcard_chatora_letter.png", [(724, 708), (1084, 752), (977, 1098), (502, 1002)]),
    ]),
    "newfoundland_postcard": ("172.jpg", [
        # 縦向きのポストカードの机の写真(柴犬と同じ)を使い回す
        (HERE / "check/postcard_newfoundland_full_visible.png", [(255, 232), (604, 232), (608, 707), (257, 707)]),
        (HERE / "check/postcard_newfoundland_letter.png", [(724, 708), (1084, 752), (977, 1098), (502, 1002)]),
    ]),
    "toypoodle_postcard": ("172.jpg", [
        # 縦向きのポストカードの机の写真(柴犬と同じ)を使い回す
        (HERE / "check/postcard_toypoodle_full_visible.png", [(255, 232), (604, 232), (608, 707), (257, 707)]),
        (HERE / "check/postcard_toypoodle_letter.png", [(724, 708), (1084, 752), (977, 1098), (502, 1002)]),
    ]),
    "bernese_postcard": ("172.jpg", [
        # 縦向きのポストカードの机の写真(柴犬と同じ写真)を使い回す。四隅も同じ
        (HERE / "check/postcard_bernese_full_visible.png", [(255, 232), (604, 232), (608, 707), (257, 707)]),
        (HERE / "check/postcard_bernese_letter.png", [(724, 708), (1084, 752), (977, 1098), (502, 1002)]),
    ]),
    "shiba_postcard": ("172.jpg", [
        # ポストカード2種の場面。立てたカード(絵いっぱい)は、下がスタンドに入って見えない。
        # 見えている部分の幅:高さ=350:475 から、カードの上から約92%だけを貼る(check/postcard_shiba_full_visible.png)
        (HERE / "check/postcard_shiba_full_visible.png", [(255, 232), (604, 232), (608, 707), (257, 707)]),
        # 机に置いたカード(手紙用)。奥のふちがカードの上、手前のふちが下(縦向きのカードをななめ上から見ている)
        (HERE / "check/postcard_shiba_letter.png", [(724, 708), (1084, 752), (977, 1098), (502, 1002)]),
    ]),
    "shiba_1": ("170.jpg", [
        # 新しい絵(2回目の拒否柴)。Geminiの袋は本物とほぼ同じ形(幅:高さ=0.67)なので、そのまま貼る
        (HERE / "check/front_shiba_blank.png", [(994, 766), (1148, 767), (1146, 1003), (989, 999)]),
    ]),
    "stbernard_1": ("165.jpg", [
        # Geminiの袋は本物とほぼ同じ形(幅:高さ=0.67)なので、そのまま貼る
        (HERE / "check/front_stbernard_blank.png", [(945, 702), (1153, 702), (1154, 1013), (944, 1011)]),
    ]),
    "maltese_1": ("164.jpg", [
        # Geminiの袋は本物とほぼ同じ形(幅:高さ=0.68、本物は0.67)なので、そのまま貼る
        (HERE / "check/front_maltese_blank.png", [(958, 699), (1162, 700), (1161, 1003), (955, 998)]),
    ]),
    "schnauzer_1": ("163.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.66)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_schnauzer_pad.png)
        (HERE / "check/front_schnauzer_pad.png", [(941, 700), (1153, 700), (1151, 1022), (938, 1020)]),
    ]),
    "whitecat_1": ("162.jpg", [
        # Geminiの袋は本物と同じ形(幅:高さ=0.665)なので、そのまま貼る
        (HERE / "check/front_whitecat_blank.png", [(950, 685), (1161, 687), (1159, 1002), (946, 1001)]),
    ]),
    "corgi_1": ("160.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.66)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_corgi_pad.png)
        (HERE / "check/front_corgi_pad.png", [(946, 706), (1151, 706), (1151, 1020), (943, 1017)]),
    ]),
    "beagle_1": ("159.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.66)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_beagle_pad.png)
        (HERE / "check/front_beagle_pad.png", [(966, 712), (1167, 712), (1166, 1020), (964, 1018)]),
    ]),
    "golden_1": ("158.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.64)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_golden_pad.png)
        (HERE / "check/front_golden_pad.png", [(975, 751), (1159, 751), (1160, 1041), (974, 1039)]),
    ]),
    "sabatora_1": ("156.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.62)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_sabatora_pad.png)
        (HERE / "check/front_sabatora_pad.png", [(971, 756), (1147, 756), (1146, 1044), (967, 1041)]),
    ]),
    "pomeranian_1": ("155.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.66)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_pomeranian_pad.png)
        (HERE / "check/front_pomeranian_pad.png", [(941, 719), (1146, 719), (1141, 1033), (932, 1032)]),
    ]),
    "dachshund_1": ("154.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.66)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_dachshund_pad.png)
        (HERE / "check/front_dachshund_pad.png", [(952, 674), (1168, 674), (1166, 1006), (948, 1002)]),
    ]),
    "westie_1": ("151.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.64)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_westie_pad.png)
        (HERE / "check/front_westie_pad.png", [(966, 701), (1169, 701), (1166, 1021), (960, 1019)]),
    ]),
    "bedlington_1": ("149.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.59)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_bedlington_pad.png)
        (HERE / "check/front_bedlington_pad.png", [(1010, 807), (1149, 807), (1148, 1048), (1006, 1046)]),
    ]),
    "russianblue_1": ("147.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.62)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_russianblue_pad.png)
        (HERE / "check/front_russianblue_pad.png", [(951, 742), (1152, 742), (1151, 1073), (943, 1070)]),
    ]),
    "akita_1": ("146.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.68)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_akita_pad.png)
        (HERE / "check/front_akita_pad.png", [(985, 741), (1174, 741), (1171, 1025), (979, 1021)]),
    ]),
    "pug_1": ("145.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.63)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_pug_pad.png)
        (HERE / "check/front_pug_pad.png", [(987, 582), (1172, 582), (1169, 883), (975, 880)]),
    ]),
    "norwegian_1": ("143.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.61)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_norwegian_pad.png)
        (HERE / "check/front_norwegian_pad.png", [(974, 791), (1162, 791), (1159, 1101), (968, 1099)]),
    ]),
    "sheltie_1": ("142.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.59)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_sheltie_pad.png)
        (HERE / "check/front_sheltie_pad.png", [(1006, 686), (1161, 686), (1158, 956), (995, 951)]),
    ]),
    "sabi_1": ("123.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.66)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_sabi_pad.png)
        (HERE / "check/front_sabi_pad.png", [(974, 771), (1150, 771), (1147, 1046), (966, 1041)]),
    ]),
    "labrador_1": ("122.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.63)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_labrador_pad.png)
        (HERE / "check/front_labrador_pad.png", [(972, 785), (1149, 785), (1148, 1074), (966, 1070)]),
    ]),
    "shihtzu_1": ("121.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.60)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_shihtzu_pad.png)
        (HERE / "check/front_shihtzu_pad.png", [(950, 703), (1156, 703), (1153, 1049), (945, 1044)]),
    ]),
    "husky_1": ("119.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.63)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_husky_pad.png)
        (HERE / "check/front_husky_pad.png", [(1015, 791), (1164, 791), (1162, 1033), (1006, 1030)]),
    ]),
    "cavalier_1": ("116.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.59)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_cavalier_pad.png)
        (HERE / "check/front_cavalier_pad.png", [(946, 668), (1123, 668), (1121, 974), (940, 970)]),
    ]),
    "kijitora_1": ("114.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.62)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_kijitora_pad.png)
        (HERE / "check/front_kijitora_pad.png", [(927, 652), (1122, 652), (1120, 969), (922, 966)]),
    ]),
    "chihuahua_1": ("111.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.59)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_chihuahua_pad.png)
        (HERE / "check/front_chihuahua_pad.png", [(910, 692), (1108, 692), (1106, 1034), (904, 1031)]),
    ]),
    "samoyed_1": ("94.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.60)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_samoyed_pad.png)
        (HERE / "check/front_samoyed_pad.png", [(974, 802), (1105, 802), (1104, 1023), (970, 1022)]),
    ]),
    "scottish_1": ("80.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.62)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_scottish_pad.png)
        (HERE / "check/front_scottish_pad.png", [(973, 791), (1116, 791), (1113, 1028), (965, 1026)]),
    ]),
    "british_1": ("72.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.60)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_british_pad.png)
        (HERE / "check/front_british_pad.png", [(940, 753), (1104, 757), (1098, 1036), (930, 1031)]),
    ]),
    "ragdoll_1": ("63.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.61)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_ragdoll_pad.png)
        (HERE / "check/front_ragdoll_pad.png", [(878, 702), (1068, 702), (1071, 1019), (875, 1019)]),
    ]),
    "mike_1": ("55.jpg", [
        # 2026-11-08 作り直した絵。場面写真は前のまま(袋を白紙に戻した templates/scenes/55.jpg)。袋の形は本物とほぼ同じ(0.68)
        (HERE / "check/front_mike_blank.png", [(845, 686), (1066, 686), (1067, 1013), (843, 1013)]),
    ]),
    "borzoi_1": ("45.jpg", [
        # Geminiの袋が本物より少し細長い(幅:高さ=0.64)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_borzoi_pad.png)
        (HERE / "check/front_borzoi_pad.png", [(913, 764), (1056, 765), (1057, 990), (910, 988)]),
    ]),
    "yorkie_1": ("38.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.58)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_yorkie_pad.png)
        (HERE / "check/front_yorkie_pad.png", [(822, 689), (1040, 689), (1041, 1066), (819, 1066)]),
    ]),
    "jackrussell_1": ("31.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.62)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_jackrussell_pad.png)
        (HERE / "check/front_jackrussell_pad.png", [(900, 716), (1147, 716), (1147, 1117), (897, 1116)]),
    ]),
    "afghan_1": ("26.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.61)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_afghan_pad.png)
        (HERE / "check/front_afghan_pad.png", [(987, 918), (1114, 918), (1114, 1128), (984, 1127)]),
    ]),
    "kuroneko_1": ("21.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.59)。絵がつぶれないよう、幅に合わせて下にそろえ、上の余りは紙の白(check/front_kuroneko_pad.png)
        (HERE / "check/front_kuroneko_pad.png", [(951, 689), (1127, 689), (1126, 991), (946, 990)]),
    ]),
    "bordercollie_2": ("14.jpg", [
        # 左にうしろ(ユーザーが撮った組み立てた袋の写真を clean_back_photo.py で整えたもの)、右におもて(おとしだま)
        (HERE / "check/back_bordercollie_photo.png", [(234, 341), (599, 341), (599, 912), (234, 912)]),
        (HERE / "check/front_bordercollie_otoshidama.png", [(656, 341), (1020, 341), (1020, 911), (656, 911)]),
    ]),
    "bordercollie_1": ("12.jpg", [  # ふたを閉じた表側の袋。木の箱に立てかけた袋
        ("8.jpg", [(882, 610), (1122, 610), (1119, 968), (877, 967)]),
    ]),
    "munchkin_2": ("7.jpg", [  # ふたを閉じた表側の袋(プロンプトを直した版)。形が本物とほぼ同じなので、そのまま貼る
        ("1.jpg", [(665, 735), (844, 735), (848, 1005), (665, 1005)]),
    ]),
    "munchkin_1": ("5.jpg", [
        # Geminiの袋が本物より細長い(幅:高さ=0.58、本物は0.67)。絵がつぶれないように、
        # 絵は幅に合わせて袋の下にそろえ、上の余りは紙の白にした(check/front_munchkin_pad.png)
        (HERE / "check/front_munchkin_pad.png", [(1140, 822), (1516, 822), (1515, 1482), (1132, 1482)]),
    ]),
    "chatora_1": ("196.jpg", [
        # 作り直した絵。Geminiの袋が本物より細長い(幅:高さ=0.60)。絵は幅に合わせて下にそろえ、上の余りは紙の白(check/front_chatora_pad.png)
        (HERE / "check/front_chatora_pad.png", [(917, 719), (1116, 719), (1117, 1050), (916, 1048)]),
    ]),
}

# 貼ったあと、もとの写真に戻す部分(カードの手前にある物)。多角形の頂点
KEEP = {"wire_postcard": [[(381, 629), (819, 629), (819, 703), (381, 703)]]}
KEEP["hachiware_postcard"] = KEEP["italiangreyhound_postcard"] = KEEP["sphynx_postcard"] = KEEP["chashiro_postcard"] = KEEP["bichon_postcard"] = KEEP["stbernard_postcard"] = KEEP["frenchbulldog_postcard"] = KEEP["samoyed_postcard"] = KEEP["british_postcard"] = KEEP["corgi_postcard"] = KEEP["wire_postcard"]
# 切り取る範囲(左, 上, 右, 下)。下の角のボタンを外す
CROP = {"greatdane_2": (52, 0, 907, 855)}
# 白紙の袋に細い線(ふたの折り目など)が写っているとき、光をこの半径でならして線を消す
SMOOTH = {"munchkin_1": 20, "munchkin_2": 8, "bordercollie_1": 8, "kuroneko_1": 8, "afghan_1": 6, "jackrussell_1": 8, "yorkie_1": 8, "borzoi_1": 6, "mike_1": 8, "ragdoll_1": 8, "british_1": 8, "scottish_1": 6, "samoyed_1": 6, "chihuahua_1": 6, "kijitora_1": 6, "cavalier_1": 6, "husky_1": 6, "shihtzu_1": 6, "labrador_1": 6, "sabi_1": 6, "sheltie_1": 6, "norwegian_1": 6, "pug_1": 6, "akita_1": 6, "russianblue_1": 6, "bedlington_1": 6, "westie_1": 6, "dachshund_1": 6, "pomeranian_1": 6, "sabatora_1": 6, "golden_1": 6, "beagle_1": 6, "corgi_1": 6, "whitecat_1": 6, "schnauzer_1": 6, "maltese_1": 6, "stbernard_1": 6, "shiba_1": 6, "shiba_postcard": 6, "wire_postcard": 6, "wire_1": 6, "hachiware_1": 6, "hachiware_postcard": 6, "bernese_1": 6, "bernese_postcard": 6, "toypoodle_1": 6, "toypoodle_postcard": 6, "italiangreyhound_1": 6, "italiangreyhound_postcard": 6, "newfoundland_1": 6, "newfoundland_postcard": 6, "sphynx_postcard": 6, "sphynx_1": 6, "chatora_postcard": 6, "chatora_1": 6, "papillon_postcard": 6, "papillon_1": 6, "chashiro_postcard": 6, "chashiro_1": 6, "bichon_1": 6, "bichon_postcard": 6, "golden_postcard": 6, "stbernard_postcard": 6, "frenchbulldog_postcard": 6, "frenchbulldog_1": 6, "maltipoo_postcard": 6, "maltipoo_1": 6, "samoyed_postcard": 6, "mike_postcard": 6, "akita_postcard": 6, "british_postcard": 6, "chin_postcard": 6, "maltese_postcard": 6, "schnauzer_postcard": 6, "whitecat_postcard": 6, "corgi_postcard": 6, "chin_1": 6}


def coeffs(dst, src):
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
        B += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(B, float))


name = sys.argv[1]
scene_fn, items = SCENES[name]
# 使い回す写真(ポストカードの机など)は templates/scenes に保存してある。会話の画像フォルダになければそちらを使う
scene_path = mv.D / scene_fn
if not scene_path.exists():
    scene_path = HERE.parent / "templates" / "scenes" / scene_fn
scene = Image.open(scene_path).convert("RGB")
W, H = scene.size
out = np.asarray(scene).astype(float)
for art_path, quad in items:
    # 文字列ならCanvaのスクリーンショット(袋の表を切り出す)、Pathなら絵そのもの
    art = (mv.front(mv.D / art_path) if isinstance(art_path, str) else Image.open(art_path)).convert("RGB")
    aw, ah = art.size
    aa = np.asarray(art).astype(float)
    paper = np.median(aa[aa.min(2) > 200], axis=0)  # 絵の紙の白
    warped = np.asarray(art.transform((W, H), Image.PERSPECTIVE,
                                      coeffs(quad, [(0, 0), (aw, 0), (aw, ah), (0, ah)]), Image.BICUBIC,
                                      fillcolor=tuple(int(v) for v in paper))).astype(float)  # 絵の外は紙の白(黒い線を出さない)
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).polygon(quad, fill=255)
    inner = np.asarray(mask.filter(ImageFilter.MinFilter(5))) > 0
    # 白紙の袋の明るさ = 光と影(袋のふちの影は除いて、少しなめらかに)
    sc = np.asarray(scene.filter(ImageFilter.GaussianBlur(1.2))).astype(float)
    white = np.percentile(sc[inner], 99, axis=0)
    light = sc / white
    if name in SMOOTH:  # 袋の内側だけで光をならす(ふちの影や、となりの物の色を混ぜない)
        m = inner.astype(float)[..., None]
        r = SMOOTH[name]

        def blur(x):  # 箱形のぼかしを2回(ガウスぼかしに近い)
            for _ in range(2):
                for ax in (0, 1):
                    c = np.cumsum(np.pad(x, [(r + 1, r) if a == ax else (0, 0) for a in range(x.ndim)], mode="edge"), axis=ax)
                    x = (np.take(c, range(2 * r + 1, c.shape[ax]), axis=ax) - np.take(c, range(0, c.shape[ax] - 2 * r - 1), axis=ax)) / (2 * r + 1)
            return x
        bm = blur(m)  # 袋のふち(内側の外)も、内側の光でうめる
        light = np.where(bm > 0.05, blur(light * m) / np.maximum(bm, 1e-3), light)
    res = np.clip(warped / paper * light * white, 0, 255)
    al = (np.asarray(mask.filter(ImageFilter.GaussianBlur(0.7))).astype(float) / 255)[..., None]
    out = out * (1 - al) + res * al
for poly in KEEP.get(name, []):  # カードの手前にある物(スタンドなど)を、もとの写真に戻す
    km = Image.new("L", (W, H), 0)
    ImageDraw.Draw(km).polygon(poly, fill=255)
    ka = (np.asarray(km.filter(ImageFilter.GaussianBlur(0.7))).astype(float) / 255)[..., None]
    out = out * (1 - ka) + np.asarray(scene).astype(float) * ka
res_im = Image.fromarray(out.astype(np.uint8))
if name in CROP:  # Geminiの画面のボタン(編集・共有)が写っているとき、正方形に切り取って外す
    res_im = res_im.crop(CROP[name])
res_im.save(HERE / f"scene_{name}.jpg", quality=92)
print("done", f"scene_{name}.jpg")
