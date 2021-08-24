import os
import cv2

# ffmpeg is a better recorder for videos

filename = 'video.mp4'  # types of video file type include: .avi, .mp4
frames_per_second = 10.0  # 24.0 is the standard for movies
my_res = '720p'  # 1080p

# set resolution for the video capture
def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

# Standard Video Dimensions Sizes
STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080": (1920, 1080),
    "4k": (3840, 2160)
}


def get_dims(video_cap, video_res='1080p'):
    width, height = STD_DIMENSIONS['480p']
    if video_res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[video_res]
    change_res(video_cap, width, height)
    return width, height

# Video Encoding, might require additional installs
# Types of Codes: https://www.fourcc.org/codecs.php
VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID')
}


def get_video_type(video_filename):
    video_filename, ext = os.path.splitext(video_filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
dims = get_dims(video_cap=cap, video_res=my_res)
video_type_cv2 = get_video_type(video_filename=filename)

out = cv2.VideoWriter(filename, video_type_cv2, frames_per_second, dims)  # width, height

while True:
    # capture frame-by-frame
    ret, frame = cap.read()

    out.write(frame)

    # display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
