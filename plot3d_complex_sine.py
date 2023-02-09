#!/usr/bin/env python3
# plot3d_complex_sine.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import sys
import os

# Defining the f(z) helper function
def f(z):
    return np.abs(np.sin(z))


def plot(ax):
    x = np.linspace(-2.5, 2.5)
    y = np.linspace(-1, 1)

    # See slides for more info but meshgrid effectively performs
    # The out product for us
    x, y = np.meshgrid(x, y)

    # defining the variable z
    z = x + 1j * y

    # cmap=cm.coolwarm changes colors based on height
    # Making sure to call f(z) rather than just z
    # Otherwise bypasses the helper function
    surf = ax.plot_surface(x, y, f(z), cmap=cm.coolwarm, linewidth=0, antialiased=False)

    # Telling python how many ticks we want on the graph
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter("{x:.02f}")

    # Creating a legend to show how values compare to colors explicitly
    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

    # Creating axis labels
    ax.set_title(r"Surface Plot of $ f(z) = \|\sin(z)\|$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")


# Standard main for 3d plots
def main():
    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)

    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0], projection="3d")

    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
