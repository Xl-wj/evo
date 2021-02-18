#!/usr/bin/env python3
# This file is covered by the LICENSE file in the root of this project.

import os
import sys

import json
import numpy as np
import random

from pygeodesy.utm import toUtm8
from pygeodesy.ellipsoidalVincenty import LatLon

import matplotlib.pyplot as plt
import matplotlib as mpl

from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, LinearColorMapper, BasicTicker, ColorBar
from bokeh.models import HoverTool
import bokeh

from evo.tools import file_interface

"""
filter condition: nbSamples, delta elevation
"""

# thickness levels selection
levels = np.array([[0.0, 100.0],
                   [0.0, 0.2],
                   [0.0, 0.3],  # 3
                   [0.2, 1.0],
                   [0.2, 2.0],
                   [0.2, 3.0],
                   [0.2, 4.0],  # 7
                   [0.7, 4.0]])  # 8

# anchor_points for anchor

anchor_points = np.array([[39.24277572, 117.46616101],
                          [39.24258, 117.47579]])


ground_key_maps = {
    'index': 0, \
    'utmX': 1, \
    'utmY': 2, \
    'height': 3 \
    }


def showData(data, output_hfile, key_map=ground_key_maps, show_key='height'):
    if show_key is None:
        print(" You should given a show_key! ")
        return

    show_index = key_map[show_key]

    print("key = ", show_key)

    print("show_index = ", show_index)

    # TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
    TOOLS = "hover,pan,wheel_zoom,reset,save,"

    TOOLTIPS = [(key, "@" + key + "{0.00000}") for key, value in key_map.items()]

    p = figure(title='color based on: ' + show_key, tools=TOOLS, plot_width=1800, plot_height=900,
               active_scroll='wheel_zoom', match_aspect=True)

    data_source_map = {key: data[:, value] for key, value in key_map.items()}

    data_source = ColumnDataSource(data_source_map)

    color_mapper = LinearColorMapper(palette='RdYlGn9', low=min(data[:, show_index]), high=max(data[:, show_index]))

    scatter = p.scatter('utmX', 'utmY', source=data_source, color={'field': show_key, 'transform': color_mapper},
                        size=1.0)

    p.add_tools(HoverTool(renderers=[scatter], tooltips=TOOLTIPS, mode='mouse'))

    color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                         label_standoff=12, border_line_color=None, location=(0, 0))

    p.add_layout(color_bar, 'right')

    output_file(output_hfile, title='color based on: '+key)
    print("output_hfile: ", output_hfile)

    show(p)  # open a browser


def printDataBounding(data):
    # index bounding
    print("------- height bounding -------")
    print("z_min = ", data[:, 0].min())
    print("z_max = ", data[:, 0].max())
    print("z_del = ", data[:, 0].max() - data[:, 0].min())
    # lat bounding
    print("------- x bounding -------")
    print ("x_min = ", data[:, 1].min())
    print ("x_max = ", data[:, 1].max())
    print ("x_del = ", data[:, 1].max() - data[:, 1].min())
    # lng bounding
    print("------- y bounding -------")
    print("y_min = ", data[:, 2].min())
    print("y_max = ", data[:, 2].max())
    print("y_del = ", data[:, 2].max() - data[:, 2].min())
    # height bounding
    print("------- height bounding -------")
    print("z_min = ", data[:, 3].min())
    print("z_max = ", data[:, 3].max())
    print("z_del = ", data[:, 3].max() - data[:, 3].min())
    # size
    print("------- size -------")
    print("size = ", data.shape[0])




def test_trajectory(pose_file, output_hfile):

    odo_trajectory, indexs = file_interface.read_neolix_trajectory_file(pose_file)

    data = np.zeros((indexs.shape[0], 4), dtype=np.float64)
    data[:, 0] = indexs
    data[:, 1:4] = odo_trajectory.positions_xyz

    printDataBounding(data)
    showData(data, output_hfile)



def test_lio_sam_trajectory(pose_file, output_hfile):

    odo_trajectory, indexs = file_interface.read_lio_sam_trajectory_file(pose_file)

    data = np.zeros((indexs.shape[0], 4), dtype=np.float64)
    data[:, 0] = indexs
    data[:, 1:4] = odo_trajectory.positions_xyz

    printDataBounding(data)

    showData(data, output_hfile)




def compare_trajectorys(pose_file_1, pose_file_2, output_hfile):
    # pose_file_1
    print "Compare trajectorysfile: ", pose_file_1, pose_file_2

    odo_trajectory_1, indexs_1 = file_interface.read_neolix_trajectory_file(pose_file_1)
    data_1 = np.zeros((indexs_1.shape[0], 4), dtype=np.float64)
    data_1[:, 0] = indexs_1
    data_1[:, 1:4] = odo_trajectory_1.positions_xyz
    data_1[:, 3] = 0.0
    printDataBounding(data_1)

    print " **************************************  "

    # pose_file_2
    odo_trajectory_2, indexs_2 = file_interface.read_neolix_trajectory_file(pose_file_2)
    data_2 = np.zeros((indexs_2.shape[0], 4), dtype=np.float64)
    data_2[:, 0] = indexs_2
    data_2[:, 1:4] = odo_trajectory_2.positions_xyz
    data_2[:, 3] = 1.0
    printDataBounding(data_2)

    data = np.concatenate((data_1, data_2), axis=0)
    showData(data, output_hfile)





if __name__ == '__main__':
    pose_file = "/home/xl/Desktop/ht_office/opt/rtk_opt_pose_after.txt"
    output_hfile = pose_file + ".html"
    test_trajectory(pose_file, output_hfile)

    # rtk_pose = "/home/xl/Desktop/sc_test/rtk/sc_poses.txt"
    # compare_trajectorys(pose_file, rtk_pose, output_hfile)
    # pose_file = "/home/xl/projects/ws_lio_sam/parse/odometry/lidar_poses.txt"
    # output_hfile = pose_file + ".html"
    # test_lio_sam_trajectory(pose_file, output_hfile)

