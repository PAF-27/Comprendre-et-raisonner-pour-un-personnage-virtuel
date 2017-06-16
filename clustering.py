# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:34:06 2017

@author: zainabhabas
"""

import numpy as np 
from sklearn.cluster import KMeans

fp = open("/Users/zainabhabas/Documents/workspace/Comprendre-et-raisonner-pour-un-personnage-virtuel/numberbatch-en-17.04b.txt", "r",encoding='UTF8')

words = []
coordinates = {}
i = 0

for line in fp:
    
    t = line.split()
    print(t)
    words = words + [t[0]]
    print(words)
    coordinates[i] = t[1:300]
    i+=i
         
fp.close()

X = np.matrix(zip(words, coordinates))

kmeans = KMeans(n_clusters=30, random_state=0).fit(X)