#!/usr/bin/env python3
# fermat_derivative.py

import numpy as np
import matplotlib.pyplot as plt

# Another way to specify major and minor ticks
from matplotlib.ticker import MultipleLocator
import sys
import os


def f(x):
    return np.cos(x)


# Defining the algebraic definition of f'
# The difference equation
def f_prime(x, h):
    return (f(x + h) - f(x)) / h


def plot(ax):
    # Initializing our variables
    a = -4 * np.pi
    b = 4 * np.pi
    n = 500

    # Creating our linear space from a to b with n number of intervals
    x = np.linspace(a, b, n)

    # Putting in and getting out an array of values for y and y'
    # This works because x is vectorized
    y = f(x)
    y_prime = f_prime(x, (b - a) / n)

    # Crating our graph
    ax.plot(x, y, label="y")
    ax.plot(x, y_prime, label=r"$\frac{dy}{dx}$")

    ax.set_title(r"$y = cos(x)$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Setting all of the tick marks for the x and y axis
    # MultipleLocator(n) determines the distance between ticks
    ax.xaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_major_locator(MultipleLocator(0.2))
    # Telling python to put the legend in the upper right
    # Will comply unless there isn't enough room
    ax.legend(loc="upper right")

    # Manually drawing the axes
    ax.axhline(0, color="black", linestyle="-")
    ax.axvline(0, color="black", linestyle="-")


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
