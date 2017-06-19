# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 09:28:25 2017

@author: zainabhabas
"""

import numpy as np 
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets.samples_generator import make_blobs
from sklearn.decomposition import PCA

f = open("/Users/zainabhabas/Documents/workspace/Comprendre-et-raisonner-pour-un-personnage-virtuel/numberbatch-en-17.04b.txt", "r",encoding='UTF8')

#f= open('C:\\Users\\cleme\\Desktop\\test.txt','r',encoding='UTF8')

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
    
pca = PCA(n_components=50)
pca.fit(coordinates)
print(pca.explained_variance_ratio_)
    
    
X, _ = make_blobs(n_samples=i, centers=coordinates, cluster_std=0.6)

bandwidth = estimate_bandwidth(X, quantile = 0.2 , n_samples = i)




ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)

print("number of estimated clusters : %d" % n_clusters_)

