#!/usr/bin/env python3
# quadratic_regression_sklearn.py


import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import sys
import os


def fit_linear(vec_x, vec_y):
    # sklearn expects vectors to be 2d, this command allows us to produce this
    vec_x = vec_x.reshape(-1, 1)
    # Calling sklearn's built in function to perform the work for us
    model = LinearRegression().fit(vec_x, vec_y)
    # Defining the variables within the provided tuple
    m = model.coef_
    b = model.intercept_
    return m, b


def fit_quadratic(vec_x, vec_y):
    vec_x = vec_x.reshape(-1, 1)
    # This syntax here allows us to limit round off error so that the x values
    # are in a relatively closer range to the y values
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    transformer.fit(vec_x)
    vec_x_ = transformer.transform(vec_x)
    model = LinearRegression().fit(vec_x_, vec_y)
    b, a = model.coef_
    c = model.intercept_
    return a, b, c


def f(a, b, c, x):
    return a * x**2 + b * x + c


def plot(ax):
    vec_x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    vec_y = np.array([205, 430, 677, 945, 1233, 1542, 1872, 2224])

    x = np.linspace(np.min(vec_x), np.max(vec_x), 1000)

    a, b, c = fit_quadratic(vec_x, vec_y)
    ax.plot(x, a * x**2 + b * x + c, label="Quadratic")

    print(f"y = ({a:.4f})x^2 + ({b:.4f})x + ({c:.4})")
    print(f"Tape counter at 65 mins = {f(a,b,c,6.5):,.4f}")

    m, b = fit_linear(vec_x, vec_y)
    ax.plot(x, m * x + b, label="Linear")

    ax.scatter(vec_x, vec_y, color="red")

    ax.set_title("Tape Counter Per Minute")
    ax.set_xlabel("Elapsed time x10 (min)")
    ax.set_ylabel("Tape Counter")
    ax.legend()


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
