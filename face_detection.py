import numpy as np
import face_detection as fr
import cv2

video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    # capture frame by frame
    ret, frame = video_capture.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # To display multiple frames
    # - cv2.imshow('frame2', frame)
    # - cv2.imshow('frame3', frame)
    # - cv2.imshow('frame4', frame)

    # Display grayscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
