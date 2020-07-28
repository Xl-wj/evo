"""
Curve fitting and interpolation.
Implementation process and usage of two types of methods: Bezier and Linear interpolation.
Author: wj
"""

import numpy as np
from evo.tools import file_interface
from evo.auxiliary import bezier_interpolate
from evo.auxiliary import linear_interpolate
from numpy import *

def bezier_test():
    odo_file = "/home/xl/evo/q_loam/re_00.txt"
    rtk_file = "/home/xl/evo/q_loam/gpstrans.txt"

    trajectory = file_interface.read_tum_trajectory_file(odo_file)

    xyz = np.array(trajectory.positions_xyz)

    timestamp = np.zeros((xyz.shape[0], 1))
    for i in range(xyz.shape[0]):
        timestamp[i] = trajectory.timestamps[i]

    txyz = np.concatenate((timestamp, xyz), axis=1)

    txyz[:, 1] = txyz[:, 1] - txyz[0, 1]
    txyz[:, 2] = txyz[:, 2] - txyz[0, 2]
    txyz[:, 3] = txyz[:, 3] - txyz[0, 3]

    bezier_interpolate.bezier_fitting(txyz)


def linear_test():
    odo_file = "/home/xl/evo/q_loam/re_00.txt"
    rtk_file = "/home/xl/evo/q_loam/gpstrans.txt"

    odo_trajectory = file_interface.read_tum_trajectory_file(odo_file)
    rtk_trajectory = file_interface.read_tum_trajectory_file(rtk_file)

    odo_timestamp_size = odo_trajectory.timestamps.shape[0]
    odo_timestamp = np.zeros((odo_timestamp_size, 1))
    for i in range(odo_timestamp_size):
        odo_timestamp[i] = odo_trajectory.timestamps[i]

    rtk_timestamp_size = rtk_trajectory.timestamps.shape[0]
    rtk_timestamp = np.zeros((rtk_timestamp_size, 1))
    for i in range(rtk_timestamp_size):
        rtk_timestamp[i] = rtk_trajectory.timestamps[i]

    xyz = np.array(rtk_trajectory.positions_xyz)
    rtk_txyz = np.concatenate((rtk_timestamp, xyz), axis=1)

    interpolation_rtk = linear_interpolate.interpolation_traj(odo_timestamp, rtk_txyz)
    # linear_interpolate.plot_trajectory_compare(rtk_txyz[:, 1:4], interpolation_rtk[:, 1:4])

    tum_format = np.concatenate((interpolation_rtk, np.zeros((interpolation_rtk.shape[0], 4))), axis=1)
    savetxt('/home/xl/evo/q_loam/interpolate_rtk.txt', tum_format)

    print("odo_trajectory size = ", odo_timestamp_size)
    print("rtk_trajectory size = ", rtk_timestamp_size)
    print("interpolation_rtk size = ", interpolation_rtk.shape[0])


if __name__ == '__main__':
    # bezier_test()
    linear_test()