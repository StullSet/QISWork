#!/usr/bin/env python3
# eulers_constant.py

import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt
import sys
import os

# Defining my euler equation
def euler_eq(x):
    return np.log(np.log(1 / x))


# Calculating the euler constant
def euler_cons():
    # Using scipy.integrate to easily calculate the value
    return (scipy.integrate.quad(euler_eq, 0, 1)[0]) * (-1)


# Creating a step function that produces a list of the first 50
# values in the harmonic series
def harmonic_num(steps):
    seq = [0]
    for n in range(1, steps + 1):
        seq.append(1 / n + seq[-1])
    return seq[1:]


def plot(ax):
    # Plotting the estimate based on ln(x) + the calculated euler constant
    x_est = np.linspace(1, 51)
    y_est = euler_cons() + np.log(x_est)
    ax.plot(x_est, y_est)

    # Plotting the step function for the first 50 Harmonic values
    x = np.linspace(1, 51)
    y = harmonic_num(50)
    plt.step(x, y)

    ax.set_title(f"Harmonic Numbers")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.grid()
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")


# Standard main() function
def main():
    # PRinting the calculated euler constant
    print(f"Euler's constant has been calculated to be: {euler_cons()}")

    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
