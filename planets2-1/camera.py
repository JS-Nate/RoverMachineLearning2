import cv2

for i in range(10):  # Check camera indices from 0 to 9
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera is accessible at index: {i}")
        cap.release()
        break
else:
    print("No camera found.")
