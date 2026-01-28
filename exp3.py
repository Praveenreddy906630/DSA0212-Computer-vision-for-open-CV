import cv2

# Read the captured video
cap = cv2.VideoCapture('34.mp4')

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get the original frame rate
fps = cap.get(cv2.CAP_PROP_FPS)
# Calculate delay for normal motion (in milliseconds)
normal_delay = int(1000 / fps)

# Define speed factors
# Higher delay = slower motion; Lower delay = faster motion
slow_motion_delay = normal_delay * 3
fast_motion_delay = max(1, int(normal_delay / 3))

print("Controls: 'n' for Normal, 's' for Slow, 'f' for Fast, 'q' to Quit")
current_delay = normal_delay

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        # Restart video when it ends
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    cv2.imshow('Video Processing', frame)

    key = cv2.waitKey(current_delay) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord('s'):
        current_delay = slow_motion_delay
        print("Mode: Slow Motion")
    elif key == ord('f'):
        current_delay = fast_motion_delay
        print("Mode: Fast Motion")
    elif key == ord('n'):
        current_delay = normal_delay
        print("Mode: Normal Motion")

cap.release()
cv2.destroyAllWindows()
