#!/usr/bin/env python3
# maze_adjacency.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection, PatchCollection
from matplotlib.patches import Rectangle
import pickle
import os
import sys


def link_cells(adj, y1, x1, y2, x2):
    cell1 = y1 * 10 + x1
    cell2 = y2 * 10 + x2
    adj[cell1, cell2] = True
    adj[cell2, cell1] = True


def init_adjmat(maze):
    adj = np.zeros(10000, dtype=bool).reshape((100, 100))
    for y in range(10):
        for x in range(10):
            cell = maze[y, x]
            if y > 0:
                if cell & 1 != 1:
                    link_cells(adj, y, x, y - 1, x)
            if y < 9:
                if cell & 4 != 4:
                    link_cells(adj, y, x, y + 1, x)
            if x < 9:
                if cell & 2 != 2:
                    link_cells(adj, y, x, y, x + 1)
            if x > 0:
                if cell & 8 != 8:
                    link_cells(adj, y, x, y, x - 1)

    return adj


def max_steps(adj_matrix):
    adj = np.copy(adj_matrix)
    steps = 0
    # Keep multiplying until the entrance and exit are "linked"
    while adj[0, 99] == False & adj[99, 0] == False:
        # Use @ operator for matrix multiplication
        adj = adj @ adj_matrix
        steps += 1
    # Add +2 to max steps, because we need +1 to step into
    # the entrance cell, and another +1 to enter the exit cell
    steps += 2
    return steps


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


def search_maze(maze, steps, step_limit):
    y, x, dir = steps.pop()

    if x == 9 and y == 9:
        steps.append((9, 9, 0))
        return True

    if len(steps) == step_limit:
        return False

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

    # Create boolen adjacency matrix from the wall data
    adj_mat = init_adjmat(maze)

    # Calculate maximum number of allowed steps along shortest path
    step_limit = max_steps(adj_mat)

    while not search_maze(maze, steps, step_limit):
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
