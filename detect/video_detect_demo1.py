import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('../weights/yolov8n.pt')

# Open the video file
video_path = ""
cap = cv2.VideoCapture(video_path)

# 定义跳帧数
frame_skip = 5  # 跳过的帧数
# 初始化当前帧
current_frame = 0

# Loop through the video frames
while cap.isOpened():
    
    cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)

    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Resize the annotated frame to fit the screen
        resized_frame = cv2.resize(annotated_frame, (1280, 720))  # Adjust the dimensions as needed

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", resized_frame)

        # 仅处理和显示跳帧后的帧
        current_frame += frame_skip

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break
    
# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()