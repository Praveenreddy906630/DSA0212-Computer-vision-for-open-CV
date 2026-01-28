
import cv2

# Load the image
img = cv2.imread('31.jpeg')

if img is None:
    print("Error: Could not load image.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Initialize ORB detector correctly
    orb = cv2.ORB_create(nfeatures=1000)

    # Find the keypoints and descriptors
    keypoints, descriptors = orb.detectAndCompute(gray, None)

    # Draw keypoints on the watch
    result = cv2.drawKeypoints(img, keypoints, None, color=(0, 255, 0), flags=0)

    # Display result
    cv2.imshow("Watch Feature Recognition", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
