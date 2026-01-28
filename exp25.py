import cv2
import numpy as np

# Load the image
img = cv2.imread('lab.png', cv2.IMREAD_GRAYSCALE)

# Create a 5x5 kernel of ones
kernel = np.ones((5, 5), np.uint8)

# Perform Dilation
# Dilation adds pixels to the boundaries of objects in an image
dilation = cv2.dilate(img, kernel, iterations=1)

# Display results
cv2.imshow('Original', img)
cv2.imshow('Dilation', dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
