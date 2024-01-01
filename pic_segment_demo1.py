from PIL import Image
from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')  # load an official model

# Predict with the model
results = model('bus.png')  # predict on an image

# View results
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('results.jpg')  # save image