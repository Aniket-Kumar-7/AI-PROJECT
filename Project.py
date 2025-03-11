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
        #convert image to gray 
        gray_img=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        #detect the faces
        faces=face_cascade.detectMultiScale(gray_img,1.1,7)
        
        for (x,y,w,h) in faces:
            #draw rectangle on faces
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
            #select the regeion of interest
            face_roi=frame[y:y+h,x:x+w]
            #convert hsv scale
            hsv=cv.cvtColor(face_roi,cv.COLOR_BGR2HSV)
            #range of reddish color
            lower_reddish_white1 = np.array([0, 0, 200])  
            upper_reddish_white1 = np.array([10, 50, 255]) 
            lower_reddish_white2 = np.array([160, 0, 200])  
            upper_reddish_white2 = np.array([180, 50, 255])
            #creating mask for color
            mask1 = cv.inRange(hsv, lower_reddish_white1, upper_reddish_white1)
            mask2 = cv.inRange(hsv, lower_reddish_white2, upper_reddish_white2)
            #creating white mask
            reddish_white_mask = cv.bitwise_or(mask1, mask2)
            
            contours,_=cv.findContours(reddish_white_mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
            
            for contour in contours:
                (center_x,center_y),radius=cv.minEnclosingCircle(contour)
                center=(int(center_x)+x,int(center_y)+y)
                radius=int(radius)
                if radius > 2:
                    cv.circle(frame,center,radius,(255,255,255),1)
                    
        cv.imshow('frames',frame)
        if cv.waitKey(1) & 0xff==ord('q'):
            break
    else:
        print("Failed to capture the frame...")
        break
    
#release the camera of device
cap.release()
cv.destroyAllWindows()