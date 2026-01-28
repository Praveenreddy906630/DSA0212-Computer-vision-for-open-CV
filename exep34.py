import cv2
import numpy as np

# Load your video
cap = cv2.VideoCapture('34.mp4')

# Create the Background Subtractor object
# MOG2 is a Gaussian Mixture-based Background/Foreground Segmentation Algorithm
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 1. Apply Background Subtraction to get the foreground mask
    fgmask = fgbg.apply(frame)

    # 2. Clean the mask using Morphological Opening (remove noise)
    kernel = np.ones((5,5), np.uint8)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    
    # 3. Find contours (shapes) of the moving objects
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        # Filter by area to ignore small noise and keep only car-sized objects
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            # Draw the bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Vehicle", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display results
    cv2.imshow('Vehicle Detection (No XML)', frame)
    cv2.imshow('Foreground Mask', fgmask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
