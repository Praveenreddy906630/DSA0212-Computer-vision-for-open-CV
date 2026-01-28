import cv2
import numpy as np

# Load the image
img = cv2.imread('lab.png', cv2.IMREAD_GRAYSCALE)

# Create a 9x9 kernel (larger kernels often yield better results for Top Hat)
kernel = np.ones((9, 9), np.uint8)

# Perform Top Hat transformation
# It is the difference between the input image and its Opening.
# It extracts objects that are brighter than the background.
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Display results
cv2.imshow('Original', img)
cv2.imshow('Top Hat', tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()
