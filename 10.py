import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('lab.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define four source points (from the original image)
# Format: [x, y]
pts_src = np.array([[141, 131], [480, 159], [493, 630],[64, 601]])

# Define four destination points (where you want them to move)
pts_dst = np.array([[318, 256], [534, 372], [316, 670], [73, 473]])

# Calculate Homography Matrix
h, status = cv2.findHomography(pts_src, pts_dst)

# Warp source image to destination based on homography
im_out = cv2.warpPerspective(image_rgb, h, (image_rgb.shape[1], image_rgb.shape[0]))

# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Homography Transformation')
plt.imshow(im_out)
plt.axis('off')

plt.show()
