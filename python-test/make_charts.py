#!/usr/bin/python3

import info
import numpy as np
import matplotlib.pyplot as plt
import pickle


#===============================================================================
# CHART A
#
# All generations from 0 to NUM are shown for all JPEG QUALITY levels
#===============================================================================
def save_chartA(src_id, metric_name, metric_values):
    filename = f'charts/chartA_{metric_name}_src{src_id:02d}.png'

    xpoints = range(0, info.COMPRESS_NUM_GENERATIONS+1)

    plt.clf()

    #ax = plt.gca()
    #ax.get_yaxis().get_major_formatter().set_useOffset(False)

    #plt.figure(num=1, figsize=(10.24, 7.68))
    plt.figure(num=1, dpi=200.0)

    for spec_index in range(0, info.COMPRESS_NUM_SPECS):
        ypoints = []

        for gen_id in range(0, info.COMPRESS_NUM_GENERATIONS+1):
            ypoints.append(metric_values[gen_id][spec_index])

        # Draw the line here
        spec_jpeg_quality = info.COMPRESS_SPECS[spec_index]
        spec_label = "JPEG Quality={}".format(spec_jpeg_quality)

        plt.plot(xpoints, ypoints, marker='o', label=spec_label)

    plt.title("{} for Source ID {}".format(metric_name, src_id))
    plt.xlabel("Generation")
    plt.ylabel(metric_name)
    plt.legend()

    plt.savefig(filename)
    plt.clf()


#===============================================================================
# CHART B
#
# Same as CHART A except that generation 0 is not shown here.
#===============================================================================
def save_chartB(src_id, metric_name, metric_values):
    filename = f'charts/chartB_{metric_name}_src{src_id:02d}.png'

    xpoints = range(1, info.COMPRESS_NUM_GENERATIONS+1)

    plt.clf()

    for spec_index in range(0, info.COMPRESS_NUM_SPECS):
        ypoints = []

        for gen_id in range(1, info.COMPRESS_NUM_GENERATIONS+1):
            ypoints.append(metric_values[gen_id][spec_index])

        # Draw the line here
        spec_jpeg_quality = info.COMPRESS_SPECS[spec_index]
        spec_label = "JPEG Quality={}".format(spec_jpeg_quality)
        
        plt.plot(xpoints, ypoints, marker='o', label=spec_label)

    plt.title("{} for Source ID {}".format(metric_name, src_id))
    plt.xlabel("Generation")
    plt.ylabel(metric_name)
    plt.legend()

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
        plt.plot(xpoints, ypoints, marker='o')

        spec_value = info.COMPRESS_SPECS[spec_index]
        src_name = "image{}.jpg".format(src_id)

        plt.title("{} for Source: {}, JPEG Quality: {}".format(metric_name, src_id, spec_value))
        plt.xlabel("Generation")
        plt.ylabel(metric_name)

        filename = f'charts/chartC_{metric_name}_spec{spec_id:02d}_src{src_id:02d}.png'
        plt.savefig(filename)
        plt.clf()


#===============================================================================
# MAINLINE
#===============================================================================
def main():
    # Unpickle the src_metrics list of individual "metrics" dictionaries
    # (one per "source file/id").
    src_metrics = pickle.load(open("metrics/src_metrics.pickle", "rb"))

    for src_index in range(0, len(src_metrics)):
        metrics = src_metrics[src_index]
        src_id = src_index + 1

        #----------------------------------------------------------------------------------
        # Now we can process the metrics and make the charts for the current source file.
        #----------------------------------------------------------------------------------
        print("PROGRESS: Making charts")

        for metric_name, metric_values in metrics.items():
            save_chartA(src_id, metric_name, metric_values)
            save_chartB(src_id, metric_name, metric_values)
            save_chartC(src_id, metric_name, metric_values)



#=======================================
# Invoke the main() function and exit.
#=======================================
main()

