"""
odometry 2 utm formats.
Author: wj
"""

import numpy as np
from evo.tools import file_interface
from numpy import *


def convert_neolix_2_utm(odometry_file, utm_file):

    odo_trajectory = file_interface.read_neolix_trajectory_file(odometry_file)

    file_interface.write_tum_trajectory_file(utm_file, odo_trajectory)



def convert_neolix_rtk_2_utm(rtk_pose_file, tum_rtk_pose_file):

    odo_trajectory = file_interface.read_neolix_rtk_trajectory_file(rtk_pose_file)

    file_interface.write_tum_trajectory_file(tum_rtk_pose_file, odo_trajectory)



if __name__ == '__main__':
    odometry_file = "/home/xl/jiashan_map/8-17-test-out/location/odometry_loc.txt"
    rtk_post_file = "/home/xl/jiashan_map/8-17-test-out/location/rtk_post_process_loc.txt"
    tum_rtk_post_file = "/home/xl/jiashan_map/8-17-test-out/location/rtk_post_process_loc_tum.txt"
    utm_file = "/home/xl/jiashan_map/8-17-test-out/location/odometry_loc_tum.txt"

    interpolate_file = "/home/xl/jiashan_map/8-17-test-out/location/interpolation_out4.txt"
    interpolate_tum_file = "/home/xl/jiashan_map/8-17-test-out/location/interpolation_out4_tum.txt"

    # convert_neolix_2_utm(odometry_file, utm_file)
    convert_neolix_2_utm(interpolate_file, interpolate_tum_file)
    convert_neolix_rtk_2_utm(rtk_post_file, tum_rtk_post_file)