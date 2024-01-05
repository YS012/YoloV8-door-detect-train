import cv2


def get_camera_list():
    # 从 0 开始逐个尝试打开摄像头设备
    index = 0
    camera_list = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.isOpened():
            break
        else:
            camera_list.append(f"Camera {index}")
            cap.release()
        index += 1

    return camera_list


# 获取摄像头设备列表
cameras = get_camera_list()
if cameras:
    print("Detected cameras:")
    for camera in cameras:
        print(camera)
else:
    print("No cameras detected.")
