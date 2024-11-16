import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("C:/Users/natt4/OneDrive/Documents/GitHub/RoverMachineLearning2/planets2-1/runs/detect/train/weights/best.pt")

# Try different camera indices
camera_index = 0  # Start with the default camera
cap = cv2.VideoCapture(camera_index)

# Check if the camera opened successfully
if not cap.isOpened():
    print(f"Camera with index {camera_index} could not be opened.")
    for i in range(10):  # Check indices from 0 to 9
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            camera_index = i
            print(f"Using camera index {camera_index}")
            break

if not cap.isOpened():
    print("No cameras found.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Perform detection on the frame
    results = model.predict(frame)

    # Annotate frame with detection results
    annotated_frame = results[0].plot()

    # Display the annotated frame in a window
    cv2.imshow('Detections', annotated_frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

print("Processing complete.")
