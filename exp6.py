
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('lab.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width = image_rgb.shape[:2]

# Define translation distances (tx, ty)
# tx = pixels to move right, ty = pixels to move down
tx, ty = 100, 50

# Create the translation matrix
# T = [[1, 0, tx], [0, 1, ty]]
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# Move the image using warpAffine
moved_image = cv2.warpAffine(image_rgb, translation_matrix, (width, height))

# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Position')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title(f'Moved (Right: {tx}, Down: {ty})')
plt.imshow(moved_image)
plt.axis('off')

plt.show()
