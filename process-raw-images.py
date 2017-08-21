#import urllib.request
import urllib2
import cv2
import numpy as np
import os

def convetAndMoveImage():
	for fileName in os.listdir('raw_neg'):
		if(fileName.endsWith(".jpg")):
			img = cv2.imread(fileName,cv2.IMREAD_GRAYSCALE)
			height, width, channels = img.shape
			if((height != 100) and (width != 100)):
				img = cv2.resize(img,(100, 100))
			cv2.imwrite("neg/"+fileName.img)

def find_uglies():
    match = False
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))
