import numpy as np
import cv2
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
fullbody_cascade = cv2.CascadeClassifier('../data/haarcascade_fullbody.xml')
boob_cascade = cv2.CascadeClassifier('../data/cascade.xml')
img = cv2.imread('/home/siadmin/Downloads/black-and-red-iphone-7.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fullbody = fullbody_cascade.detectMultiScale(gray,scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30))

for(x,y,w,h) in fullbody:
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    boobs = boob_cascade.detectMultiScale(roi_gray,scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30))

    for (bx,by,bw,bh) in boobs:
        cv2.rectangle(roi_color,(bx,by),(bx+bw,by+bh),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
