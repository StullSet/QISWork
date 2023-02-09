#!/usr/bin/env python3
# maze_draw.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection, PatchCollection
from matplotlib.patches import Rectangle
import pickle
import os
import sys


def load_maze(file_name):
    maze = np.genfromtxt(file_name, delimiter=",", dtype=np.int)
    print(maze)
    return maze


def validate_maze(maze):
    for y in range(10):
        for x in range(10):
            cell = maze[y, x]
            # Check CSV has a value in every cell
            if cell == -1:
                print(f"Cell {y, x} has no value")
                return False
            # Check for any holes in border walls of maze
            if y == 0 and not cell & 1 == 1:
                print(f"Cell {y, x} is missing the NORTH wall")
                return False
            if x == 9 and not cell & 2 == 2:
                print(f"Cell {y, x} is missing the EAST wall")
                return False
            if y == 9 and not cell & 4 == 4:
                print(f"Cell {y, x} is missing the SOUTH wall")
                return False
            if x == 0 and not cell & 8 == 8:
                print(f"Cell {y, x} is missing the WEST wall")
                return False
            # Check every cell agrees with its NORTH cell
            if y > 0:
                cell2 = maze[y - 1, x]
                if (cell & 1 == 1 and cell2 & 4 != 4) or (
                    cell & 1 != 1 and cell2 & 4 == 4
                ):
                    print(
                        f"Cell {y, x} and cell {y - 1, x}"
                        f" do not agree between NORTH/SOUTH"
                    )
                    return False
            # Check every cell agrees with its SOUTH cell
            if y < 9:
                cell2 = maze[y + 1, x]
                if (cell & 4 == 4 and cell2 & 1 != 1) or (
                    cell & 4 != 4 and cell2 & 1 == 1
                ):
                    print(
                        f"Cell {y, x} and cell {y + 1, x}"
                        f" do not agree between NORTH/SOUTH"
                    )
                    return False
            # Check every cell agrees with its EAST cell
            if x < 9:
                cell2 = maze[y, x + 1]
                if (cell & 2 == 2 and cell2 & 8 != 8) or (
                    cell & 2 != 2 and cell2 & 8 == 8
                ):
                    print(
                        f"Cell {y, x} and cell {y, x + 1}"
                        f" do not agree between EAST/WEST"
                    )
                    return False
            # Check every cell agrees with its WEST cell
            if x > 0:
                cell2 = maze[y, x - 1]
                if (cell & 8 == 8 and cell2 & 2 != 2) or (
                    cell & 8 != 8 and cell2 & 2 == 2
                ):
                    print(
                        f"Cell {y, x} and cell {y, x - 1}"
                        f" do not agree between EAST/WEST"
                    )
                    return False
    return True


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


def plot_maze(ax, file_name, maze):
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_xlim(-5, 105)
    ax.set_ylim(-5, 105)
    base = os.path.basename(file_name)
    maze_name = os.path.splitext(base)[0]
    ax.set_title(f"{maze_name}")

    # Plot enter and exit cells
    entrance = Rectangle((0, 90), 10, 10)
    ax.add_collection(PatchCollection([entrance], facecolor="tan"))
    exit = Rectangle((90, 0), 10, 10)
    ax.add_collection(PatchCollection([exit], facecolor="orange"))

    # Plot cell corner circles
    for x in range(0, 110, 10):
        for y in range(0, 110, 10):
            ax.scatter(x, y, color="black")

    plot_cell_walls(ax, maze)


def main(file_name):
    maze = load_maze(file_name)

    if not validate_maze(maze):
        return

    fig = plt.figure(file_name)
    fig.set_size_inches(8, 8)
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])

    with open(file_name + ".pickle", "wb") as file_out:
        pickle.dump(maze, file_out, pickle.HIGHEST_PROTOCOL)

    plot_maze(ax, file_name, maze)

    plt.show()


if __name__ == "__main__":
    file_name = None
    if len(sys.argv) == 1:
        file_name = os.path.dirname(sys.argv[0]) + "/maze2.csv"
    else:
        file_name = sys.argv[1]

    main(file_name)
