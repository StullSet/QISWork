#!/usr/bin/env python3
# identify_element.py

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import sys
import os

# PV = nRT -> PV-nRT = 0
# Unknown = n

# Global Variables
p = 2  # ATM
R = 8.31  # J/mol K
M = 0.050  # kg


def linear_fit(vec_x, vec_y):
    vec_x = vec_x.reshape(-1, 1)
    model = LinearRegression().fit(vec_x, vec_y)
    m = model.coef_
    b = model.intercept_
    return m, b


def plot(ax):
    # Converting all given data to correct units
    vec_celsius = np.array([-50.0, 0.0, 50.0, 100.0, 150.0])
    vec_kelvin = vec_celsius + 273.15

    vec_liters = np.array([11.6, 14.0, 16.2, 19.4, 21.8])
    vec_meter_cubed = vec_liters / 1000

    x = np.linspace(0, 500, 1000)

    # Unpacking tuple
    m, b = linear_fit(vec_kelvin, vec_meter_cubed)

    # Defining line of best fit
    y = m * x + b

    # Calculating molar mass
    n = ((p * 101325) / R) * m
    molar_mass = M / n

    # Plotting given points and line of best fit
    ax.scatter(vec_kelvin, vec_meter_cubed, color="red")
    ax.plot(x, y)

    ax.set_title(f" Argon Gas")
    ax.set_xlabel("Temperature")
    ax.set_ylabel("Volume")


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()

    # print(f"The molar mass is {molar_mass}")


if __name__ == "__main__":
    main()
