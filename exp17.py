import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('17.jpeg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define Laplacian mask with diagonal neighbors (negative center)
# As shown in image_0f64aa.png: [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
kernel = np.array([[1, 1, 1], 
                   [1, -8, 1], 
                   [1, 1, 1]])

# Apply the filter
laplacian = cv2.filter2D(image_rgb, -1, kernel)

# Sharpening: Original Image - Laplacian (since center coefficient is negative)
sharpened = cv2.subtract(image_rgb, laplacian)

# Display results
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Sharpened (Diagonal Neighbors Mask)')
plt.imshow(sharpened)
plt.axis('off')

plt.show()
