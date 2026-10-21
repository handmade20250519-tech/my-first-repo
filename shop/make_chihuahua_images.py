"""チワワの商品画像(1枚目のデザイン見本と、3枚目の6種類)。"""
from pathlib import Path
import os
import sys
sys.path.insert(0, str(Path(__file__).parent))
import make_listing_variants as mv
import make_covers

mv.D = Path(os.environ.get("IMG_DIR", "/tmp/claude-0/-home-user/068ade54-c79c-53ef-8da1-36e19e767c22/images"))

# 1枚目は、のしのみ・おとしだまの袋から作る(左上にダウンロード商品のマーク)
make_covers.make("chihuahua", (mv.front(mv.D / "106.jpg"), mv.front(mv.D / "107.jpg")))

# 6種類の画像は、こころばかりの画像がそろってから作る(例: python3 make_chihuahua_images.py <こころばかり>)
if len(sys.argv) > 1:
    mv.main([("106.jpg", "のしのみ"), ("107.jpg", "おとしだま"), ("108.jpg", "ありがとう"),
             ("109.jpg", "おめでとう"), (sys.argv[1], "こころばかり"), ("105.jpg", "無地(手書き用)")],
            "listing_chihuahua_3.jpg")
print("done")
