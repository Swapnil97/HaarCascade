import urllib.request
import cv2
import numpy as np
import os

# https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

def run_app():
    eye_cascade = cv2.CascadeClassifier('data/haarcascade_eye.xml')
    face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)

    while True:
        ret, imf = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+2,y+h), (255,0,0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)& 0xff
            if k == 27:
                break
cap.release()
cvw.destroyAllWindows()


