import numpy
import cv2


n = numpy.arange(27)

#reshaping the array in a 3*3 matrix
print n.reshape(3,3,3)

#creating numpy arrays out of images
# 0 represents importing gray scale image 
def im_gray(x):
	x = cv2.imread("C:/Users/ibhar/OneDrive/Pictures/gray.png",0)

x = cv2.imread("C:/Users/ibhar/OneDrive/Pictures/gray.png",0)
print im_gray(x)

# 1 represents a color image i.e, BGR
# openCV uses BGR format and NOT RGB! 
im_gray = cv2.imread("C:/Users/ibhar/OneDrive/Pictures/gray.png",1)
print im_gray

#creating images out of numpy arrays
print cv2.imwrite("newgray.png",im_gray)
