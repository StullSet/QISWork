#!/usr/bin/env python3
# lattice_circle.py

import numpy as np
from numba import jit

# See https://en.wikipedia.org/wiki/Gauss_circle_problem

# Compiling the function to machine language
@jit(nopython=True)
def lattice_points(radius):
    num_points = 0
    radius_squared = radius**2
    # x and y values range across the diameter
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            # Using distance formula to determine if inside the circle
            if x**2 + y**2 <= radius_squared:
                # Increase count by 1
                num_points += 1
    return num_points


def main():
    for radius in range(1000, 10001, 1000):
        # Calling the helper program
        act_points = lattice_points(radius)
        # Calculating the gaussian estimate
        est_points = int(np.pi * radius**2 + 2 * np.sqrt(2 * np.pi * radius))
        print(
            f"Radius = {radius:>6,}"
            f"  Act Points = {act_points:>12,}"
            f"  Est Points = {est_points:>12,}"
            # Relative error because we're accepting negative error as well
            f"  % Rel. Err = {(act_points - est_points)/est_points:0.4%}"
        )


if __name__ == "__main__":
    main()
