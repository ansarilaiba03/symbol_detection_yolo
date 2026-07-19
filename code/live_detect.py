import cv2
from ultralytics import YOLO

# Load trained YOLO model
model = YOLO("../model/best.pt")   # make sure best.pt is in same folder

# Connect to phone camera
#cap = cv2.VideoCapture("http://192.0.0.2:4747/mjpeg")

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera stream")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Run YOLO detection
    results = model(frame, conf=0.5)

    # Draw results on frame
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("YOLO Real vs Fake Detection", annotated_frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




