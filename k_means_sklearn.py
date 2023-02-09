#!/usr/bin/env python3
# k_means_sklearn.py


import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import sys
import os

K_CLUSTERS = 3


def plot(ax):
    ax.set_title(f"k-Means Clustering (k={K_CLUSTERS})")
    ax.set_xlim(-5, 45)
    ax.set_ylim(-5, 45)
    ax.set_aspect("equal")

    file_name = os.path.dirname(sys.argv[0]) + "/cluster_samples.csv"
    points = np.genfromtxt(file_name, delimiter=",")
    points = points[:-1, :]

    np.random.seed(2016)
    kmeans = KMeans(K_CLUSTERS)
    kmeans.fit(points)

    y_kmeans = kmeans.predict(points)
    ax.scatter(points[:, 0], points[:, 1], c=y_kmeans)

    centers = kmeans.cluster_centers_
    ax.scatter(centers[:, 0], centers[:, 1], c="black", marker="s")


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
