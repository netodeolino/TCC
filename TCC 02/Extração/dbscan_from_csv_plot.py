# -*- coding: utf-8 -*-
"""
===================================
Demo of DBSCAN clustering algorithm
===================================

Finds core samples of high density and expands clusters from them.

"""
print(__doc__)

import numpy as np
import pandas

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from collections import defaultdict

# #############################################################################
# Read the file CSV and save in frame
dataFrame = pandas.read_csv("./jan-crimes.csv")
novoFrame = dataFrame.copy()

X = []

for i, row in dataFrame.iterrows():
  if row['LONGITUDE'] != "null":
    X.append([float(row['LATITUDE']), float(row['LONGITUDE'])])
    #print (row['LONGITUDE'], row['LATITUDE'])

#X = StandardScaler().fit_transform(X)
X = np.asmatrix(X)

# #############################################################################
# define the number of kilometers in one radian
kms_per_radian = 6371.0088

# define epsilon and min_samples; converted epsilon to radians for use by haversine
epsilon = 0.5 / kms_per_radian
minimo_samples = 5

# Compute DBSCAN
db = DBSCAN(eps=epsilon, min_samples=minimo_samples, metric='haversine').fit(np.radians(X))
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

listaFlor = []
for a in labels:
	listaFlor.append(a)
	#print (a)

# #############################################################################
# Save the cluster_id in new column in CSV file
novoFrame["CLUSTER"] = pandas.Series(listaFlor)
novoFrame.to_csv("./eps="+str(epsilon*kms_per_radian)+"min_samples="+str(minimo_samples)+"-janeiro.csv", index=False)

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

# #############################################################################
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
    
    xy = X[class_member_mask & core_samples_mask]

    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)

    xy = X[class_member_mask & ~core_samples_mask]
    
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
