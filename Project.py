#including libraries 
import numpy as np
import cv2 as cv

#including default camera
cap=cv.VideoCapture(0)

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
        cv.imshow('frames',frame)
        if cv.waitKey(1) & 0xff==ord('q'):
            break
    else:
        print("Failed to capture the frame...")
        break
    
#release the camera of device
cap.release()
cv.destroyAllWindows()