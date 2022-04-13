#!/usr/bin/python3

import cv2



#===============================================================================
# MAINLINE
#===============================================================================

def main():
    # A list of filenames for the source images.
    src_filenames = [
        '/home/joe/joehw/CSE408/python_test/zig.jpg'
    ]

    # Resize Scenarios (Each number is a percent, must be greater than 0 and not equal to 100)
    scenarios = [
        [  80, 120, 150,  50 ],
        [  95,  95,  90,  90 ],
        [ 150,  50, 150,  50 ],
        [  50, 150,  50, 150 ],
        [ 200,  50, 200,  50 ],
        [  50, 200,  50, 200 ]
    ]

    # The strategies list
    strategies = [
        cv2.INTER_NEAREST,
        cv2.INTER_LINEAR,
        cv2.INTER_AREA,
        cv2.INTER_CUBIC,
        cv2.INTER_LANCZOS4,
        cv2.INTER_LINEAR_EXACT,
    ]


    # Loop over each source file.
    for src_index in range(0, len(src_filenames)):
        src_num = src_index + 1
        src_filename = src_filenames[src_index]
        src_image = cv2.imread(src_filename)
        src_height = src_image.shape[0]
        src_width  = src_image.shape[1]
        src_dim    = (src_width, src_height)

        for scenario_index in range(0, len(scenarios)):
            scenario_num = scenario_index + 1
            scenario = scenarios[scenario_index]

            for strategy_index in range(0, len(strategies)):
                strategy_num = strategy_index + 1
                strategy = strategies[strategy_index]

                work_image = src_image

                for resize_percentage in scenario:
                    factor = resize_percentage / 100.0

                    work_image = cv2.resize(work_image,
                                            None,
                                            fx=factor,
                                            fy=factor,
                                            interpolation=strategy)

                work_image = cv2.resize(work_image, src_dim, interpolation=strategy)              
                
                out_filename = f'resized_src{src_num:02d}_scen{scenario_num:02d}_strat{strategy_num:02d}.png'

                cv2.imwrite(out_filename, work_image, [cv2.IMWRITE_PNG_COMPRESSION, 0])


#=======================================
# Invoke the main() function and exit.
#=======================================
main()

