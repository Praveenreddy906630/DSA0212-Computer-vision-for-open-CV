import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('lab.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

rows, cols, ch = image_rgb.shape

# Define four corners in the original image
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])

# Define where those four corners should map to in the output (rectifying)
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# Get the Perspective Transformation Matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply the transformation (using a 300x300 output window)
dst = cv2.warpPerspective(image_rgb, M, (300, 300))

# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Perspective Transformation')
plt.imshow(dst)
plt.axis('off')

plt.show()
