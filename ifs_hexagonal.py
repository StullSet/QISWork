#!/usr/bin/env python3
# ifs_hexagonal.py

from simple_screen import SimpleScreen
from ifs import IteratedFunctionSystem
import numpy as np

ifs = IteratedFunctionSystem()


def plot_ifs(ss):
    iterations = 200_000
    x, y = 0, 0

    # Iterate (but don't draw) to let IFS reach its stable orbit
    # As a test
    for _ in range(100):
        x, y, color = ifs.transform_point(x, y)

    # Drawing over desired number of iterations
    for _ in range(iterations):
        x, y, color = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, color)


def main():
    # Setting base frame size
    ifs.set_base_frame(0, 0, 30, 30)

    # Creating equal probability for each mapping
    p = 1 / 6
    # Splitting the equilateral triangles into 30-60-90 triangles
    # Using the geometry of a 30-60-90 triangle to calculate the points
    # COD
    ifs.add_mapping(25, 15, 15, 15, 20, 15 + 5 * np.sqrt(3), "blue", p)
    # DOE
    ifs.add_mapping(20, 15 + 5 * np.sqrt(3), 15, 15, 10, 15 + 5 * np.sqrt(3), "blue", p)
    # EOF
    ifs.add_mapping(10, 15 + 5 * np.sqrt(3), 15, 15, 5, 15, "blue", p)
    # FOA
    ifs.add_mapping(5, 15, 15, 15, 10, 15 - 5 * np.sqrt(3), "blue", p)
    # AOB
    ifs.add_mapping(10, 15 - 5 * np.sqrt(3), 15, 15, 20, 15 - 5 * np.sqrt(3), "blue", p)
    # BOC
    ifs.add_mapping(20, 15 - 5 * np.sqrt(3), 15, 15, 25, 15, "blu", p)

    # Solves the linear algebra for the transformation matrix
    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="Sierpinksi Triangle",
    )
    ss.show()


if __name__ == "__main__":
    main()
