import numpy as np
import cv2
import pickle
face_cascade=cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('train.yml')
labels={}
with open("labels.pickle",'rb') as f:
    og_labels=pickle.load(f)
    labels={v:k for k,v in og_labels.items()}
cap=cv2.VideoCapture(0)
print(cap)
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for(x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        _id,conf=recognizer.predict(roi_gray)
        if conf>45 and conf<85:
            print(_id)
            print(labels[_id])
            font=cv2.FONT_HERSHEY_SIMPLEX
            name=labels[_id]
            color=(0,255,0)
            stroke=3
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
        img_name='face.png'
        cv2.imwrite(img_name,roi_gray)
        color=(255,0,0)
        stroke=2
        end_cord_x=x+w
        end_cord_y=y+h
        cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()