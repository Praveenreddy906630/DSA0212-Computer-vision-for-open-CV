import cv2
import numpy as np

# Load the existing video file
cap = cv2.VideoCapture('34.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]

    # Define source points (the area to be transformed)
    # These coordinates select a trapezoid in the original frame
    pts1 = np.float32([[150, 150], [width - 150, 150], 
                       [50, height - 50], [width - 50, height - 50]])

    # Define destination points (mapping to a full rectangular view)
    pts2 = np.float32([[0, 0], [width, 0], 
                       [0, height], [width, height]])

    # Generate the Perspective Transformation matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply the transformation to the frame
    transformed_frame = cv2.warpPerspective(frame, matrix, (width, height))

    # Display results
    cv2.imshow('Original Video', frame)
    cv2.imshow('Perspective Transformation', transformed_frame)

    # Press 'q' to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
