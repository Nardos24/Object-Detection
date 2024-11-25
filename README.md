# Real-Time Object Detection with YOLO

This project implements real-time object detection using the YOLO (You Only Look Once) model. The implementation utilizes the Ultralytics YOLO library and OpenCV to capture video from a webcam and display detected objects in real-time.
## Requirements

• **Python:** 3.7 or higher
• **Ultralytics YOLO:** 
Install using `pip install ultralytics`
• **OpenCV:** 
Install using `pip install opencv-python`
## Setup

 **Clone the repository:**
  
bash
  git clone https://github.com/Nardos24/Real-Time-Object-Detection-with-YOLO.git
 ## Usage

1. Run the script: Execute the Python script main.py.
2. Object Detection: The webcam feed will be displayed with detected objects highlighted by bounding boxes and labels.
3. Stop the script: Press the 's' key to stop the program.


## Model Selection

This project uses yolov11n.pt by default, a smaller, faster model suitable for real-time applications. However, Ultralytics offers various YOLOv11 models with different size/speed/accuracy trade-offs. For more information and to explore other models, please refer to the Ultralytics YOLOv11 Model Documentation (https://docs.ultralytics.com/models/yolo11/#performance-metrics). You can easily switch models by changing the model path in the main.py file.
