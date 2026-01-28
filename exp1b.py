import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('1B.JPEG')

# Convert BGR to RGB for correct display in Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Apply Gaussian Blur
# ksize (7, 7) must be odd, sigmaX = 0
blurred_image = cv2.GaussianBlur(image_rgb, (7, 7), 0)

# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Gaussian Blur')
plt.imshow(blurred_image)
plt.axis('off')

plt.savefig('blurred_output.png')
plt.show()
