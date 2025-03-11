#including libraries 
import numpy as np
import cv2 as cv

#including default camera
cap=cv.VideoCapture(0)

#including file
face_cascade=cv.CascadeClassifier(r"C:\Users\ANIKET KUMAR\OneDrive\Desktop\AI Project\haarcascade_frontalface_default.xml")

#checking file is loaded or not
if face_cascade.empty():
    print("file is not loaded...")
    exit()

#capture the device widthxheight
frame_width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

#checking the camera
if cap.isOpened() is not True:
    print("Something went Wrong...")
    exit()
    
#capture the camera and performe the operations
while cap.isOpened():
    ret,frame=cap.read()
    if ret is True:
        frame=cv.resize(frame,(frame_width,frame_height))
        gray_img=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray_img,1.1,8)
        
        for (x,y,w,h) in faces:
            cv.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),1)
            
        cv.imshow('frames',frame)
        
        if cv.waitKey(1) & 0xff==ord('q'):
            break
    else:
        print("Failed to capture the frame...")
        break
    
#release the camera of device
cap.release()
cv.destroyAllWindows()