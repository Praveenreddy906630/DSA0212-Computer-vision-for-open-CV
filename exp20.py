import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('20.jpeg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define High-boost mask parameters
# As per image_0f6c0f.png, A >= 1. 
# If A = 1.5, center becomes A + 4 = 5.5 (for the 4-neighbor version)
A = 1.5
kernel_high_boost = np.array([[0, -1, 0], 
                             [-1, A + 4, -1], 
                             [0, -1, 0]])

# Apply the High-boost filter
high_boost_result = cv2.filter2D(image_rgb, -1, kernel_high_boost)

# Display the results
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title(f'High-Boost Sharpening (A={A})')
plt.imshow(high_boost_result)
plt.axis('off')

plt.show()
