#!/usr/bin/python3

import cv2



#===============================================================================
# MAINLINE
#===============================================================================

def main():
    # A list of filenames for the source images.
    src_filenames = [
        '../zig.jpg'
    ]

    compression_specs = [
        [int(cv2.IMWRITE_JPEG_QUALITY), 100],
        [int(cv2.IMWRITE_JPEG_QUALITY),  90],
        [int(cv2.IMWRITE_JPEG_QUALITY),  80],
        [int(cv2.IMWRITE_JPEG_QUALITY),  70],
    ]

    num_generations = 10

    for src_index in range(0, len(src_filenames)):
        src_filename = src_filenames[src_index]
        src_image = cv2.imread(src_filename)

        work_image = src_image
        src_num = src_index + 1

        for spec_index in range(0, len(compression_specs)):
            write_args = compression_specs[spec_index]
            spec_num = spec_index + 1

            for gen_num in range(1, num_generations+1):
                out_filename = f'comp_src{src_num:02d}_spec{spec_num:02d}_gen{gen_num:02d}.jpg'

                cv2.imwrite(out_filename, work_image, write_args)

                work_image = cv2.imread(out_filename)
            

#=======================================
# Invoke the main() function and exit.
#=======================================
main()

