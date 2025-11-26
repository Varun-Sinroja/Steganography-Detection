import os
from PIL import Image
from stegano import lsb

os.makedirs("images/cover", exist_ok=True)
os.makedirs("images/stego", exist_ok=True)

for i in range(3):
    img = Image.new("RGB", (200, 200), (i*80, 100, 150))
    img.save(f"images/cover/cover_{i+1}.png")

print("✅ 3 cover images created in 'images/cover/'")


messages = ["Hidden 1", "Secret 2", "TopSecret 3"]

for i, msg in enumerate(messages):
    secret_img = lsb.hide(f"images/cover/cover_{i+1}.png", msg)
    secret_img.save(f"images/stego/stego_{i+1}.png")

print("✅ 3 stego images created in 'images/stego/' with hidden text!")
