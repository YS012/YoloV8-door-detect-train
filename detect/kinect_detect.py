import cv2
from ultralytics import YOLO
import numpy as np
from pykinect2 import PyKinectRuntime, PyKinectV2

# Load the YOLOv8 model
model = YOLO('../weights/yolov8n-pose.pt')

# Open the video file
kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth | PyKinectV2.FrameSourceTypes_Color)

# Loop through the video frames
while 1:
    if kinect.has_new_color_frame():
        frameC = kinect.get_last_color_frame()
        frameC = np.reshape(frameC, [1080, 1920, 4])[:, :, 0:3]
        # output = cv2.resize(frameC, (1280, 720))  # (1920, 1080)
        frame_depth = kinect.depth_frame_data
        result = next(model.track(frameC, stream=True))
        img = result.orig_img
        annotated_frame = result.plot()
        key_points_xy = result.keypoints.xy

        for point in key_points_xy[0]:
            # 在图片上绘制圆，参数依次为：图片、圆心坐标、半径、颜色、线宽（-1表q示填充）
            center = tuple(map(int, point))

            # if center != (0, 0):
            #     print('center', center, 'depth', frame_depth[center[1] * img.shape[1] + center[0]])
            cv2.circle(annotated_frame, center, 5, (0, 0, 0), -1)
        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    key = cv2.waitKey(1)

# Release the video capture object and close the display window

cv2.destroyAllWindows()
