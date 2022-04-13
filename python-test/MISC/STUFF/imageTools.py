#!/usr/bin/python3

import cv2
import numpy as np

from sewar import full_ref


originalImage = cv2.imread("/home/joe/joehw/CSE408/python_test/original_image.png")

# Use the originalImage as the dirty image to test.
#dirtyImage    = cv2.imread("/home/joe/joehw/CSE408/python_test/original_image.png")

dirtyImage    = cv2.imread("/home/joe/joehw/CSE408/python_test/compressed_image.png")

image_PSNR   = full_ref.psnr(originalImage, dirtyImage)
#image_PSNRB  = full_ref.psnrb(originalImage, dirtyImage)
image_UQI    = full_ref.uqi(originalImage, dirtyImage)
image_MSE    = full_ref.mse(originalImage, dirtyImage)
image_RMSE   = full_ref.rmse(originalImage, dirtyImage)
image_VIFP   = full_ref.vifp(originalImage, dirtyImage)
image_ERGAS  = full_ref.ergas(originalImage, dirtyImage)
image_SAM    = full_ref.sam(originalImage, dirtyImage)
image_SSIM   = full_ref.ssim(originalImage, dirtyImage)
image_RASE   = full_ref.rase(originalImage, dirtyImage)



print("-------------------------------------------------------")
print("The Peak Signal-to-Noise Raito (PSNR): {}".format(image_PSNR))
print("------------------------------------------------------- \n")

print("-------------------------------------------------------")
#print("The PSNRB : {}".format(image_PSNRB))
print("------------------------------------------------------- \n")

print("-------------------------------------------------------")
print("The Universal Quality Image Index (UQI): {}".format(image_UQI))
print("------------------------------------------------------- \n")

print("-------------------------------------------------------")
print("The Mean Squared Error (MSE): {}".format(image_MSE))
print("------------------------------------------------------- \n")

print("-------------------------------------------------------")
print("The Root Mean Squared Error (RMSE): {}".format(image_RMSE))
print("------------------------------------------------------- \n")

print("-------------------------------------------------------")
print("The Visual Infomation Fidelity Pixel (VIFP): {}".format(image_VIFP))
print("------------------------------------------------------- \n")

print("-------------------------------------------------------")
print("The Global Relitive Error (ERGAS): {}".format(image_ERGAS))
print("------------------------------------------------------- \n")

print("-------------------------------------------------------")
print("The Spectral Angal Mapper (SAM): {}".format(image_SAM))
print("------------------------------------------------------- \n")

print("-------------------------------------------------------")
print("The Structural Simalarity Index (SSIM): {}".format(image_SSIM))
print("------------------------------------------------------- \n")


print("-------------------------------------------------------")
print("The Relitive Average Spectral Error (RASE): {}".format(image_RASE))
print("------------------------------------------------------- \n")

