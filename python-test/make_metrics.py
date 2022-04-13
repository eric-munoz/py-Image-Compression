#!/usr/bin/python3

import cv2
import info
import os
import pickle
from sewar import full_ref


#===============================================================================
# MAINLINE
#===============================================================================
def main():
    src_metrics = []

    for src_id in range(1, info.NUM_SRC_FILES+1):
        print("PROGRESS: Starting on src_id {}".format(src_id))
        #------------------------
        # Read the source image
        #------------------------
        src_filename = "input/image{}.jpg".format(src_id)
        src_image = cv2.imread(src_filename)

        #----------------------
        # Set up the metrics
        #----------------------
        metrics = {
            'SizeOnDisk' : [],
            'PSNR'       : [],
            'MSE'        : [],
            'UQI'        : [],
            'SSIM'       : [],
        }

        # For each metric add a list for each generation including generation 0.
        for metric_name in metrics.keys():
            for gen_id in range(0, info.COMPRESS_NUM_GENERATIONS+1):
                metrics[metric_name].append([])

        #-------------------------------------------------------------------------------
        # Now we can loop over each spec, and perform each generation using that spec.
        #-------------------------------------------------------------------------------
        for spec_id in range(1, info.COMPRESS_NUM_SPECS+1):
            print("PROGRESS: Starting on spec_id {}".format(spec_id))
            for gen_id in range(0, info.COMPRESS_NUM_GENERATIONS+1):
                if gen_id % 10 == 0:
                    print("PROGRESS: Starting on gen_id {}".format(gen_id))

                # Setup the test_filename to either be the src_filename, for generation 0 only,
                # or to the formatted name of the test file for the source, spec, and generation.
                test_filename = src_filename

                if gen_id > 0:
                    test_filename = f'output/comp_src{src_id:02d}_spec{spec_id:02d}_gen{gen_id:02d}.jpg'

                # Now we can read in the test image.
                test_image = cv2.imread(test_filename)

                # Now we can compute metrics and save the results in the "metrics" dictionary.
                metrics['SizeOnDisk'][gen_id].append(os.path.getsize(test_filename))

                metrics['PSNR'][gen_id].append(full_ref.psnr(src_image, test_image))
                metrics['MSE'][gen_id].append(full_ref.mse(src_image, test_image))
                metrics['UQI'][gen_id].append(full_ref.uqi(src_image, test_image))

                ssim_output = full_ref.ssim(src_image, test_image)
                metrics['SSIM'][gen_id].append(ssim_output[0])

        #-----------------------------------------------------------------------------
        # Now we can add the metrics for the current src_id to the src_metrics list.
        #-----------------------------------------------------------------------------
        src_metrics.append(metrics)

    #------------------------------------------------------
    # Let's save the src_metrics to a binary pickle file.    
    #------------------------------------------------------
    pickle.dump(src_metrics, open("metrics/src_metrics.pickle", "wb"))


#=======================================
# Invoke the main() function and exit.
#=======================================
main()

