import numpy as np
import cv2
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
fullbody_cascade = cv2.CascadeClassifier('')
boob_cascade = cv2.CascadeClassifier('../data/HaarCascade_Nips_DO_10_10172017.xml')
img = cv2.imread('20161028_222607.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

boobs = boob_cascade.detectMultiScale(gray,scaleFactor=1.4,
    minNeighbors=5,
    minSize=(30, 30))

print boobs
for (x,y,w,h) in boobs:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
