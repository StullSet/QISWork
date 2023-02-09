#!/usr/bin/env python3
# plot3d_surface.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import sys
import os


def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))


def plot(ax):
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)

    # See slides for more info but meshgrid effectively performs
    # The outer product for us
    x, y = np.meshgrid(x, y)

    z = f(x, y)

    # cmap=cm.coolwarm changes colors based on height
    surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    # Telling python how many ticks we want on the graph
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter("{x:.02f}")

    # Creating a legend to show how values compare to colors explicitly
    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d")

    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
