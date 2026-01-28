import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('lab.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel Edge Detection along Y axis
# ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)

# Convert back to uint8 to display
sobely_8u = cv2.convertScaleAbs(sobely)

# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Sobel Y Edge Detection')
plt.imshow(sobely_8u, cmap='gray')
plt.axis('off')

plt.show()
