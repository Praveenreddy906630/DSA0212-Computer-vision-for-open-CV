import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('lab.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Source points
pts_src = np.array([[50, 50], [200, 50], [50, 200], [200, 200]], dtype=float)

# Destination points
pts_dst = np.array([[10, 100], [210, 40], [60, 250], [240, 220]], dtype=float)

def calculate_dlt(src, dst):
    A = []
    for i in range(len(src)):
        x, y = src[i][0], src[i][1]
        u, v = dst[i][0], dst[i][1]
        A.append([-x, -y, -1, 0, 0, 0, x*u, y*u, u])
        A.append([0, 0, 0, -x, -y, -1, x*v, y*v, v])
    
    A = np.array(A)
    # Singular Value Decomposition (SVD)
    U, S, Vh = np.linalg.svd(A)
    # The solution is the last row of Vh (or last column of V)
    H = Vh[-1, :].reshape(3, 3)
    # Normalize the matrix
    return H / H[2, 2]

# Compute Homography using DLT
H_dlt = calculate_dlt(pts_src, pts_dst)

# Apply transformation
rows, cols, ch = image_rgb.shape
dlt_output = cv2.warpPerspective(image_rgb, H_dlt, (cols, rows))

# Display results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('DLT Transformation')
plt.imshow(dlt_output)
plt.axis('off')

plt.show()
