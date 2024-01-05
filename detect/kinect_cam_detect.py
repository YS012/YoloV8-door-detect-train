import cv2
from ultralytics import YOLO
import numpy as np
from pykinect2 import PyKinectRuntime, PyKinectV2

# Load the YOLOv8 model
model = YOLO('../weights/yolov8n-pose.pt')

# Open the video file
kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth | PyKinectV2.FrameSourceTypes_Color)

iter_model = iter(model.track(source=1, show=False, stream=True))

while 1:
    result = next(iter_model)
    key = result.keypoints

