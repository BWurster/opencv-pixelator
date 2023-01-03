import numpy as np
import cv2 as cv

PIXEL_SIZE = 20

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    for i in range(0, frame.shape[0], PIXEL_SIZE):
        for j in range(0, frame.shape[1], PIXEL_SIZE):
            mean = np.mean(frame[i:i+PIXEL_SIZE, j:j+PIXEL_SIZE], (0,1))
            cv.rectangle(frame, (j,i), (j+PIXEL_SIZE, i+PIXEL_SIZE), (int(mean[0]), int(mean[1]), int(mean[2])), -1)

    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()