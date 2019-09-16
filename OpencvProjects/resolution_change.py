import numpy as np
import cv2

cap=cv2.VideoCapture(0)
def set_res(cap,width,height):
    cap.set(3,width)
    cap.set(4,height)
def rescale_frame(frame,percent):
    width=int(frame.shape[1]*percent/100)
    height=int(frame.shape[1]*percent/100)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
set_res(cap,1920,1080)
while True:
    ret,frame=cap.read()
    frame=rescale_frame(frame,100)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()