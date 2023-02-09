#!/usr/bin/env python3
# benfords_law.py

import numpy as np
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import random
import sys
import os


def p_MSD():
    # Calculating the most significant digit
    p = np.zeros(10)
    for val in range(100_000):
        # Creating our very large values to analyze
        n = random.randint(1, 1_000_000) ** 100
        # Convert the number into a string, and pull the first element
        # As the MSD and increasing the count for that digit by 1
        p[int(str(n)[0])] += 1
    p = p[1:]
    # Normalizing the values
    p = p / 100_000
    return p


def plot(ax):
    # Grouping the values into buckets that range from 1 to 9
    # Based on the results from the p_MSD() helper function
    ax.bar(range(1, 10), p_MSD(), zorder=2.0)
    ax.grid()

    ax.set_title(f"Benford's Law")
    ax.set_xlabel("Most Significant Digit")
    ax.set_ylabel("Probability")

    ax.xaxis.set_major_locator(MultipleLocator(1))


# Typical main function
def main():
    random.seed(2022)

    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
