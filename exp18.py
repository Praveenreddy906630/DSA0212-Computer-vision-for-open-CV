import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('18.jpeg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define Laplacian mask with positive center coefficient as shown in image_0f682b.png
# Kernel: [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
# This mask combines the identity and the negative Laplacian for one-step sharpening
kernel = np.array([[0, -1, 0], 
                   [-1, 5, -1], 
                   [0, -1, 0]])

# Apply the filter
# Since the center is positive and includes the original pixel weight (5), 
# this directly produces the sharpened image.
sharpened = cv2.filter2D(image_rgb, -1, kernel)

# Display results
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Sharpened (Positive Center Laplacian)')
plt.imshow(sharpened)
plt.axis('off')

plt.show()
