import cv2
import numpy as np

# Load the image
img = cv2.imread('lab.png', cv2.IMREAD_GRAYSCALE)

# Create a 5x5 kernel of ones
kernel = np.ones((5, 5), np.uint8)

# Perform Opening
# Opening is Erosion followed by Dilation. It is useful for removing noise.
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Display results
cv2.imshow('Original', img)
cv2.imshow('Opening', opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
