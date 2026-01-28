import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('lab.PNG')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get dimensions
height, width = image.shape[:2]

# Scale to Bigger size (2x)
bigger = cv2.resize(image_rgb, (width * 2, height * 2), interpolation=cv2.INTER_CUBIC)

# Scale to Smaller size (0.5x)
smaller = cv2.resize(image_rgb, (int(width * 0.5), int(height * 0.5)), interpolation=cv2.INTER_AREA)

# Display the results
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title(f'Original\n{width}x{height}')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title(f'Bigger (2x)\n{width*2}x{height*2}')
plt.imshow(bigger)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title(f'Smaller (0.5x)\n{int(width*0.5)}x{int(height*0.5)}')
plt.imshow(smaller)
plt.axis('off')

plt.tight_layout()
plt.show()
