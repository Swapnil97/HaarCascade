# HaarCascade
Opencv-Python Haar Cascade


# Notes
https://github.com/mrnugget/opencv-haar-classifier-training
find ./positive_images -iname "*.jpg" > positives.txt
find ./negative_images -iname "*.jpg" > negatives.txt

perl bin/createsamples.pl positives.txt negatives.txt samples 1500\
  "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1\
  -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 80 -h 40"


https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/  
opencv_workspace
--neg
----negimages.jpg
--opencv
--info
--bg.txt
--watch5050.jpg

opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950

opencv_createsamples -info info/info.lst -num 1950 -w 20 -h 20 -vec positives.vec

# Resize image
sudo yum install ImageMagick

mogrify -resize 500 *.jpg
convert 12.jpg -resize 50 12.jpg

# change background/negatives to gray scale
mkdir bw && for i in *.jpg; do convert $i -colorspace Gray -gamma 2.2 bw/$i; done


# Marker positive images
python ./ObjectMarker.py ./positive_images/ output.txt

# ObjectMarker error
export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages

# Create Samples
opencv_createsamples -img ./crop/2.jpg -bg negatives.txt -info info2/info.lst -pngoutput info2 -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 400

cat ../info.dat >> ./info/info.lst

opencv_createsamples -info info/info.lst -num 4927 -w 20 -h 20 -vec positives.vec


# Train
nohup opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20 &

opencv_traincascade -data data -vec positives.vec -bg negatives.txt -numPos 2110 -numNeg 1000 -numStages 20 -w 20 -h 20

Note -numPos = totalNumOfPos * .9 worked for testing

This will allow the command to continue running, even after you close the terminal. You can do more,
but you may or may not run out of your 2GB of ram.

# ideas for haarcascades
 explicit *default
 lingerie/swimsuits
 top
 bottom
