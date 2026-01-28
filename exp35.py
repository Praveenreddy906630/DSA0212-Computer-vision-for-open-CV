import cv2

# Load the image
img = cv2.imread('35.jpeg')

# Define the rectangle coordinates [y:y+h, x:x+w]
# Example: Extracting the face of Rohit Sharma based on the image
x, y, w, h = 250, 60, 200, 250

# 1. Draw the Rectangular shape on the original image
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 2. Extract the object (Crop the region)
extracted_object = img[y:y+h, x:x+w]

# Display results
cv2.imshow('Rectangle on Image', img)
cv2.imshow('Extracted Object', extracted_object)

cv2.waitKey(0)
cv2.destroyAllWindows()
