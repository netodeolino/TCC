# -*- coding: utf-8 -*-

import numpy as np
import pandas

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from collections import defaultdict

class Cluster(object):

  def printLabels(self, labels, matrixLatLng, core_samples_mask):
    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    # Plot result
    import matplotlib.pyplot as plt

    # Black removed and is used for noise instead.
    unique_labels = set(labels)

    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, len(unique_labels))]

    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]

        class_member_mask = (labels == k)
        
        xy = matrixLatLng[class_member_mask & core_samples_mask]

        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=14)

        xy = matrixLatLng[class_member_mask & ~core_samples_mask]
        
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=6)

    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()


  def main(self, fileName, newFileName, lat, lng, eps, minPoints):
    dataFrame = pandas.read_csv("./" + fileName + ".csv")
    novoFrame = dataFrame.copy()

    X = []
    for i, row in dataFrame.iterrows():
      if row[lng] != "null":
        X.append([float(row[lat]), float(row[lng])])

    X = np.asmatrix(X)

    # define the number of kilometers in one radian
    kms_per_radian = 6371.0088

    # define epsilon and min_samples; converted epsilon to radians for use by haversine
    epsilon = eps / kms_per_radian

    # Compute DBSCAN
    db = DBSCAN(eps=epsilon, min_samples=minPoints, metric='haversine').fit(np.radians(X))
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    labelsList = []
    for a in labels:
    	labelsList.append(a)

    novoFrame["CLUSTER"] = pandas.Series(labelsList)
    novoFrame.to_csv("./" + newFileName + ".csv", index=False)

    self.printLabels(labels, X, core_samples_mask)

if __name__ == '__main__':
  cl = Cluster()
  cl.main("jan-crimes", "cluster-janeiro", "LATITUDE", "LONGITUDE", 0.5, 5)