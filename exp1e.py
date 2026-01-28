import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('1E.JPEG')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the kernel for erosion
kernel = np.ones((5, 5), np.uint8)

# Erode the image
eroded_image = cv2.erode(image_rgb, kernel, iterations=1)

# Display results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Eroded Image')
plt.imshow(eroded_image)
plt.axis('off')

plt.show()
