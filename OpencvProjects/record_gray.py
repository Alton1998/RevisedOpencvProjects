import numpy as np
import cv2
import os
filename='video_gray.avi'
frames_per_seconds=24.0
res='720p'
VIDEO_TYPE={
    'avi':
    cv2.VideoWriter_fourcc(*'XVID'),
    'mp4':cv2.VideoWriter_fourcc(*'XVID'),
}

STD_DIMENSIONS={
    "480p":(640,480),
    "720p":(1280,720),
    "1080p":(1920,1080),
    "4k":(3840,216)
}

def get_video_type(filename):
    filename,ext=os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']

def set_res(cap,width,height):
    cap.set(3,width)
    cap.set(4,height)

def get_dims(cap,res='1080p'):
    width,height=STD_DIMENSIONS['480p']
    if res in STD_DIMENSIONS:
        width,height=STD_DIMENSIONS[res]
        set_res(cap,width,height)
        return width,height

cap=cv2.VideoCapture(0)
dims=get_dims(cap,res)
out = cv2.VideoWriter(filename, get_video_type(filename), frames_per_seconds, get_dims(cap, res))
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(gray)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()