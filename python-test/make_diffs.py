#!/usr/bin/python3

import cv2
import info



#===============================================================================
# MAINLINE
#===============================================================================
def main():
    for src_id in range(1, info.NUM_SRC_FILES+1):
        src_filename = "input/image{}.jpg".format(src_id)
        src_image = cv2.imread(src_filename)

        work_image = src_image

        for spec_id in range(1, info.COMPRESS_NUM_SPECS+1):
            
            for gen_id in range(1, info.COMPRESS_NUM_GENERATIONS+1):
                prev_work_image = work_image
                work_filename = f'output/comp_src{src_id:02d}_spec{spec_id:02d}_gen{gen_id:02d}.jpg'
                work_image = cv2.imread(work_filename)

                diff_image = cv2.subtract(src_image, work_image)
                delta_image = cv2.subtract(prev_work_image, work_image)

                # Color the mask red 
                Conv_hsv_Gray = cv2.cvtColor(diff_image, cv2.COLOR_BGR2GRAY)
                ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
                diff_image[mask != 255] = [0, 0, 255]

                Conv_hsv_Gray = cv2.cvtColor(delta_image, cv2.COLOR_BGR2GRAY)
                ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
                delta_image[mask != 255] = [0, 0, 255]

                # Store images
                diff_filename = f'output/comp_diff_src{src_id:02d}_spec{spec_id:02d}_gen{gen_id:02d}.jpg'
                delta_filename = f'output/comp_delta_src{src_id:02d}_spec{spec_id:02d}_gen{gen_id:02d}.jpg'

                cv2.imwrite(diff_filename, diff_image)
                cv2.imwrite(delta_filename, delta_image)



#=======================================
# Invoke the main() function and exit.
#=======================================
main()

