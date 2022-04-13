#!/usr/bin/python3

import cv2
import numpy as np


#===============================================================================
#===============================================================================
def determine_metric_a():
    pass


#===============================================================================
#===============================================================================
def determine_metric_b():
    pass


#===============================================================================
#===============================================================================
def determine_metric_c():
    pass


#===============================================================================
#===============================================================================
def determine_size_on_disk(image, quality):
    pass


#===============================================================================
# MAINLINE
#===============================================================================
def main():
    # The Width and Height of the display on the device.
    DISPLAY_WIDTH  = 200
    DISPLAY_HEIGHT = 600

    # The filename of the source image
    src_filename = 'original_image.png'

    # The choice of interpolation to be used for the resize operation.
    the_interpolation = cv2.INTER_LINEAR

    # Read the image using imread.
    src_image = cv2.imread(src_filename)
    cv2.imshow('Original Image', src_image)

    # Determine the source image size.
    src_height = src_image.shape[0]
    src_width  = src_image.shape[1]

    # Determine the factor to apply as both fx and fy in the resize operation.
    factor = min(DISPLAY_WIDTH / src_width, DISPLAY_HEIGHT / src_height)

    # Perform the resize operation to get a new, resized image.
    target_image = cv2.resize(src_image,
                            None,
                            fx=factor,
                            fy=factor,
                            interpolation=the_interpolation)

    # Determine the target image size.
    target_height = target_image.shape[0]
    target_width  = target_image.shape[1]


    # Perform quality measurements of the new image, each returning measurement
    # value(s), storing the returned values in local variables here.
    metric_a = determine_metric_a()
    metric_b = determine_metric_b()
    metric_c = determine_metric_c()

    # Perform jpeg save scenarios, each time returning the size-on-disk
    # (in bytes) of the saved jpeg file.  Do this with a few different
    # quality values (100%, 75%, 50%), and save the size-on-disk value
    # for each to local variables.
    size_on_disk_100 = determine_size_on_disk(target_image, 100)
    size_on_disk_75  = determine_size_on_disk(target_image,  75)
    size_on_disk_50  = determine_size_on_disk(target_image,  50)

    # Display the CSV line for the current "test/sample" data collected
    # (in the local variables).
    print("{},{},{},{},{},{},{},{},{},{},{},{}".format(
            src_filename,
            src_height,
            src_width,
            target_height,
            target_width,
            metric_a,
            metric_b,
            metric_c,
            size_on_disk_100,
            size_on_disk_75,
            size_on_disk_50))

    # Display the images.
    cv2.imshow('Resized by defining height and width', target_image)
    cv2.waitKey()

    #press any key to close the windows
    cv2.destroyAllWindows


#=======================================
# Invoke the main() function and exit.
#=======================================
main()

