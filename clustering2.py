# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 14:08:41 2017

@author: zainabhabas
"""

#import numpy as np 
from sklearn.cluster import KMeans
import numpy as np
from sklearn.mixture import GMM

f= open("/Users/zainabhabas/Documents/workspace/Comprendre-et-raisonner-pour-un-personnage-virtuel/resultat.txt",'r',encoding='UTF8')
words=[]
tmp=[]
coordinates=[]


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
    
#extraction des coordonnées des centroids pour l'initialisation  
f_centroids = open("/Users/zainabhabas/Documents/workspace/Comprendre-et-raisonner-pour-un-personnage-virtuel/image_schemas_a_utiliser_extraites.txt",'r',encoding='UTF8')
i = 0
centroids_coordinates = []
centroids_words = []
tmp2=[]

"""def trouverDistanceEtCentre(n,clustersParValeurs,kmeans):
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
    centreString=""
    for i in range(n):
        centreString=centreString+" "+words[positionCentre[i]]
    return centreString, distanceMoyenne

def distance(n, x, y):
    res=0
    for i in range(n):
         res=res+abs(float(x[i])-float(y[i]))
    return res

def trouverCluster(n,kmeans):
    clustersParValeurs=[]
    clustersParMots=[]
    for i in range (n):
        listeClusterIParMots=[]
        listeClusterIParValeurs=[]
        for j in range(len(kmeans.labels_)) :
            if kmeans.labels_[j]==i:
                listeClusterIParMots.append(words[j])
                listeClusterIParValeurs.append(coordinates[j])
        clustersParValeurs.append(listeClusterIParValeurs)
        clustersParMots.append(listeClusterIParMots)
    return clustersParValeurs,clustersParMots 
    
#renvoie une liste des i mots les plus proches du centre du cluster
def motsLesPlusProchesUnCluster(clusterParValeurs,clusterParMots,nombreDeProches,clusterCentre):
    ecart=[]
    for i in range(len(clusterParValeurs)):
        ecart.append(distance(300,clusterParValeurs[i],clusterCentre))
    x,indices=tri_ins(ecart)
    res=[]
    for i in range(nombreDeProches):
        if i<=len(indices)-1:
            res.append(clusterParMots[indices[i]])
    return res
    
#algorithme de tri
def tri_ins(t):
    tt=t[:]
    indices=[i for i in range(len(t))]
    for k in range(1,len(tt)):
        temp=tt[k]
        j=k
        while j>0 and temp<tt[j-1]:
            tt[j]=tt[j-1]
            indices[j]=indices[j-1]
            j-=1
        tt[j]=temp
        indices[j]=k
    return tt,indices
"""
for line in f_centroids:
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
    centroids_words.append(t[0])
    tmp2=t[1:len(t)]
    centroids_coordinates.append(tmp2)    
#print(centroids_words)    



clf = GMM(n_components = 44, init_params= "wc")
clf.means_= np.array(centroids_coordinates)
clf.fit(coordinates)
#clusters = 
tmp = 0

clusters = [[] for i in range (44)]
labels = clf.predict(coordinates)
for i in range(len(labels)) :
    tmp = labels[i]
    clusters[tmp].append(words[i])
    
#print(clusters)
for i in range(len(clusters)):
    listeDesMots="cluster numero "+str(i)+" : "
    for j in clusters[i]:
        listeDesMots=listeDesMots+j+" "
    print(listeDesMots)

"""for c in range(27):
    print(words[coordinates.index(clf.means_[c].tolist())])

#print(trouverDistanceEtCentre(27, trouverCluster(300,clf)[0], clf))"""




