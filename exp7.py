
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('lab.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

rows, cols, ch = image_rgb.shape

# Define three points in the original image
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Define where those three points should be in the output image
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Get the Affine Transformation Matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply the transformation
dst = cv2.warpAffine(image_rgb, M, (cols, rows))

# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Affine Transformation')
plt.imshow(dst)
plt.axis('off')

plt.show()
