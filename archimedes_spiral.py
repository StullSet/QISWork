#!/usr/bin/env python3
# archimedes_spiral.py

import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt
import sys
import os


def f(theta):
    return np.sqrt(theta**2 + 1)


def plot(ax):
    theta = np.linspace(0, 8 * np.pi, 1000)
    x = theta * np.cos(theta)
    y = theta * np.sin(theta)

    ax.plot(x, y)

    arc_length = scipy.integrate.quad(f, 0, 8 * np.pi)[0]

    ax.set_title(
        r"Archimedes Spiral $(r=\theta,\;0\leq\theta\leq 8\pi)$"
        f"\nArc Length = {arc_length:.4f}"
    )

    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    ax.set_aspect("equal")


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
