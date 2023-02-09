#!/usr/bin/env python3
# plot3d_sphere.py

import numpy as np
import matplotlib.pyplot as plt
import sys
import os


def plot(ax):
    # Defining necessary variables to create a cylinder
    theta = np.linspace(0, 2 * np.pi, 30)
    # v is functioning as height
    v = np.linspace(0, 1, 30)

    # using np.meshgrid to perform the outer product
    theta, v = np.meshgrid(theta, v)
    # Defining variables x,y,z in polar coordinates
    # The 30 represents our desired radius
    x = 30 * np.cos(theta)
    y = 30 * np.sin(theta)
    z = v

    ax.set_title("3D Wire Grid of Cylinder")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    # ax.scatter(x, y, z)
    ax.plot_wireframe(x, y, z)
    # ax.plot_surface(x, y, z)


# Standard main for 3d plots
def main():
    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d")

    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
