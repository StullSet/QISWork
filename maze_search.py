#!/usr/bin/env python3
# maze_search.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection, PatchCollection
from matplotlib.patches import Rectangle
import pickle
import os
import sys


def plot_cell_walls(ax, maze):
    for y in range(10):
        bottom = (9 - y) * 10
        top = bottom + 10
        for x in range(10):
            left = x * 10
            right = left + 10
            cell = maze[y, x]
            if cell & 1 == 1:
                lc = LineCollection(
                    [[(left, top), (right, top)]], color="black", linewidth=3
                )
                ax.add_collection(lc)
            if cell & 2 == 2:
                lc = LineCollection(
                    [[(right, bottom), (right, top)]], color="black", linewidth=3
                )
                ax.add_collection(lc)
            if cell & 4 == 4:
                lc = LineCollection(
                    [[(left, bottom), (right, bottom)]], color="black", linewidth=3
                )
                ax.add_collection(lc)
            if cell & 8 == 8:
                lc = LineCollection(
                    [[(left, bottom), (left, top)]], color="black", linewidth=3
                )
                ax.add_collection(lc)


def plot_steps(ax, steps):
    for s in steps:
        y, x, _ = s
        bottom = (9 - y) * 10
        left = x * 10
        patch = Rectangle((left + 4, bottom + 4), 2, 2)
        ax.add_collection(PatchCollection([patch], facecolor="blue"))


def plot_maze(ax, file_name, maze, steps):
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_xlim(-5, 105)
    ax.set_ylim(-5, 105)
    base = os.path.basename(file_name)
    maze_name = os.path.splitext(base)[0]
    ax.set_title(f"{maze_name} ({len(steps)} steps)")

    # Plot enter and exit cells
    entrance = Rectangle((0, 90), 10, 10)
    ax.add_collection(PatchCollection([entrance], facecolor="tan"))
    exit = Rectangle((90, 0), 10, 10)
    ax.add_collection(PatchCollection([exit], facecolor="orange"))

    # Plot cell corner circles
    for x in range(0, 110, 10):
        for y in range(0, 110, 10):
            ax.scatter(x, y, color="black")

    plot_steps(ax, steps)

    plot_cell_walls(ax, maze)


def in_path(steps, y, x):
    for s in reversed(steps):
        sy, sx, _ = s
        if sy == y and sx == x:
            return True
    return False


def search_maze(maze, steps):
    y, x, dir = steps.pop()

    if x == 9 and y == 9:
        steps.append((9, 9, 0))
        return True

    if dir == 0:
        steps.append((y, x, 1))
        if maze[y, x] & 1 != 1:
            if not in_path(steps, y - 1, x):
                steps.append((y - 1, x, 0))
        return False

    if dir == 1:
        steps.append((y, x, 2))
        if maze[y, x] & 2 != 2:
            if not in_path(steps, y, x + 1):
                steps.append((y, x + 1, 0))
        return False

    if dir == 2:
        steps.append((y, x, 4))
        if maze[y, x] & 4 != 4:
            if not in_path(steps, y + 1, x):
                steps.append((y + 1, x, 0))
        return False

    if dir == 4:
        steps.append((y, x, 8))
        if maze[y, x] & 8 != 8:
            if not in_path(steps, y, x - 1):
                steps.append((y, x - 1, 0))
        return False

    return False


def main(file_name):
    global total_steps
    total_steps = 0
    with open(file_name + ".pickle", "rb") as file_in:
        maze = pickle.load(file_in)

    # Steps is list of tuples, where each tuple contains the
    # (y, x, last direction tried) for each step along current path
    steps = [(0, 0, 0)]

    while not search_maze(maze, steps):
        pass

    fig = plt.figure(file_name)
    fig.set_size_inches(8, 8)
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])

    plot_maze(ax, file_name, maze, steps)

    plt.show()


if __name__ == "__main__":
    file_name = None
    if len(sys.argv) == 1:
        file_name = os.path.dirname(sys.argv[0]) + "/maze2.csv"
    else:
        file_name = sys.argv[1]

    main(file_name)
