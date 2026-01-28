import cv2
import os

# 1. Check if file exists to avoid NoneType error
file_path = 'lab.png'

if not os.path.exists(file_path):
    print(f"Error: The file '{file_path}' was not found in the current directory.")
else:
    img = cv2.imread(file_path)

    # 2. Perform Cropping (ROI)
    # y:y+h, x:x+w
    roi = img[620:740, 155:305] 

    # 3. Copying
    cp_roi = roi.copy()

    # 4. Pasting inside another area
    img[485:605, 435:585] = cp_roi

    # Display result
    cv2.imshow('Result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
