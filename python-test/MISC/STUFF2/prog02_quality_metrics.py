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
        'zig.jpg'
    ]

    # Resize Scenarios
    num_scenarios = 6

    # The strategies list
    strategies = [
        'NEAREST',
        'LINEAR',
        'AREA',
        'CUBIC',
        'LANCZOS4',
        'LINEAR_EXACT',
    ]

    # Loop over each source file
    for src_index in range(0, len(src_filenames)):
        src_num = src_index + 1
        src_filename = src_filenames[src_index]
        src_image = cv2.imread(src_filename)

        for scenario_num in range(1, num_scenarios+1):
            for strategy_index in range(0, len(strategies)):
                strategy_num = strategy_index + 1
                strategy = strategies[strategy_index]

                test_filename = f'resized_src{src_num:02d}_scen{scenario_num:02d}_strat{strategy_num:02d}.png'

                test_image = cv2.imread(test_filename)

                output = []
                output.append(src_filename)
                output.append(test_filename)
                output.append(strategy)
                output.append(src_num)
                output.append(scenario_num)
                output.append(strategy_num)
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

