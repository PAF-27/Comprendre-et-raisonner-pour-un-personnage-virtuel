# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 09:28:25 2017

@author: zainabhabas
"""

import numpy as np 
from sklearn.cluster import MeanShift, estimate_bandwidth

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
    
    


bandwidth = estimate_bandwidth(np.asarray(coordinates) ,quantile =0.5)
ms = MeanShift(bandwidth=bandwidth)

ms.fit(coordinates)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
print(cluster_centers)
labels_unique = np.unique(labels)
print(labels_unique)
n_clusters_ = len(labels_unique)

print("number of estimated clusters : %d" % n_clusters_)

