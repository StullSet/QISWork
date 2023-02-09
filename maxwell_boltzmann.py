#!/usr/bin/env python3
# maxwell_boltzmann.py

import numpy as np
import matplotlib.pyplot as plt
import sys
import os


def plot(ax):

    # Initializing my x and y variables
    # x spans from 0 to 20 with 1000 evenly spaced intervals
    x = np.linspace(0, 20, 1000)
    # lambda a allows me to declare the variable a as independent so that
    # I can easily change the value later
    y = lambda a: (
        np.sqrt(2 / np.pi)
        * ((x**2) * (np.e ** ((-((x) ** 2)) / (2 * a**2)) / (a**3)))
    )

    # Assigning 3 different y functions, each with
    # the required values for a
    y1 = y(1)
    y2 = y(2)
    y3 = y(5)

    # Plotting all functions within the same graph
    ax.plot(x, y1, color="black", label="a = 1")
    ax.plot(x, y2, color="blue", label="a = 2")
    ax.plot(x, y3, color="red", label="a = 5")
    # Assigning the legend to the top right corner
    ax.legend(loc="upper right")

    ax.grid()

    ax.set_title(f"Probability Density Function")
    ax.set_xlabel("x")
    ax.set_ylabel("P(x)")


# Typical main function
def main():

    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
