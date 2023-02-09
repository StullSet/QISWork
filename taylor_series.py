#!/usr/bin/env python3
# taylor_series.py

import matplotlib.pyplot as plt
import numpy as np
import sympy
import sys
import os


def plot(ax):
    # Plot exact y = cos(x)
    x = np.linspace(0, 2 * np.pi, 1000)
    ax.plot(x, np.cos(x), label="Exact")

    # Plot Newton's Expansion for cos(x)
    ax.plot(
        x,
        1
        - (1 / 2) * np.power(x, 2) / 2
        + (1 / 24) * np.power(x, 4)
        - (1 / 720) * np.power(x, 6)
        + (1 / 362880) * np.power(x, 9),
        label="Newton (5 terms)",
    )

    # Plot Taylor Series for cos(x)
    num_terms = 20
    xs = sympy.symbols("x")
    poly = sympy.cos(xs).series(xs, 0, num_terms).removeO()
    eqn = sympy.lambdify(xs, poly.as_expr(), modules="numpy")
    print(f"Taylor Series for cos(x) = {poly}")
    ax.plot(x, eqn(x), label=f"Taylor ({num_terms} terms)")

    # Plot Euler's Method for d[cos(x)] = -sin(x)
    # Estimating the function based on it's first derivative
    xm = np.linspace(0, 2 * np.pi, 20)
    ym = np.zeros(len(xm))
    dx = xm[1] - xm[0]
    ym[0] = np.cos(0)
    for i in range(1, len(xm)):
        ym[i] = ym[i - 1] - np.sin(xm[i - 1]) * dx
    ax.plot(xm, ym, label="Euler (20 terms)")

    ax.set_title(r"Taylor Series for $y = \cos(x)$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-1.1, 1.1)
    ax.axhline(y=0.0, color="lightgray", zorder=-2)


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
