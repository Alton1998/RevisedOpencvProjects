import numpy as np
import cv2
from utils import CFEVideoConf,image_resize
filename='watermark.mp4'
frames_per_seconds=24.0
cap=cv2.VideoCapture(0)
config=CFEVideoConf(cap,filepath=filename,res='720p')
out=cv2.VideoWriter(filename,config.video_type,frames_per_seconds,config.dims)
watermark='Marketing-Communications-Logo-1.png'
image=cv2.imread(watermark,-1)
image=image_resize(image,100,100)
cv2.imshow('watermark',image)
while True:
    ret,frame=cap.read()
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()