#!/usr/bin/env python3
# werner_formula.py

import numpy as np
import matplotlib.pyplot as plt


def plot(ax):
    x = np.linspace(-3 * np.pi, 3 * np.pi)

    y1 = np.sin(0.8 * x)
    y2 = np.sin(0.5 * x)
    y3 = np.sin(0.8 * x) * np.sin(0.5 * x)
    y4 = 0.5 * (np.cos(0.8 * x - 0.5 * x) - np.cos(0.8 * x + 0.5 * x))

    ax.plot(x, y1, color="red", zorder=1, label=r"$\sin(0.8x)$")
    ax.plot(x, y2, color="blue", zorder=2, label=r"$\sin(0.5x)$")
    ax.plot(x, y3, color="green", zorder=3, label=r"$\sin(0.8x)\cdot\sin(0.5x)$")
    ax.scatter(
        x, y4, color="black", s=6, zorder=4, label=r"$0.5(\cos(0.3x)-\cos(1.2x))$"
    )

    ax.set_title("Werner Formula")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="upper right", prop={"size": 6})

    ax.grid()
    ax.set_xlim(-3 * np.pi, 3 * np.pi)
    ax.set_ylim(-2, 4)

    ax.axhline(0, color="black")
    ax.axvline(0, color="black")


def main():
    fig = plt.figure("Werner Formula")
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    ax.set_aspect("equal")

    plt.show()


main()
