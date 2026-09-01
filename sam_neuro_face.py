import cv2
import numpy as np
import os
import sys

# ============================================
# Model Files
# ============================================
MODEL_FILE = "res10_300x300_ssd_iter_140000.caffemodel"
PROTO_FILE = "deploy.prototxt"

# ============================================
# Check if files exist
# ============================================
if not os.path.exists(MODEL_FILE):
    print(f"❌ Model file not found: {MODEL_FILE}")
    sys.exit()

if not os.path.exists(PROTO_FILE):
    print(f"❌ Prototxt file not found: {PROTO_FILE}")
    sys.exit()

print("✅ Model File :", os.path.abspath(MODEL_FILE))
print("✅ Proto File :", os.path.abspath(PROTO_FILE))

print(f"Model Size : {os.path.getsize(MODEL_FILE)/1024/1024:.2f} MB")
print(f"Proto Size : {os.path.getsize(PROTO_FILE)/1024:.2f} KB")

# ============================================
# Load Neural Network
# ============================================
try:
    net = cv2.dnn.readNetFromCaffe(PROTO_FILE, MODEL_FILE)
    print("✅ Neural network loaded successfully.")
except Exception as e:
    print("❌ Failed to load model.")
    print(e)
    sys.exit()

# ============================================
# Start Webcam
# ============================================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Could not open webcam.")
    sys.exit()

print("📷 Press Q to quit")

while True:

    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to capture frame.")
        break

    h, w = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(
        frame,
        scalefactor=1.0,
        size=(300, 300),
        mean=(104.0, 177.0, 123.0),
        swapRB=False,
        crop=False
    )

    net.setInput(blob)

    try:
        detections = net.forward()
    except Exception as e:
        print("❌ Error during forward pass.")
        print(e)
        break

    for i in range(detections.shape[2]):

        confidence = detections[0, 0, i, 2]

        if confidence > 0.6:

            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])

            startX, startY, endX, endY = box.astype(int)

            startX = max(0, startX)
            startY = max(0, startY)
            endX = min(w - 1, endX)
            endY = min(h - 1, endY)

            cv2.rectangle(
                frame,
                (startX, startY),
                (endX, endY),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"{confidence*100:.1f}%",
                (startX, startY - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    cv2.imshow("Live Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()