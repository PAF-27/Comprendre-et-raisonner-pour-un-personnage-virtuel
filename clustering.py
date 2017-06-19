# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:34:06 2017

@author: zainabhabas
"""

import numpy as np 
from sklearn.cluster import KMeans



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



def distance(n, x, y):
    res=0
    for i in range(n):
         res=res+abs(float(x[i])-float(y[i]))
    return res
    
    
    
n=10
kmeans = KMeans(n_clusters=n, random_state=0).fit(coordinates)
print(kmeans.labels_)
print(kmeans.cluster_centers_)
clustersParMots=[]
clustersParValeurs=[]

for i in range (n):
    listeClusterIParMots=[]
    listeClusterIParValeurs=[]
    for j in range(len(kmeans.labels_)) :
        if kmeans.labels_[j]==i:
            listeClusterIParMots.append(words[j])
            listeClusterIParValeurs.append(coordinates[j])
    clustersParValeurs.append(listeClusterIParValeurs)
    clustersParMots.append(listeClusterIParMots)
    
print(clustersParMots)
minimum=[]
positionCentre=[0 for i in range(n)]
distanceMoyenne=[0 for i in range(n)]
for i in range(n):
    minimum.append(distance(300, clustersParValeurs[i][0], kmeans.cluster_centers_[i]))
    for j in range(len(clustersParValeurs[i])):
        distanceTmp=distance(300,clustersParValeurs[i][j],kmeans.cluster_centers_[i])
        if distanceTmp<minimum[i]:
            positionCentre[i]=j
        distanceMoyenne[i]=distanceMoyenne[i]+distanceTmp
    distanceMoyenne[i]=distanceMoyenne[i]/len(clustersParValeurs[i])
print(distanceMoyenne)
print(positionCentre)
centreString=""
for i in range(n):
    centreString=centreString+" "+words[positionCentre[i]]
print(centreString)