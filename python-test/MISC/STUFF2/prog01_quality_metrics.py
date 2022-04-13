#!/usr/bin/python3

import cv2
import time
import os
import numpy as np
from scipy.ndimage.measurements import variance
from sewar import full_ref



#===============================================================================
# MAINLINE
#===============================================================================

def main():
    # A list of filenames of pictures.
    src_filenames = [
        '../zig.jpg'
    ]

    num_compression_specs = 4
    num_generations = 10


    for src_index in range(0, len(src_filenames)):
        src_filename = src_filenames[src_index]
        src_image = cv2.imread(src_filename)
        src_num = src_index + 1

        for spec_num in range(1, num_compression_specs+1):
            for gen_num in range(1, num_generations+1):
                test_filename = f'comp_src{src_num:02d}_spec{spec_num:02d}_gen{gen_num:02d}.jpg'

                test_image = cv2.imread(test_filename)
                size_in_bytes = os.path.getsize(test_filename)

                output = []
                output.append(src_filename)
                output.append(test_filename)
                output.append(size_in_bytes)
                output.append(src_num)
                output.append(spec_num)
                output.append(gen_num)
                output.append(full_ref.psnr(src_image, test_image))
                output.append(full_ref.mse(src_image, test_image))
                output.append(full_ref.rmse(src_image, test_image))
                output.append(full_ref.uqi(src_image, test_image))
                output.append(full_ref.ergas(src_image, test_image))
                output.append(full_ref.sam(src_image, test_image))
                output.append(full_ref.rase(src_image, test_image))

                # TBD - ADD THIS BACK!!!
                #ssim_output = full_ref.ssim(src_image, test_image)
                #output.append(ssim_output[0])
                #output.append(ssim_output[1])

                # TBD - ADD THIS BACK!!!
                #output.append(full_ref.vifp(src_image, test_image))

                output_string = ""

                for data in output:
                    if output_string != "":
                        output_string += ", "

                    output_string += str(data)

                print(output_string)


#=======================================
# Invoke the main() function and exit.
#=======================================
main()

