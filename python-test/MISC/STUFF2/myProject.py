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
    filenames = [
        'zig.jpg'
    ]

    compression_specs = {
        'SP01' : [100,100,100],
        'SP02' : [ 90, 90, 90],
        'SP03' : [ 80, 80, 80],
        'SP04' : [ 70, 70, 70],
        'SP05' : [ 60, 60, 60],
    }

    for src_filename in filenames:
        src_image = cv2.imread(src_filename)

        target_image = src_image

        for spec_name, levels in compression_specs.items():
            for level in levels:
                cv2.imwrite("/tmp/xxx.jpg", target_image, [int(cv2.IMWRITE_JPEG_QUALITY), level])

                before_time = time.time()
                target_image = cv2.imread("/tmp/xxx.jpg")
                after_time = time.time()
                print("DBG: write time at level {} is {}".format(level, after_time - before_time))

            # Now compute metrics using src_image and target_image
            time_01 = time.time()
            _psnr  = full_ref.psnr(src_image, target_image)
            time_02 = time.time()
            _mse   = full_ref.mse(src_image, target_image)
            time_03 = time.time()
            _rmse  = full_ref.rmse(src_image, target_image)
            time_04 = time.time()
            _uqi   = full_ref.uqi(src_image, target_image)
            time_05 = time.time()
            # TBD - CHANGE THIS BACK (AND DON'T SET IT TO 69)
            #_vifp  = full_ref.vifp(src_image, target_image)
            _vifp = 69
            time_06 = time.time()
            _ergas = full_ref.ergas(src_image, target_image)
            time_07 = time.time()
            _sam   = full_ref.sam(src_image, target_image)
            time_08 = time.time()
            _rase  = full_ref.rase(src_image, target_image)
            time_09 = time.time()
            _ssim  = full_ref.ssim(src_image, target_image)
            time_10 = time.time()


            print("DBG: psnr  time = {}".format(time_02 - time_01))
            print("DBG: mse   time = {}".format(time_03 - time_02))
            print("DBG: rmse  time = {}".format(time_04 - time_03))
            print("DBG: uqi   time = {}".format(time_05 - time_04))
            print("DBG: vifp  time = {}".format(time_06 - time_05))
            print("DBG: ergas time = {}".format(time_07 - time_06))
            print("DBG: sam   time = {}".format(time_08 - time_07))
            print("DBG: rase  time = {}".format(time_09 - time_08))
            print("DBG: ssim  time = {}".format(time_10 - time_09))

            
            # This needs to be the size of the /tmp/xxx.jpg file in bytes.
            size_in_bytes = os.path.getsize("/tmp/xxx.jpg")

            print("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(
                                                                        src_filename, 
                                                                        spec_name,
                                                                        size_in_bytes,
                                                                        _psnr, 
                                                                        _mse, 
                                                                        _rmse,
                                                                        _uqi, 
                                                                        _vifp, 
                                                                        _ergas, 
                                                                        _sam,
                                                                        _rase,
                                                                        _ssim[0],
                                                                        _ssim[1]
                                                                        ))


#=======================================
# Invoke the main() function and exit.
#=======================================
main()

