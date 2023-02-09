#!/usr/bin/env python3
# adaptive_quadrature.py

import time


def f(x):
    # This is the function we are numerically integrating
    return 5 * pow(x, 3) - 9 * pow(x, 2) + 11


def F(x):
    # This is the exact analytic integral of our function
    return 5 * pow(x, 4) / 4 - 3 * pow(x, 3) + 11 * x


# Defining the standard process for a fixed midpoint rule
def midpoint_fixed(a, b):
    x = a
    dx = (b - a) / 1e6
    area = 0
    while x < b:
        area += f(x + dx / 2) * dx
        x += dx
    return area


# Defining the process for the adaptive midpoint rule
# See slides for a more elaborate explanation
def midpoint_adaptive(a, b):
    x = a
    dx = 1
    area = 0
    while x < b:
        f1 = f(x)
        f2 = f(x + dx)
        # Keep halving dx if current delta is too great
        while abs((f2 - f1) / f1) > 1e-3:
            dx /= 2
            f2 = f(x + dx)
        # Use the midpoint rule
        area += f(x + dx / 2) * dx
        x += dx
        # Expand current interval width
        dx *= 2
    return area


def main():
    a = 0
    b = 10

    area_actual = F(b) - F(a)
    print(f"\nExact integral using analytic calculus = {area_actual}")
    print()

    # Taking the current processor time
    start_time = time.process_time()
    # Calculating the values based on a fixed delta x
    area_fixed = midpoint_fixed(a, b)
    elapsed_time = time.process_time() - start_time
    err = (area_fixed - area_actual) / area_actual * 100
    # Printing the results and the time it took
    print(f"Estimated integral using fixed width midpoint rule = {area_fixed}")
    print(f"Fixed width midpoint rule error = {err:.8f}")
    print(f"Time (sec) Fixed = {elapsed_time:.3f}")
    print()

    # Following the same process with an adaptive delta x
    start_time = time.process_time()
    area_adaptive = midpoint_adaptive(a, b)
    elapsed_time = time.process_time() - start_time
    err = (area_adaptive - area_actual) / area_actual * 100
    print(f"Estimated integral using adaptive width midpoint rule = {area_adaptive}")
    print(f"Adaptive width midpoint rule error = {err:.8f}")
    print(f"Time (sec) Adaptive = {elapsed_time:.3f}")
    print()


if __name__ == "__main__":
    main()
