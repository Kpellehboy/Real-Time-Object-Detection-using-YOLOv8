from ultralytics import YOLO
import cv2

# 1. Load the YOLOv8 model (it will download automatically on first run)
# 'yolov8n.pt' is the "nano" version - very fast for laptops
model = YOLO("yolov8n.pt") 

# 2. Initialize Video Stream (OpenCV built-in)
cap = cv2.VideoCapture(0)

print("[INFO] starting YOLO video stream... Press 'q' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # 3. Run YOLO detection on the frame
    # This replaces the 'blob', 'net.forward', and 'for loop' from your old code
    results = model(
        source=frame, 
        stream=True, 
        conf=0.25,    # Standard threshold (0.5 is often too strict)
        iou=0.45,     # Helps separate overlapping objects (like people in a crowd)
        imgsz=640,    # Default COCO size; increasing to 1280 improves small object detection
        classes=None  # Ensuring all 80 classes are active (None = all)
    )

    # 4. Visualize the results
    annotated_frame = frame
    for r in results:
        annotated_frame = r.plot() # Automatically draws boxes and labels

    # Show the output
    cv2.imshow("YOLOv8 Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()