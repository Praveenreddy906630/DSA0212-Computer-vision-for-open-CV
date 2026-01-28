
import cv2
import numpy as np

# Load the image
img = cv2.imread('lab.png', cv2.IMREAD_GRAYSCALE)

# Create a 5x5 kernel of ones
kernel = np.ones((5, 5), np.uint8)

# Perform Morphological Gradient
# This is the difference between dilation and erosion of an image.
# It results in the outline (boundary) of the objects.
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Display results
cv2.imshow('Original', img)
cv2.imshow('Morphological Gradient', gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
