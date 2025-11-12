import cv2
import ultralytics
from ultralytics import YOLO
#YOLO for object detection
model=YOLO("yolo11n.pt")
cap = cv2.VideoCapture(0)

try:
    while True:
        success, frame = cap.read()
        if not success:
            print("Failed to capture frame")
            break
        frame = cv2.flip(frame, 1)  # Flip horizontally

        results = model(frame)
        annotated_frame = results[0].plot()

        cv2.imshow("OBJECT", annotated_frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
