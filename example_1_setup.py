from PIL import Image
import cv2
import numpy as np

print("✅ Libraries imported successfully!")

img_array = np.zeros((100, 100, 3), dtype=np.uint8)
img_array[:] = [0, 255, 0]  # Green square

img = Image.fromarray(img_array)
img.save("test_image.png")
print("✅ Created and saved 'test_image.png' successfully.")
img_cv = cv2.imread("test_image.png")
print(f"✅ OpenCV loaded image shape: {img_cv.shape}")
