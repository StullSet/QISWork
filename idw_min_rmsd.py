#!/usr/bin/env python3
# idw_min_rmsd.py

import numpy as np
import matplotlib.pyplot as plt
from numba import jit
import sys
import os


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
    grid_x, grid_y = np.mgrid[
        0 : ocean_size : complex(0, num_intervals),
        0 : ocean_size : complex(0, num_intervals),
    ]
    grid_z = act_height(grid_x, grid_y)

    global samples_x, samples_y, samples_z
    samples_x = np.random.uniform(0, ocean_size, num_samples)
    samples_y = np.random.uniform(0, ocean_size, num_samples)
    samples_z = act_height(samples_x, samples_y)


@jit(nopython=True)
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
    global est_z
    est_z = np.zeros_like(grid_x)
    for xi in range(num_intervals):
        for yi in range(num_intervals):
            est_z[xi, yi] = calc_idw_height(xi, yi, p)
    return est_z


def calc_rmsd(p):
    # Calculating the Root Mean Square Deviation
    # See slides 99 and 101 for overview
    sum_errors = 0.0
    for xi in range(num_intervals):
        for yi in range(num_intervals):
            act = grid_z[xi, yi]
            est = calc_idw_height(xi, yi, p)
            sum_errors += (act - est) ** 2
    rmsd = np.sqrt(sum_errors / num_samples**2)
    return rmsd


def plot(ax):
    p = np.linspace(1.0, 9.0, 50)
    calc_rmsd_vec = np.vectorize(calc_rmsd)
    rmsd = calc_rmsd_vec(p)

    # Using built in numpy functions to calculate the minimum and
    # find the index of the minimum p value
    min_rmsd = np.amin(rmsd)
    best_p = p[np.argmin(rmsd)]

    ax.plot(p, rmsd)
    ax.scatter(best_p, min_rmsd, color="red")

    ax.set_title("Inverse Distance Weighting (p vs RMSD)")
    ax.set_xlabel("p (Power) term")
    ax.set_ylabel("RMSD (Act vs. Est)")

    ax.text(5.0, 3.0, f"best p = {best_p:.4f}", ha="left")


def main():

    init_samples()

    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
