"""
odometry 2 utm formats.
Author: wj
"""

import numpy as np
from evo.tools import file_interface
from evo.core.trajectory import PoseTrajectory3D
from numpy import *


def convert_neolix_2_utm(odometry_file, utm_file, begin_timestamp=-1.0, end_timestamp=1e15):

    odo_trajectory, _ = file_interface.read_neolix_trajectory_file(odometry_file)

    timestamps = np.array(odo_trajectory.timestamps, dtype=float64)
    valid_index = np.where((timestamps>begin_timestamp) & (timestamps < end_timestamp))
    # valid_index = np.array(valid_index, dtype=int32)
    # print valid_index.shape[0], valid_index.shape[1]

    xyz = odo_trajectory.positions_xyz[valid_index]
    quat = odo_trajectory.orientations_quat_wxyz[valid_index]
    timestamps = timestamps[valid_index]

    file_interface.write_tum_trajectory_file(utm_file, PoseTrajectory3D(xyz, quat, timestamps))



def convert_neolix_rtk_2_utm(rtk_pose_file, tum_rtk_pose_file):

    odo_trajectory = file_interface.read_neolix_rtk_trajectory_file(rtk_pose_file)

    file_interface.write_tum_trajectory_file(tum_rtk_pose_file, odo_trajectory)



if __name__ == '__main__':
    # odometry_file = "/home/xl/jiashan_map/8-17-test-out/location/odometry_loc.txt"
    # rtk_post_file = "/home/xl/jiashan_map/8-17-test-out/location/rtk_post_process_loc.txt"
    # tum_rtk_post_file = "/home/xl/jiashan_map/8-17-test-out/location/rtk_post_process_loc_tum.txt"
    # utm_file = "/home/xl/jiashan_map/8-17-test-out/location/odometry_loc_tum.txt"

    odometry_file = "/home/xl/Desktop/ht_office/opt/rtk_opt_pose_after.txt"
    odometry_file_tum_file = odometry_file + "_tum.txt"
    convert_neolix_2_utm(odometry_file, odometry_file_tum_file)


    # interpolate_file = "/home/xl/Desktop/ht_office/rtk/best_pose.txt_pose.txt"
    # interpolate_tum_file = interpolate_file + "_tum.txt"
    #
    # begin_timestamp = 1604916727.546555042267
    # end_timestamp = 1604917231.745474100113
    #
    # convert_neolix_2_utm(interpolate_file, interpolate_tum_file, begin_timestamp, end_timestamp)
    # convert_neolix_rtk_2_utm(rtk_post_file, tum_rtk_post_file)