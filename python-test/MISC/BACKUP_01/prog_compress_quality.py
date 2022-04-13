#!/usr/bin/python3

import cv2
import info
import os
import numpy as np
import matplotlib.pyplot as plt
from sewar import full_ref



#===============================================================================
# CHART A
#
# All generations from 0 to NUM are shown for all JPEG QUALITY levels
#===============================================================================
def save_chartA(src_id, metric_name, metric_values):
    filename = f'output/chartA_{metric_name}_src{src_id:02d}.png'

    xpoints = range(0, info.COMPRESS_NUM_GENERATIONS+1)

    plt.clf()

    for spec_index in range(0, info.COMPRESS_NUM_SPECS):
        ypoints = []
        for gen_id in range(0, info.COMPRESS_NUM_GENERATIONS+1):
            ypoints.append(metric_values[gen_id][spec_index])

        # Draw the line here
        plt.plot(xpoints, ypoints)

    plt.savefig(filename)
    plt.clf()


#===============================================================================
# CHART B
#
# Same as CHART A except that generation 0 is not shown here.
#===============================================================================
def save_chartB(src_id, metric_name, metric_values):
    filename = f'output/chartB_{metric_name}_src{src_id:02d}.png'

    xpoints = range(1, info.COMPRESS_NUM_GENERATIONS+1)

    plt.clf()

    for spec_index in range(0, info.COMPRESS_NUM_SPECS):
        ypoints = []
        for gen_id in range(1, info.COMPRESS_NUM_GENERATIONS+1):
            ypoints.append(metric_values[gen_id][spec_index])

        # Draw the line here
        plt.plot(xpoints, ypoints)

    plt.savefig(filename)
    plt.clf()


#===============================================================================
# CHART C
#
# Same as CHART B except that each "spec" (JPEQ Quality Level) gets a chart
#===============================================================================
def save_chartC(src_id, metric_name, metric_values):
    xpoints = range(1, info.COMPRESS_NUM_GENERATIONS+1)

    plt.clf()

    for spec_index in range(0, info.COMPRESS_NUM_SPECS):
        spec_id = spec_index + 1
        ypoints = []
        for gen_id in range(1, info.COMPRESS_NUM_GENERATIONS+1):
            ypoints.append(metric_values[gen_id][spec_index])

        # Draw the line here
        plt.plot(xpoints, ypoints)
        filename = f'output/chartC_{metric_name}_spec{spec_id:02d}_src{src_id:02d}.png'
        plt.savefig(filename)
        plt.clf()


#===============================================================================
# MAINLINE
#===============================================================================
def main():
    for src_id in range(1, info.NUM_SRC_FILES+1):
        #------------------------
        # Read the source image
        #------------------------
        src_filename = "input/image{}.jpg".format(src_id)
        src_image = cv2.imread(src_filename)

        #----------------------
        # Set up the metrics
        #----------------------
        metrics = {
            'size_on_disk' : [],
            'psnr'         : [],
            'mse'          : [],
            'rmse'         : [],
            'uqi'          : [],
            #'ssim'         : [],
            #'ergas'        : [],
            #'sam'          : [],
            #'rase'         : [],
        }

        # For each metric add a list for each generation including generation 0.
        for metric_name in metrics.keys():
            for gen_id in range(0, info.COMPRESS_NUM_GENERATIONS+1):
                metrics[metric_name].append([])

        #-------------------------------------------------------------------------------
        # Now we can loop over each spec, and perform each generation using that spec.
        #-------------------------------------------------------------------------------
        for spec_id in range(1, info.COMPRESS_NUM_SPECS+1):
            for gen_id in range(0, info.COMPRESS_NUM_GENERATIONS+1):
                # Setup the test_filename to either be the src_filename, for generation 0 only,
                # or to the formatted name of the test file for the source, spec, and generation.
                test_filename = src_filename

                if gen_id > 0:
                    test_filename = f'output/comp_src{src_id:02d}_spec{spec_id:02d}_gen{gen_id:02d}.jpg'

                # Now we can read in the test image.
                test_image = cv2.imread(test_filename)

                # Now we can compute metrics and save the results in the "metrics" dictionary.
                metrics['size_on_disk'][gen_id].append(os.path.getsize(test_filename))

                metrics['psnr'][gen_id].append(full_ref.psnr(src_image, test_image))
                metrics['mse'][gen_id].append(full_ref.mse(src_image, test_image))
                metrics['rmse'][gen_id].append(full_ref.rmse(src_image, test_image))
                metrics['uqi'][gen_id].append(full_ref.uqi(src_image, test_image))

                # TBD - TURN THIS ONE BACK ON
                #ssim_output = full_ref.ssim(src_image, test_image)
                #metrics['ssim'][gen_id].append(ssim_output[0])

                # ALTERNATE SSIM value.
                #metrics['ssimTBD2'][gen_id].append(ssim_output[1])

                # TBD - ADD THESE IF YOU WANT THEM
                #metrics['ergas'][gen_id].append(full_ref.ergas(src_image, test_image))
                #metrics['sam'][gen_id].append(full_ref.sam(src_image, test_image))
                #metrics['rase'][gen_id].append(full_ref.rase(src_image, test_image))

                # TBD - ADD THIS IF YOU WANT IT.  MOST EXPENSIVE!!!
                #metrics['vifp'][gen_id].append(full_ref.vifp(src_image, test_image))


        #----------------------------------------------------------------------------------
        # Now we can process the metrics and make the charts for the current source file.
        #----------------------------------------------------------------------------------
        for metric_name, metric_values in metrics.items():
            save_chartA(src_id, metric_name, metric_values)
            save_chartB(src_id, metric_name, metric_values)
            save_chartC(src_id, metric_name, metric_values)


#=======================================
# Invoke the main() function and exit.
#=======================================
main()

