from ultralytics import YOLO


def train_img():
    # Load a model
    model = YOLO('yolov8n-pose.pt')  # load a pretrained model (recommended for training)

    # Train the model
    results = model.train(data='test_pos.yaml', epochs=300, batch=64, imgsz=640)


if __name__ == '__main__':
    train_img()
