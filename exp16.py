import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('16.jpeg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define Laplacian mask with negative center coefficient as shown in image_0f6143.png
# Kernel: [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
kernel = np.array([[0, 1, 0], 
                   [1, -4, 1], 
                   [0, 1, 0]])

# Apply the Laplacian filter
laplacian = cv2.filter2D(image_rgb, -1, kernel)

# Sharpening: Original Image - Laplacian (since center is negative)
sharpened = cv2.subtract(image_rgb, laplacian)

# Display the original and sharpened images
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Sharpened Image (Negative Center Laplacian)')
plt.imshow(sharpened)
plt.axis('off')

plt.show()
