"""共有カード img/ogp.png（1200x630）を作る。文言を変えたらこれを再実行する。"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RED, NAVY, INK, GRAY = (193, 57, 44), (16, 22, 91), (37, 37, 37), (242, 242, 242)
BOLD = "/System/Library/Fonts/ヒラギノ角ゴシック W7.ttc"
MID = "/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc"

img = Image.new("RGB", (1200, 630), (255, 255, 255))
d = ImageDraw.Draw(img)
d.rectangle([0, 0, 1200, 14], fill=RED)
d.rectangle([0, 560, 1200, 630], fill=NAVY)
d.text((80, 90), "SAKENOTE LAB", font=ImageFont.truetype(BOLD, 34), fill=RED)
f = ImageFont.truetype(BOLD, 64)
for i, line in enumerate(["麹がラップする。", "杜氏が麻雀を打つ。", "お猪口が菰樽に育つ。"]):
    d.text((80, 160 + i * 92), line, font=f, fill=NAVY)
d.text((80, 470), "醸造とお酒の専門家がつくった、ゲームと知識ツール", font=ImageFont.truetype(MID, 32), fill=INK)
d.text((80, 578), "合同会社サケノテ", font=ImageFont.truetype(BOLD, 30), fill=(255, 255, 255))
img.save(ROOT / "img" / "ogp.png", optimize=True)
print("img/ogp.png")
