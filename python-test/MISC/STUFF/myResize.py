#!/usr/bin/python3

import cv2 as cv

# Read in the image with opencv.
#image = cv.imread('test_resize_image.jpg')

# Display the image. 
#cv.imshow('Test Image', image)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    # Resize the frame and return.
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Reading Video
capture = cv.VideoCapture('Test_video.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

