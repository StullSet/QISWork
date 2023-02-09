#!/usr/bin/env python3
# plot3d_torus.py

import numpy as np
import matplotlib.pyplot as plt
import sys
import os


def plot(ax):
    radius_toroidal = 25
    radius_poloidal = 5

    u = np.linspace(0, 2 * np.pi, 30)  # Poloidal rotation
    v = np.linspace(0, 2 * np.pi, 30)  # Toroidal rotation

    # Similar to sphere formula, just accounting for multiple radii
    x = np.outer(radius_toroidal + radius_poloidal * np.cos(u), np.cos(v))
    y = np.outer(radius_toroidal + radius_poloidal * np.cos(u), np.sin(v))
    z = np.outer(radius_poloidal * np.sin(u), np.ones_like(v))

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.view_init(azim=-60, elev=50)
    ax.set_xlim(-25, 25)
    ax.set_ylim(-25, 25)
    ax.set_zlim(-25, 25)

    # TODO: Uncomment the following lines one-by-one
    ax.scatter(x, y, z)
    # ax.plot_wireframe(x, y, z)
    # ax.plot_surface(x, y, z)


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d")

    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
