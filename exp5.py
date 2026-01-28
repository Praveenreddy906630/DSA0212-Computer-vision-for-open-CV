
import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('lab.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions and center
(h, w) = image_rgb.shape[:2]
center = (w // 2, h // 2)

# 1. Rotate Clockwise (90 degrees)
# Note: cv2.getRotationMatrix2D uses counter-clockwise as positive, 
# so -90 is clockwise.
matrix_cw = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated_cw = cv2.warpAffine(image_rgb, matrix_cw, (w, h))

# 2. Rotate Counter-Clockwise (90 degrees)
matrix_ccw = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated_ccw = cv2.warpAffine(image_rgb, matrix_ccw, (w, h))

# Display the results
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('Original')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('90° Clockwise')
plt.imshow(rotated_cw)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('90° Counter-Clockwise')
plt.imshow(rotated_ccw)
plt.axis('off')

plt.show()
