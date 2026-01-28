import cv2
import numpy as np

# Load the image
img = cv2.imread('lab.png', cv2.IMREAD_GRAYSCALE)

# Create a 5x5 kernel of ones
kernel = np.ones((5, 5), np.uint8)

# Perform Closing
# Closing is Dilation followed by Erosion. It is useful for filling small holes.
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Display results
cv2.imshow('Original', img)
cv2.imshow('Closing', closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
