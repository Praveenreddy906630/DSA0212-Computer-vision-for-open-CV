import cv2
import numpy as np

# Load the image
img = cv2.imread('21.jpeg', cv2.IMREAD_GRAYSCALE)

# Define Sobel kernels
kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

# Calculate gradients
grad_x = cv2.filter2D(img, cv2.CV_64F, kernel_x)
grad_y = cv2.filter2D(img, cv2.CV_64F, kernel_y)

# Compute Gradient Magnitude
magnitude = cv2.magnitude(grad_x, grad_y)
magnitude = np.uint8(np.clip(magnitude, 0, 255))

# Sharpen: Original + Mask
sharpened = cv2.add(img, magnitude)

# Display results
cv2.imshow('Original', img)
cv2.imshow('Gradient Mask', magnitude)
cv2.imshow('Sharpened Image', sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
