import cv2
import os


def extract_frames(video_path, output_folder):
    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # 每隔5秒（150帧）保存一帧图像
        if frame_count % 150 == 0:
            output_path = os.path.join(output_folder, f"{frame_count // 150 + 1:07d}.jpg")
            cv2.imwrite(output_path, frame)

        frame_count += 1

    cap.release()


# 设置输入视频文件夹和输出图像文件夹
input_folder = "C:\\Users\\Y\\Desktop"
output_folder = "C:\\Users\\Y\\Desktop\\images"

# 获取输入文件夹中的视频文件列表
video_files = [f for f in os.listdir(input_folder) if f.endswith(('.mp4', '.avi', '.mov'))]

# 逐个处理视频文件
for video_file in video_files:
    video_path = os.path.join(input_folder, video_file)
    extract_frames(video_path, output_folder)

print("截屏完成！")
