"""共有カード img/ogp.png（1200x630）を作る。ページと同じ生成りの地に暖簾の絵だけ。暖簾の絵を替えたらこれを再実行する。"""
from PIL import Image
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BG = (243, 239, 230)  # style.css の --bg
W, H, PAD = 1200, 630, 40

noren = Image.open(ROOT / "img" / "art" / "label_top.webp").convert("RGBA")
scale = min((W - PAD * 2) / noren.width, (H - PAD * 2) / noren.height)
noren = noren.resize((round(noren.width * scale), round(noren.height * scale)), Image.LANCZOS)

img = Image.new("RGB", (W, H), BG)
img.paste(noren, ((W - noren.width) // 2, (H - noren.height) // 2), noren)
img.save(ROOT / "img" / "ogp.png", optimize=True)
print("img/ogp.png")
