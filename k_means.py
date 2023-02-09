#!/usr/bin/env python3
# k_means.py

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Global variables are often shown using all upper case
K_CLUSTERS = 3
INCLUDE_OUTLIERS = True
MEAN_MULTIPLE = 2

# Creating our own data type
class DataPoint:
    # Uses dunder method to declare the constructor for a class
    # using the work init. Must be named this way
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None

    # __repr__ is used to produce a set of characters that can be used somewhere
    # else to recreate the same class
    def __repr__(self):
        return f"DataPoint({self.x}, {self.y})"


class Cluster:
    def __init__(self, index):
        self.index = index
        # Center of mass of the cluster
        self.x = 0.0
        self.y = 0.0
        # Tracking the number of values within the cluster
        self.population = 0
        # Seeing how far on average each point is from the mean/CM
        self.mean_distance = 0.0

        colmap = ("red", "blue", "green", "purple", "yellow", "orange")
        # Assigning color based on the index
        self.color = colmap[index]

    def __repr__(self):
        return f"Cluster({self.index})"


def init_clusters(k):
    # List comprehension where we create and initialize clusters based on the k value
    clusters = [Cluster(i) for i in range(k)]
    return clusters


def init_points(file_name):
    # Storing csv as a 2d array
    samples = np.genfromtxt(f"{file_name}", delimiter=",")
    points = []
    for s in samples:
        # Pass the first and second column into the constructor function
        # and then adding them to our empty list
        point = DataPoint(s[0], s[1])
        points.append(point)
    return points


def init_assign(points, clusters):
    k = len(clusters)
    # Assigning points to a cluster at "random" using the mod operator
    # And then increasing it's population by 1
    for idx, p in enumerate(points):
        c = clusters[idx % k]
        p.cluster = c
        c.population += 1


def reassign(points, clusters):
    converged = True

    # Phase I: Calculate the new geometric mean of each
    # cluster based upon current data point assignments
    for c in clusters:
        new_x, new_y = 0, 0
        for p in points:
            # If a point's c value matches the one we consider
            # Take it's x and y values and add it to new
            if p.cluster == c:
                new_x += p.x
                new_y += p.y
        # Take the mean of the new data
        new_x /= c.population
        new_y /= c.population

        # If anything changed, set converged to False
        if c.x != new_x or c.y != new_y:
            c.x, c.y = new_x, new_y
            converged = False

    # Phase II: Assign data points to nearest cluster
    # phase2_change = False
    for p in points:
        dist_min = sys.float_info.max
        nearest_cluster = None
        for c in clusters:
            # Use np.hypot to find the distance the point to a cluster
            dist = np.hypot(p.x - c.x, p.y - c.y)
            if dist < dist_min:
                # If shorter distance found reassign c
                dist_min = dist
                nearest_cluster = c
        # If the old and new clusters are different
        if nearest_cluster != p.cluster:
            # Move to new cluster unless unless you are the last point
            # Update all counts
            if p.cluster.population > 1:
                p.cluster.population -= 1
                p.cluster = nearest_cluster
                p.cluster.population += 1
                converged = False

    # Phase III - Evict any point too far away from its cluster's center
    if converged and MEAN_MULTIPLE > 0:
        # Calculate mean distance from each cluster's center
        # to the assigned points for that cluster
        for c in clusters:
            total_distance = 0.0
            for p in points:
                if p.cluster == c:
                    total_distance += np.hypot(p.x - c.x, p.y - c.y)
            c.mean_distance = total_distance / c.population

        # Only keep points where the distance to its assigned cluster's
        # center is less than a multiple of that cluster's mean distance
        # to its assigned points
        new_points = []
        for p in points:
            c = p.cluster
            dist = np.hypot(p.x - c.x, p.y - c.y)
            if dist < c.mean_distance * MEAN_MULTIPLE:
                new_points.append(p)
            else:
                if c.population > 1:
                    print(f"Evicted {p} from {c}")
                    c.population -= 1
                    converged = False
        points[:] = new_points

    return converged


def plot(ax, points, clusters):
    ax.set_aspect("equal")
    ax.set_xlim(-5, 45)
    ax.set_ylim(-5, 45)
    ax.set_title(f"k-Means Clustering (k={K_CLUSTERS})")

    for p in points:
        # Producing a scatter plot and then assigning the color based on the cluster it's in
        ax.scatter(p.x, p.y, color=p.cluster.color, alpha=0.5, edgecolor="black")

    for c in clusters:
        # Marking the mean/CM with a square marker
        ax.scatter(c.x, c.y, color=c.color, marker="s")


def on_key_press(event, ax, points, clusters):
    # if n is pressed, run through one step of reassign
    if event.key == "n":
        if reassign(points, clusters):
            # If returned True, then the system is in equilibrium
            print("Cluster has converged!")
        # Otherwise clear the screen, and plot the new graph
        ax.clear()
        plot(ax, points, clusters)
        plt.draw()


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])

    # Callback function for user inputs
    # Every time we hit n, the algorithm will progress
    key_press_event = fig.canvas.mpl_connect(
        "key_press_event", lambda event: on_key_press(event, ax, points, clusters)
    )

    clusters = init_clusters(K_CLUSTERS)

    file_name = os.path.dirname(sys.argv[0]) + "/cluster_samples.csv"
    points = init_points(file_name)

    if not INCLUDE_OUTLIERS:
        # Removes outlier if we aren't using one
        points.pop()

    init_assign(points, clusters)

    plot(ax, points, clusters)

    plt.show()


if __name__ == "__main__":
    main()
