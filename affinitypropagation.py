# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 17:19:29 2017

@author: zainabhabas
"""

from sklearn.cluster import AffinityPropagation
from sklearn import metrics

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
    #print(i)
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
    
af = AffinityPropagation().fit(coordinates)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)

print('Estimated number of clusters: %d' % n_clusters_)
"""print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels, metric='sqeuclidean'))"""