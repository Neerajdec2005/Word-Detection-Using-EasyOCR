import cv2
import easyocr
reader = easyocr.Reader(['en'])

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    cv2.imshow('Press SPACE to capture', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break
    elif key == 32:
        results = reader.readtext(frame)
        for (bbox, text, prob) in results:
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = tuple(map(int, top_left))
            bottom_right = tuple(map(int, bottom_right))
            cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
            cv2.putText(frame, text, (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.imshow('Detected Text', frame)
        cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()