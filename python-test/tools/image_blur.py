#!/usr/bin/python3

# import the necessary packages
from imutils import paths

import cv2

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()



# load the image, convert it to grayscale, and compute the
# focus measure of the image using the Variance of Laplacian
# method
imagePath = '/home/joe/joehw/CSE408/python_test/output/comp_src01_spec04_gen50.jpg'
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fm = variance_of_laplacian(gray)
text = "Not Blurry"
# if the focus measure is less than the supplied threshold,
# then the image should be considered "blurry"
if fm < 100.00 or fm > 500:
		text = "Blurry"

# show the image
cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
	cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
cv2.imshow("Image", image)
key = cv2.waitKey(0)