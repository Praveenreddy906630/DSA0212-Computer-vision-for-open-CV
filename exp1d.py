
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. RECTIFICATION: Check if file exists and use correct filename
file_path = '1D.JPEG'

if not os.path.exists(file_path):
    print(f"Error: The file {file_path} was not found in the directory.")
else:
    image = cv2.imread(file_path)

    if image is None:
        print("Error: Image could not be decoded. Check file integrity.")
    else:
        # 2. Convert BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 3. Define kernel and Dilate
        kernel = np.ones((5, 5), np.uint8)
        dilated_image = cv2.dilate(image_rgb, kernel, iterations=1)

        # 4. Display
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.title('Original')
        plt.imshow(image_rgb)
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.title('Dilated')
        plt.imshow(dilated_image)
        plt.axis('off')
        plt.show()
