import os
from stegano import lsb

for file in os.listdir("images/stego"):
    path = os.path.join("images/stego", file)
    secret = lsb.reveal(path)
    print(f"{file} → Hidden message: {secret}")
