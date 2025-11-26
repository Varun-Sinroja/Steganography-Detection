import os
import numpy as np
import pandas as pd
from PIL import Image

def extract_features(image_path):
    img = Image.open(image_path).convert("L")
    arr = np.array(img)

    hist = np.histogram(arr, bins=256, range=(0, 255))[0]
    hist = hist / np.sum(hist)

    diff = np.diff(arr.astype(np.int16), axis=0)
    noise_var = np.var(diff)

    lsb_plane = arr & 1
    lsb_mean = np.mean(lsb_plane)
    lsb_std = np.std(lsb_plane)

    return np.concatenate([hist, [noise_var, lsb_mean, lsb_std]])


os.makedirs("images/cover", exist_ok=True)
os.makedirs("images/stego", exist_ok=True)

features = []
labels = []

for folder, label in [("images/cover", 0), ("images/stego", 1)]:
    for f in os.listdir(folder):
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
            path = os.path.join(folder, f)
            feat = extract_features(path)
            features.append(feat)
            labels.append(label)
            print(f"✅ Processed: {f} ({'cover' if label==0 else 'stego'})")

df = pd.DataFrame(features)
df["label"] = labels
df.to_csv("features_dataset.csv", index=False)

print("\n✅ Feature extraction complete!")
print(f"📄 Saved dataset as 'features_dataset.csv' with {len(df)} samples and {df.shape[1]-1} features.")
