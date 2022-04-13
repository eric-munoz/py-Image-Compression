#!/usr/bin/python3

import cv2
import info
import time
#import os
#import numpy as np
#from scipy.ndimage.measurements import variance
from sewar import full_ref



#===============================================================================
# MAINLINE
#===============================================================================

def main():
    for src_id in range(1, info.NUM_SRC_FILES+1):
        src_filename = "input/image{}.jpg".format(src_id)
        src_image = cv2.imread(src_filename)

        for scenario_id in range(1, info.RESIZE_NUM_SCENARIOS+1):
            for strategy_index in range(0, info.RESIZE_NUM_STRATEGIES):
                strategy_id = strategy_index + 1
                strategy = info.RESIZE_STRATEGIES[strategy_index]

                test_filename = f'output/resized_src{src_id:02d}_scen{scenario_id:02d}_strat{strategy_id:02d}.png'

                test_image = cv2.imread(test_filename)

                output = []
                output.append(src_filename)
                output.append(test_filename)
                output.append(strategy)
                output.append(src_id)
                output.append(scenario_id)
                output.append(strategy_id)
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

