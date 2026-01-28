import cv2
import numpy as np

def add_watermark(image_path, watermark_text):
    # Load the main image
    img = cv2.imread('lab.png')
    h, w = img.shape[:2]

    # Create a transparent overlay for the watermark
    overlay = img.copy()
    
    # Define font, scale, and thickness
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    color = (255, 255, 255) # White
    thickness = 5
    
    # Get text size to center it
    text_size = cv2.getTextSize(watermark_text, font, font_scale, thickness)[0]
    text_x = (w - text_size[0]) // 2
    text_y = (h + text_size[1]) // 2

    # Draw text on the overlay
    cv2.putText(overlay, watermark_text, (text_x, text_y), font, font_scale, color, thickness)

    # Blend the overlay with the original image (alpha = 0.7 original, beta = 0.3 watermark)
    alpha = 0.7
    result = cv2.addWeighted(overlay, 1 - alpha, img, alpha, 0)

    # Display results
    cv2.imshow('Watermarked Image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Usage
add_watermark('lab.png', 'CONFIDENTIAL')
