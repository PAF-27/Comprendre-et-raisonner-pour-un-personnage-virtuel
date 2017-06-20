# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 09:28:25 2017

@author: zainabhabas
"""

import numpy as np 
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets.samples_generator import make_blobs
from sklearn.decomposition import PCA

f= open("/Users/zainabhabas/Documents/workspace/Comprendre-et-raisonner-pour-un-personnage-virtuel/resultat.txt",'r',encoding='UTF8')
words=[]
tmp=[]
coordinates=[]
f.readline()
tmp2=[]
i=0
for line in f:
    t=line.split()
    i=i+1
    print(i)
    for j in range (1, len(t)) :
        string=t[j]
        if string.startswith('-'):
            string=string.replace('-','')
            float(string)
            t[j]=-float(string)
        else :
            t[j]=float(string)
    words.append(t[0])
    tmp=t[1:len(t)]
    coordinates.append(tmp)
    
    
#X, _ = make_blobs(n_samples=500, centers=coordinates)

#bandwidth = estimate_bandwidth(X,quantile =0.2,  n_samples = i)

ms = MeanShift()
ms.fit(coordinates)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
print(cluster_centers)
labels_unique = np.unique(labels)
print(labels_unique)
n_clusters_ = len(labels_unique)

print("number of estimated clusters : %d" % n_clusters_)

