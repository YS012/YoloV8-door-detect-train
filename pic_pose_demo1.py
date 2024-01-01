from PIL import Image
import supervision as sv
import cv2
from ultralytics import YOLO

model = YOLO('yolov8n-pose.pt')  # load an official model

img = cv2.imread('1.png')
# Predict with the model
results = model.track('1.png')[0]  # predict on an image
detections = sv.Detections.from_ultralytics(results)

bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()
labels = [
    results.names[class_id]
    for class_id
    in detections.class_id
]
labels = [f"aaa" for _ in detections]
annotated_image = bounding_box_annotator.annotate(scene=img, detections=detections)
annotated_image = label_annotator.annotate(scene=img, detections=detections, labels=labels)
sv.plot_image(annotated_image)


# # View results
#
# im_array = results[0].plot()  # plot a BGR numpy array of predictions
# im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
# im.show()  # show image
# im.save('results.jpg')  # save image
