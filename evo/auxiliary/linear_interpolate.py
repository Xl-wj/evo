"""
Linear interpolation.
Author: wj
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def linear_interpolate(time, pos1, pos2):
    t1 = time - pos1[0]
    t2 = pos2[0] - time
    po = (pos1[1:4] * t2 + pos2[1:4] * t1) / (t1 + t2)
    return po


def interpolation_traj(odo_timestamp, rtk_trajectory_with_timestamp):

    begin_rtk_time = rtk_trajectory_with_timestamp[0][0]
    end_rtk_time = rtk_trajectory_with_timestamp[-1][0]
    interpolate_trajectory = np.zeros((odo_timestamp.shape[0], 4))

    rtk_max_index = rtk_trajectory_with_timestamp.shape[0]

    i = 0
    for time in odo_timestamp:
        if time > begin_rtk_time and time < end_rtk_time:
            interpolate_trajectory[i][0] = time

            for j in range(rtk_max_index - 1):
                if rtk_trajectory_with_timestamp[j][0] <= time and rtk_trajectory_with_timestamp[j+1][0] >= time:

                    interpolate_trajectory[i][1:4] = \
                        linear_interpolate(time,rtk_trajectory_with_timestamp[j], rtk_trajectory_with_timestamp[j+1])

                    i = i + 1
                    break

    interpolate_trajectory = interpolate_trajectory[0:i, :]

    return interpolate_trajectory


def plot_trajectory_compare(ori_rtk_trajectory, interpolation_trajectory):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot(ori_rtk_trajectory[:, 0], ori_rtk_trajectory[:, 1], ori_rtk_trajectory[:, 2], 'b-')
    ax.plot(interpolation_trajectory[:, 0], interpolation_trajectory[:, 1], interpolation_trajectory[:, 2], 'r-')
    plt.show()


if __name__ == '__main__':
    odo_timestamp = np.array([
        [1],
        [2],
        [3]
    ])

    rtk_trajectory_with_timestamp = np.array([
        [0.5, 1, 2, 1],
        [2.3, 2, 3, 1],
        [3.5, 2, 5, 1]
    ])

    interpolation_traj = interpolation_traj(odo_timestamp, rtk_trajectory_with_timestamp)
    plot_trajectory_compare(rtk_trajectory_with_timestamp[:,1:4], interpolation_traj[:,1:4])