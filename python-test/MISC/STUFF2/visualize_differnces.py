#!/usr/bin/python3
import cv2

# Load images.
image_original = cv2.imread("/home/joe/joehw/CSE408/python_test/STUFF2/comp_src01_spec01_gen01.jpg")
image_compare  = cv2.imread("/home/joe/joehw/CSE408/python_test/STUFF2/comp_src01_spec04_gen10.jpg")

# Compute difference
difference = cv2.subtract(image_original, image_compare)

# Color the mask red 
Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
difference[mask != 255] = [0, 0, 255]

# Add the red mask to the image to make the differences obvious
image_original[mask != 255] = [0, 0, 255]
image_compare[mask != 255]  = [0, 0, 255]

# Store images
cv2.imwrite('Original_Image.png', image_original)
cv2.imwrite('Compared_Image.png', image_compare)
cv2.imwrite('diff.png', difference)