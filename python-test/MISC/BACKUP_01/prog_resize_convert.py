#!/usr/bin/python3

import cv2
import info



#===============================================================================
# MAINLINE
#===============================================================================
def main():
    for src_id in range(1, info.NUM_SRC_FILES+1):
        src_filename = "imput/image{}.jpg".format(src_id)
        src_image = cv2.imread(src_filename)
        src_height = src_image.shape[0]
        src_width  = src_image.shape[1]
        src_dim    = (src_width, src_height)

        for scenario_index in range(0, info.RESIZE_NUM_SCENARIOS):
            scenario_id = scenario_index + 1
            scenario = info.RESIZE_SCENARIOS[scenario_index]

            for strategy_index in range(0, info.RESIZE_NUM_STRATEGIES):
                strategy_id = strategy_index + 1
                strategy = info.RESIZE_STRATEGIES[strategy_index]

                work_image = src_image

                for resize_percentage in scenario:
                    factor = resize_percentage / 100.0

                    work_image = cv2.resize(work_image,
                                            None,
                                            fx=factor,
                                            fy=factor,
                                            interpolation=strategy)

                work_image = cv2.resize(work_image, src_dim, interpolation=strategy)              
                
                out_filename = f'output/resized_src{src_id:02d}_scen{scenario_id:02d}_strat{strategy_id:02d}.png'

                cv2.imwrite(out_filename, work_image, [cv2.IMWRITE_PNG_COMPRESSION, 0])



#=======================================
# Invoke the main() function and exit.
#=======================================
main()

