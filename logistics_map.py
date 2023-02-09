#!/usr/bin/env python3
# logistics_map.py

import numpy as np

# Importing the created SimpleScreen function so that we can code in world coordinates
# While this function converts into screen coordinates
# Which tells python how to run based on our unique screen dimensions
from simple_screen import SimpleScreen


def plot_logistics_map(ss):
    for sx in range(ss.screen_width):
        # COnverting from screen to world for us to easily provide inputs
        x = ss.world_x(sx)
        y = np.random.random()

        # Iterate (but don't draw) to reach a stable orbit
        for i in range(500):
            y = x * y * (1 - y)

        # Looping through 500 times again and plotting the values
        for i in range(500):
            y = x * y * (1 - y)
            ss.set_world_pixel(x, y, "blue")


def main():
    ss = SimpleScreen(
        # (x_min, y_min), (x_max, y_max)
        world_rect=((2.5, 0), (4.0, 1)),
        # Calling the function to draw
        draw_function=plot_logistics_map,
        screen_size=(900, 900),
        title="Logistics Map",
    )
    ss.show()


if __name__ == "__main__":
    main()
