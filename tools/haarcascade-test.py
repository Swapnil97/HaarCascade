import numpy as np
import cv2
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
boob_cascade = cv2.CascadeClassifier('../data/cascade.xml')
img = cv2.imread('../info/0001_0286_0161_0278_0278.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

boobs = boob_cascade.detectMultiScale(gray, 100, 100)

print boobs
for (x,y,w,h) in boobs:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
