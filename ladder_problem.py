#!/usr/bin/env python3
# ladder_problem.py

import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt
import sys
import os


def plot(ax):
    # Defining our functions and variables
    # Cannot use zero because it causes divide by zero error
    theta = np.linspace(0.00000000001, np.pi / 2, 500)
    func = lambda theta: (2 / np.sin(theta)) + (1 / np.cos(theta))

    # Defining y in a method that we can then plot
    y = 2 / np.sin(theta) + 1 / np.cos(theta)

    # Using scipy to calculate the minimum theta value
    theta_min = minimize_scalar(func, method="bounded", bounds=(0, np.pi / 2))
    print(f"The maximum theta value is: {theta_min.x} radians")

    ax.plot(theta, y)

    ax.set_title("Maximum Ladder Length Function")
    ax.set_xlabel("Theta (Radians)")
    ax.set_ylabel("Ladder Length (m)")

    ax.grid()

    # Putting a dot where the function has zero rate of change
    ax.plot(0.8999077907621497, func(0.8999077907621497), color="red", marker=".")

    ax.set_xlim(0, 3)
    ax.set_ylim(0, 10)
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")


# Standard main() function
def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
