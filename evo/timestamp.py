import numpy as np
from evo.tools import file_interface
from numpy import *


def PlotTime(times):
    import matplotlib.pyplot as plt

    index = np.zeros(times.shape[0], dtype=float)
    for i in range(times.shape[0]):
        index[i] = i

    plt.plot(index, times, 'o')
    plt.xlabel('index')
    plt.ylabel('times')
    plt.show()


def TestPCDTimestamp(file):
    times = file_interface.load_neolix_pcd_timestamps(file)
    delta_times = np.zeros(times.shape[0] - 1, dtype=float)

    for i in range(times.shape[0] - 1):
        delta_times[i] = times[i + 1] - times[i]

    print delta_times.max(), delta_times.min()

    PlotTime(times=delta_times)


def TestRTKTimestamp(file):
    timestamps = file_interface.load_neolix_rtk_timestamps(file)

    delta_times = np.zeros(timestamps.shape[0] - 1, dtype=float)

    for i in range(timestamps.shape[0] - 1):
        delta_times[i] = timestamps[i + 1] - timestamps[i]

    print delta_times.max(), delta_times.min()

    PlotTime(times=delta_times)



if __name__ == '__main__':
    timestamp_file = "/home/xl/jiashan_map/8-17-test-out/pcd_timestamp.txt"
    rtk_file = "/home/xl/jiashan_map/8-17-test-out/location/rtk_post_process_loc.txt"


    # TestRTKTimestamp(rtk_file)
    TestPCDTimestamp(timestamp_file)
