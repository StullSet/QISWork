#!/usr/bin/env python3
# idw.py

import numpy as np

# mayavi is a third party library that does 3D graphic rendering
import mayavi.mlab as mlab
from numba import jit


def act_height(x, y):
    # Calculate the height of the "actual" ocean at (x,y)
    return (
        30 * np.sin(y / 40) * np.cos(x / 40) + 50 * np.sin(np.sqrt(x * x + y * y) / 40)
    ) - 800


def init_samples():
    np.random.seed(2016)

    global ocean_size, num_intervals, num_samples
    ocean_size, num_intervals, num_samples = 390, 65, 220

    global grid_x, grid_y, grid_z
    # USing meshgrid produce a 3D grid of our x,y, and z values
    grid_x, grid_y = np.mgrid[
        0 : ocean_size : complex(0, num_intervals),
        0 : ocean_size : complex(0, num_intervals),
    ]
    # Running x and y through our function to produce z
    grid_z = act_height(grid_x, grid_y)

    global samples_x, samples_y, samples_z
    samples_x = np.random.uniform(0, ocean_size, num_samples)
    samples_y = np.random.uniform(0, ocean_size, num_samples)
    samples_z = act_height(samples_x, samples_y)


@jit(nopython=True)
# Calculating the Inverse Distance Weighting and returning a calculated height
# See slides 81-83 for in depth explanation
def calc_idw_height(xi, yi, p):
    sum_weight = 0.0
    sum_height_weight = 0.0
    for si in range(num_samples):
        distance = np.hypot(
            grid_x[xi, xi] - samples_x[si], grid_y[yi, yi] - samples_y[si]
        )
        if distance == 0:
            return samples_z[si]
        weight = 1 / np.power(distance, p)
        sum_weight += weight
        sum_height_weight += samples_z[si] * weight
    return sum_height_weight / sum_weight


def est_height(p):
    # Calculating an estimated height
    global est_z
    est_z = np.zeros_like(grid_x)
    for xi in range(num_intervals):
        for yi in range(num_intervals):
            est_z[xi, yi] = calc_idw_height(xi, yi, p)
    return est_z


def plot(idw_plot_type):

    # Plotting "actual"
    if idw_plot_type == 1:
        mlab.surf(grid_x, grid_y, grid_z, colormap="ocean")

    # Plotting estimates
    if idw_plot_type == 2:
        mlab.surf(grid_x, grid_y, est_z, colormap="ocean")

    # Plotting both to compare
    if idw_plot_type == 3:
        mlab.surf(grid_x, grid_y, grid_z, colormap="Blues", representation="wireframe")

        mlab.surf(grid_x, grid_y, est_z, colormap="Reds", representation="wireframe")

    if idw_plot_type == 1 or idw_plot_type == 2:
        mlab.points3d(samples_x, samples_y, samples_z, scale_factor=3, color=(1, 0, 0))

    mlab.show()


def main():
    init_samples()
    # TODO: Adjust the p (power) value in the following line
    est_height(p=4.7551)
    # TODO: Change the plot type (1,2,3) in the following line
    plot(idw_plot_type=3)


if __name__ == "__main__":
    main()
