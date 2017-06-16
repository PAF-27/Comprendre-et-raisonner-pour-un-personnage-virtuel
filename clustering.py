# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:34:06 2017

@author: zainabhabas
"""

import numpy as np 
from sklearn.cluster import KMeans

f= open('C:\\Users\\cleme\\numberbatch-en-17.04b.txt','r',encoding='UTF8')
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
#X=zip(words, coordinates)
#Y = np.matrix(X)
kmeans = KMeans(n_clusters=2, random_state=0).fit(coordinates)
print(kmeans.labels_)
print(kmeans.cluster_centers_)