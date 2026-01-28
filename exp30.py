import cv2
import numpy as np

# Load the image
img = cv2.imread('lab.png', cv2.IMREAD_GRAYSCALE)

# Create a 9x9 kernel
kernel = np.ones((9, 9), np.uint8)

# Perform Black Hat transformation
# It is the difference between the Closing of the image and the input image.
# It extracts objects that are darker than the background.
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# Display results
cv2.imshow('Original', img)
cv2.imshow('Black Hat', blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
