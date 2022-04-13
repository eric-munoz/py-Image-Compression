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

        for spec_index in range(0, info.COMPRESS_NUM_SPECS):
            spec_quality = info.COMPRESS_SPECS[spec_index]
            write_args = [int(cv2.IMWRITE_JPEG_QUALITY), spec_quality]
            spec_id = spec_index + 1
            
            for gen_id in range(1, info.COMPRESS_NUM_GENERATIONS+1):
                out_filename = f'output/comp_src{src_id:02d}_spec{spec_id:02d}_gen{gen_id:02d}.jpg'

                cv2.imwrite(out_filename, work_image, write_args)

                work_image = cv2.imread(out_filename)


#=======================================
# Invoke the main() function and exit.
#=======================================
main()

