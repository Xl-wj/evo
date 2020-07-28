"""
Bezier curve fitting and interpolation.
Author: wj
"""

import numpy as np
import matplotlib.pyplot as plt
from math import  factorial
from mpl_toolkits.mplot3d import Axes3D


def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def get_bezier_curve(points):
    n = len(points) - 1
    return lambda t : sum(
        comb(n, i) * (t**i) * ((1 - t)**(n - i)) * points[i] for i in range(n+1)
    )


def evaluate_bezier(points, total):
    bezier = get_bezier_curve(points)
    new_points = np.array([bezier(t) for t in np.linspace(0, 1, total)])
    return new_points[:, 0], new_points[:, 1], new_points[:, 2]


def bezier_fitting(traj_with_timestamp = None):
    if traj_with_timestamp is None:
        return
    timestamp = traj_with_timestamp[:,0]
    trajectory = traj_with_timestamp[:, 1:4]

    bx, by, bz = evaluate_bezier(trajectory, 50)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot(trajectory[:,0], trajectory[:,1], trajectory[:,2], 'r.')
    ax.plot(bx, by, bz, 'b-')
    plt.show()


def test_bezier_curve_tool():
    trajectory_data = np.array([
        [1, 0, 0, 0],
        [2, -1, 3, 0],
        [3, 4, 3, 1],
        [4, 6, 0, 1],
        [5, 7, 2.5, 2]
    ])
    bezier_fitting(trajectory_data)


if __name__ == '__main__':
    test_bezier_curve_tool()