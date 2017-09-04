#import urllib.request
import urllib2
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
	   print getContentType(neg_image_urls)
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
	 print("Processing Complete!")

def getContentType(pageUrl):
    page = urllib2.urlopen(pageUrl)
    pageHeaders = page.headers
    contentType = pageHeaders.getheader('content-type')
    return contentType

store_raw_images()
