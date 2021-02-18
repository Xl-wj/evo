#! /usr/bin/env python

import os
import math
import matplotlib.pyplot as plt
import numpy as np

def mean(data):
    sum = 0
    for i in data:
        sum = sum+i
    return sum/len(data)


if __name__ == "__main__":

    file = "/home/xl/kalmanfilter_result.txt"

    frame = []
    measure_noise = []
    post_eval = []
    groundtruth = []
    counter = 0

    # Read all data
    document1 = open(file, 'rw+')
    for line1 in document1:
        split_line1 = line1.split()
        counter = counter + 1
        frame.append(counter)
        measure_noise.append(float(split_line1[0]))
        post_eval.append(float(split_line1[1]))
        groundtruth.append(float(split_line1[2]))

    document1.close()

    START = 0
    END = len(frame)-1

    frame_sub = frame[START:END]
    measure_noise_sub = measure_noise[START:END]
    post_eval_sub = post_eval[START:END]
    groundtruth_sub = groundtruth[START:END]


    fig, axes = plt.subplots(2,2)

    print axes.shape

    color = 'blue'
    axes[0, 0].set_xlabel(xlabel='Frame No.')
    axes[0, 0].set_ylabel('measure noise', color=color)
    axes[0, 0].set_ylim(-10, 500)
    axes[0, 0].plot(frame_sub, measure_noise_sub, '*-', color=color)
    axes[0, 0].tick_params(axis='y', labelcolor=color)

    color = 'red'
    axes[0, 1].set_ylabel('post eval', labelpad=40, color=color)  # we already handled the x-label with ax1
    axes[0, 1].set_ylim(-10, 500)
    axes[0, 1].plot(frame_sub, post_eval_sub, color=color)
    axes[0, 1].tick_params(axis='y', pad=30.0, labelcolor=color)

    color = 'gray'
    axes[1, 0].set_ylabel('ground truth', labelpad=40, color=color)  # we already handled the x-label with ax1
    axes[1, 0].set_ylim(-10, 500)
    axes[1, 0].tick_params(axis='y', labelcolor=color)
    axes[1, 0].plot(frame_sub, groundtruth_sub, color=color)

    plt.grid()
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.title("Kalman Test")
    plt.show()