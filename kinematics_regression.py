#!/usr/bin/env python3
# kinematics_regression.py


import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import os
import sys


def fit_quadratic(vec_x, vec_y):
    vec_x = vec_x.reshape(-1, 1)
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    transformer.fit(vec_x)
    vec_x_ = transformer.transform(vec_x)
    model = LinearRegression().fit(vec_x_, vec_y)
    b, a = model.coef_
    c = model.intercept_
    return a, b, c


def plot(ax):
    # Passing in a file name and extracting the values to analyze
    file_name = os.path.dirname(sys.argv[0]) + "/kinematics_regression.csv"
    data = np.genfromtxt(file_name, delimiter=",")

    vec_x = data[:, 0]
    vec_y = data[:, 1]

    a, b, c = fit_quadratic(vec_x, vec_y)

    acceleration = a * 2
    initial_velocity = b

    print(f"Constant acceleration = {acceleration:.4f} m/s^2")
    print(f"     Initial velocity = {initial_velocity:.4f} m/s")

    x = np.linspace(np.min(vec_x), np.max(vec_x), 1000)
    ax.plot(x, a * x**2 + b * x + c)

    ax.scatter(vec_x, vec_y, color="red")

    ax.set_title("Newtonian Kinematics")
    ax.set_xlabel("Time (sec)")
    ax.set_ylabel("Distance (m)")


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
