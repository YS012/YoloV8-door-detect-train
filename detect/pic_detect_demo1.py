import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('../weights/yolov8n.pt')

# Open the video file
video_path = "../data_test/VID_20210615_095517 - Trim.mp4"
results = iter(model.track(source=0, stream=True))

# Loop through the video frames
while 1:
    try:
        # Run YOLOv8 inference on the frame
        # Visualize the results on the frame
        result = next(results)
        annotated_frame = result.plot()
        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    except StopIteration:
        break

# Release the video capture object and close the display window

cv2.destroyAllWindows()
