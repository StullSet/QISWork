#!/usr/bin/env python3
# ifs_triangle.py

from simple_screen import SimpleScreen
from ifs import IteratedFunctionSystem

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
    p = 1 / 3
    ifs.add_mapping(0, 0, 15, 0, 0, 15, "blue", p)
    ifs.add_mapping(15, 0, 30, 0, 15, 15, "green", p)
    ifs.add_mapping(7.5, 15, 22.5, 15, 7.5, 30, "red", p)

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
