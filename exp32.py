import cv2

# Load the video file
cap = cv2.VideoCapture('32.mp4')

# Get total number of frames
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# Start from the last frame index
frame_index = frames - 1

while frame_index >= 0:
    # Set the current frame position
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    
    # Read the frame
    ret, frame = cap.read()
    
    if ret:
        cv2.imshow('Video in Reverse', frame)
        
        # Decrement frame index to move backward
        frame_index -= 1
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
