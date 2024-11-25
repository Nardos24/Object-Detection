
# Import required libraries
from ultralytics import YOLO
import cv2

# use YOLO pre-trained model
model = YOLO("yolo1n.pt")  


cap = cv2.VideoCapture(0)  # initialize the webcam using opencv

# Loop to perform real-time object detection
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame from webcam.")
        break
    
    # Perform object detection on the current frame
    results = model(frame, verbose=False)
    
    
    annotated_frame = results[0].plot()  # Plot detections on the frame

    # Display the frame
    cv2.imshow('YOLO11 Object Detection', annotated_frame)

    # Break the loop if 's' is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break


cap.release()
cv2.destroyAllWindows()