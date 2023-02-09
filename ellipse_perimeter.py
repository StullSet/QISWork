#!/usr/bin/env python3
# ellipse_perimeter.py

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import sys
import os

# Defining the differential unit of arc length on the perimeter of
# the ellipse at the passed-in value for theta
def d_s(theta, a, b):
    return np.sqrt(np.power(a * np.sin(theta), 2) + np.power(b * np.cos(theta), 2))


# Defining Ramanujuan's estimate
def ram(a, b):
    h = (a - b) / (a + b)
    return (a + b) * (1 + 3 * h / (10 + np.sqrt(4 - 3 * h))) * np.pi


def fit_quadratic(vec_x, vec_y):
    print(vec_x.shape)
    vec_x = vec_x.reshape(-1, 1)  # Make a column vector
    print(vec_x.shape)
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    transformer.fit(vec_x)
    vec_x_ = transformer.transform(vec_x)
    model = LinearRegression().fit(vec_x_, vec_y)
    b, a = model.coef_
    c = model.intercept_
    return a, b, c


def plot_p(ax):
    ax.plot(range(len(p)), p, label="Integral")
    ax.plot(range(len(r)), r, label="Ramanujan")
    ax.set_title("Numerical Ellipse Perimeter Estimate")
    ax.set_xlabel("b")
    ax.set_ylabel("Perimeter")
    ax.legend(loc="best")
    ax.set_xlim(1, len(p) - 1)


def plot_err(ax):
    ax.scatter(range(len(e)), e, color="red")
    ax.set_title("Ramanujan's Estimate Relative Error")
    ax.set_xlabel("b")
    ax.set_ylabel("Relative Error")
    ax.set_xlim(1, len(e) - 1)


def plot_fit(ax):
    global fa, fb, fc
    ax.scatter(range(len(e)), e, color="red")
    x = np.linspace(0, len(e) - 1, 500)
    ax.plot(x, fa * x**2 + fb * x + fc)
    ax.set_title("Ramanujan's Error (Quadratic Fit)")
    ax.set_xlabel("b")
    ax.set_ylabel("Relative Error")
    ax.set_xlim(1, len(e) - 1)


def plot_fix(ax):
    ax.plot(range(len(p)), p, label="Integral")
    ax.plot(range(len(f)), f, label="Adjusted")
    ax.set_title("Ramanujan's Perimeter Estimate (Adjusted)")
    ax.set_xlabel("b")
    ax.set_ylabel("Perimeter")
    ax.legend(loc="best")
    ax.set_xlim(1, len(f) - 1)


def main():
    global p, r, e, f, fa, fb, fc
    a = 100
    p, r, e, f = np.zeros(21), np.zeros(21), np.zeros(21), np.zeros(21)

    for b, _ in enumerate(p):
        p[b] = scipy.integrate.quad(d_s, 0, 2 * np.pi, args=(a, b))[0]
        r[b] = ram(a, b)
        e[b] = np.abs((r[b] - p[b]) / r[b])

    fa, fb, fc = fit_quadratic(np.arange(len(e)), e)

    print(f"{'b':>3}{'Perimeter':>10}{'Ramanujan':>11}{'Error':>10}{'Adjusted':>10}")
    for b, _ in enumerate(p):
        f[b] = r[b] - r[b] * (fa * b**2 + fb * b + fc)
        print(f"{b:>3}{p[b]:>10.3f}{r[b]:>11.3f}{e[b]:>10.6f}{f[b]:>10.3f}")

    fig = plt.figure(os.path.basename(sys.argv[0]), constrained_layout=True)

    gs = fig.add_gridspec(2, 2)
    plot_p(fig.add_subplot(gs[0, 0]))
    plot_err(fig.add_subplot(gs[0, 1]))
    plot_fit(fig.add_subplot(gs[1, 0]))
    plot_fix(fig.add_subplot(gs[1, 1]))

    plt.show()


if __name__ == "__main__":
    main()
