## Overview: Convert images

Converting regular images into array (Numpy) format. Manipulating the array in order to change the dimensions of the image. Converted images can either be in color format or gray (black&white) images. 

## Installing the library/ prerequisites

- numpy --> import numpy

- cv2 (OpenCV) -->
 
 OpenCV was added lately in the online Python package repository so first make sure you have the latest version of pip by executing:
 
 pip install -- upgrade pip
 
 Then install OpenCV:
 pip install opencv-python 
 
 And then you can import opencv in Python as:
 import cv2 


## Running the tests

step:1  Choose the image you want to convert into array format.
step:2  Provide its path for it to be readable by the code. 
step:3  If you want the image to be imported into gray code, use 0 at the end or 1 if you want it to be in original format.
step:4  running this portion of the code will give you the array of the image you provide. 

Converting array into image

step:1 Either use an array or use the converted image --> array 
step:2 Pass that array to cv2.imwrite and it will generate the image.

## Running the code

Once you have completed the entire project, you can run it in a terminal like this:

`python convert.py`
