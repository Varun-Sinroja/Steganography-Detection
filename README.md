# Steganography Detection Tool (ML-Based)

This project demonstrates a simple **steganography detection pipeline** using Python and machine learning.  
It generates cover and stego images, extracts statistical features from them, and trains classifiers to detect whether an image contains hidden data.

---

## 🚀 Features

- Generate synthetic **cover** and **stego** images using LSB steganography.
- Verify that hidden messages are correctly embedded.
- Extract numerical features from images:
  - 256-bin grayscale histogram
  - Noise residual variance
  - LSB bit-plane statistics (mean & standard deviation)
- Train and evaluate ML models (Random Forest and SVM) to classify:
  - `0` → cover image
  - `1` → stego image
- Save the best model for later use (`stego_model.pkl`).

---

## 🗂 Project Structure

```text
.
├── images/                     # Folder for cover & stego images (initially empty)
├── example_1_setup.py          # Tests Pillow, NumPy, and OpenCV
├── example_2_generate_stego.py # Generates cover & stego images
├── example_3_verify_stego.py   # Reads hidden messages from stego images
├── example_3_dataset_structure.txt # Notes about the dataset (optional)
├── example_4_extract_features.py   # Extracts features and saves CSV
├── example_5_train_model.py        # Trains ML models (RF & SVM)
└── README.md

