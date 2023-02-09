#!/usr/bin/env python3
# binomial_distribution.py

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy.stats import binom
import sys
import os


def plot(ax):
    # n = Number of trials
    n = 50

    # List of integers from 0 to n (inclusive)
    r_values = list(range(n + 1))

    # Use list comprehension to get scipy.binom.pmf for each r_value
    # for the given probabilities p=.3, p=.5, p=.9
    dist1 = [binom.pmf(r, n, 0.30) for r in r_values]
    dist2 = [binom.pmf(r, n, 0.50) for r in r_values]
    dist3 = [binom.pmf(r, n, 0.90) for r in r_values]

    # Use matplotlib bar plot to show each r_value
    # with its associated probability of occurrence
    plt.bar(r_values, dist1, label="p = 0.3")
    plt.bar(r_values, dist2, label="p = 0.5")
    plt.bar(r_values, dist3, label="p = 0.9")

    ax.set_title(f"Binomial Distribution (n={n} trials)")
    ax.set_xlabel("Number of Successes")
    ax.set_ylabel("Probability")

    ax.legend(loc="upper right")

    ax.xaxis.set_major_locator(MultipleLocator(5))


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
