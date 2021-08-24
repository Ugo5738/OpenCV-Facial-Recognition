import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)


def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)


def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)


def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)


def rescale_frame(input_frame, percent=75):
    scale_percent = 75
    width = int(input_frame.shape[1] * scale_percent/100)
    height = int(input_frame.shape[0] * scale_percent/100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


#

# To rescale:
# make_1080p()

# To change it to a custom scale:
# change_res(4000, 2000)

while True:
    # capture frame by frame
    ret, frame = cap.read()

    # to rescale the frame
    frame = rescale_frame(frame, percent=70)

    # Display the resulting
    cv2.imshow('frame', frame)

    frame2 = rescale_frame(frame, percent=140)
    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray_frame2', gray)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
