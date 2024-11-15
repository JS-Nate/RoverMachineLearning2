from ultralytics import YOLO
model = YOLO("yolo11m.pt")
model.train(data="data.yaml", imgsz=640, batch=8, epochs=100, workers=1, device="gpu")