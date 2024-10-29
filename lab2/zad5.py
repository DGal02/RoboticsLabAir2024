from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt


def task5(clusters, x_vals=True):
    x = np.random.normal(loc=0, scale=1, size=1000)
    y = np.random.normal(loc=0, scale=1, size=1000)
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)

    K_object = KMeans(n_clusters=clusters)
    if x_vals:
        K_object.fit(x)
    else:
        K_object.fit(y)
    x_labels = K_object.labels_

    plt.figure()
    plt.scatter(x, y, c=x_labels)
    plt.show()


task5(3, True)
task5(2, True)
task5(3, False)
task5(5, False)
