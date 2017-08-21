#import urllib.request
import urllib2
import cv2
import numpy as np
import os
from subprocess import call

def store_raw_images():
    # Sports
    #neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'

    # Clubs
    # neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02931417'
    # Bedrooms
    #neg_image_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02821627'
    # Bathing Suits
    #  neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02814774'

	url_list = []
	# Sports
	url_list.append('http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513')
	# Clubs
	url_list.append('http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02931417')
	# Bedrooms
	url_list.append('http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02821627')
	#baithing suits
	url_list.append('http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02814774')

    	pic_num = 1
	for url in url_list:
	   neg_image_urls = urllib2.urlopen(url).read()
	   print("Processing.....")
	   print(url)
	   if not os.path.exists('raw_neg'):
			os.makedirs('raw_neg')

	   for i in neg_image_urls.split('\n'):
			try:
				print(i)
				imageData = urllib2.urlopen(i)
				with open("raw_neg/"+str(pic_num)+".jpg",'wb') as output:
					output.write(imageData.read())
				pic_num += 1
			except Exception as e:
				print(str(e))

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

store_raw_images()
#find_uglies()
#convetAndMoveImage()
