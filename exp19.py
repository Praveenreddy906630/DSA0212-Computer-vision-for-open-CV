import cv2
import numpy as np

def unsharp_masking(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Could not load image.")
        return

    # Step 1: Create a blurred version of the image
    # Using Gaussian Blur as the blurred image f_bar(x, y)
    blurred = cv2.GaussianBlur(image, (5, 5), 1.0)
    
    # Step 2: Calculate the mask (Unsharp Mask)
    # Formula: fs(x, y) = f(x, y) - f_bar(x, y)
    mask = cv2.subtract(image, blurred)
    
    # Step 3: Add the mask back to the original image to sharpen
    # sharpened = original + mask
    sharpened = cv2.add(image, mask)
    
    # Display the results
    cv2.imshow('Original Image', image)
    cv2.imshow('Unsharp Mask (Edges)', mask)
    cv2.imshow('Sharpened Image', sharpened)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Usage
unsharp_masking('19.jpeg')
