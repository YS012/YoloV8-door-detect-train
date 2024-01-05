import cv2
import numpy as np
from pykinect2 import PyKinectRuntime, PyKinectV2

kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth | PyKinectV2.FrameSourceTypes_Color)

while 1:
    if kinect.has_new_color_frame():
        frameC = kinect.get_last_color_frame()
        frameC = np.reshape(frameC, [1080, 1920, 4])[:, :, 0:3]
        output = cv2.resize(frameC, (1280, 720))  # (1920, 1080)
        cv2.imshow('KINECT COLOR Video Stream', output)
        frameC = None
        if cv2.waitKey(1) & 0xFF == 27:
            break
    if kinect.has_new_depth_frame():
        frameD = kinect.get_last_depth_frame()
        frame_depth = kinect.depth_frame_data
        frameD = frameD.astype(np.uint8)
        frameD = np.reshape(frameD, (424, 512))
        output = cv2.cvtColor(frameD, cv2.COLOR_GRAY2BGR)


        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                print(x, y)
            if event == cv2.EVENT_RBUTTONDOWN:
                Pixel_Depth = frame_depth[((y * 512) + x)]
                print(Pixel_Depth)


        # output = cv2.bilateralFilter(output, 1, 150, 75)
        cv2.imshow('KINECT DEPTH Video Stream', output)
        cv2.setMouseCallback('KINECT DEPTH Video Stream', click_event)
        output = None
        if cv2.waitKey(1) & 0xFF == 27:
            break

    key = cv2.waitKey(1)
