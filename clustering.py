# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:34:06 2017

@author: zainabhabas
"""

import numpy as np 
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt

    
    
#permet de décoder le fichier texte contenant la projection des frames sur un espace en 300 dismension
f= open("/home/erwan/Documents/PAF/Clustering/frame-raisonnable.txt",'r',encoding='UTF8')
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
#//////////////////////////////////////////////////////////////////////////////



#fonction de calcul de distance
def distance(n, x, y):
    res=0
    for i in range(n):
         res=res+abs(float(x[i])-float(y[i]))
    return res
#///////////////////////////////////////////////////////////////////////////


#fonction de calcul de distance de minkowski
def distanceMinkowski(n,x,y,p):
    res=0
    for i in range(n):
         res=res+(float(x[i])-float(y[i]))**p
    return res**(1/p)
#////////////////////////////////////////////////////////////////////////

def distanceTchebychev(n,x,y):
    distanceParCoordonnees=[0 for i in range(n)]
    for i in range(n):
        distanceParCoordonnees[i]=abs(x[i]-y[i])
    return max(distanceParCoordonnees[i] for i in range(n))


#permet de retourner la liste des clusters par mots ou par valeurs
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
#///////////////////////////////////////////////////////////////



#permet de calculer le centre et la distance moyenne pour chaque cluster
def trouverDistanceEtCentre(n,clustersParValeurs,kmeans):
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
#//////////////////////////////////////////////////////////////


#permet de calculer le centre et la distance moyenne pour chaque cluster à partir de la distance de minkowski avec p un paramètre
def trouverDistanceEtCentreMinkowski(n,clustersParValeurs,kmeans,p):
    minimum=[]
    positionCentre=[0 for i in range(n)]
    distanceMoyenne=[0 for i in range(n)]
    for i in range(n):
        minimum.append(distanceMinkowski(300, clustersParValeurs[i][0], kmeans.cluster_centers_[i],p))
        for j in range(len(clustersParValeurs[i])):
            distanceTmp=distanceMinkowski(300,clustersParValeurs[i][j],kmeans.cluster_centers_[i],p)
            if distanceTmp<minimum[i]:
                positionCentre[i]=j
            distanceMoyenne[i]=distanceMoyenne[i]+distanceTmp
        distanceMoyenne[i]=distanceMoyenne[i]/len(clustersParValeurs[i])
    centreString=""
    for i in range(n):
        centreString=centreString+" "+words[positionCentre[i]]
    return centreString, distanceMoyenne
#//////////////////////////////////////////////////////////////

#permet de calculer le centre et la distance moyenne pour chaque cluster à partir de la distance de Tchebychev
def trouverDistanceEtCentreTchebychev(n,clustersParValeurs,kmeans):
    minimum=[]
    positionCentre=[0 for i in range(n)]
    distanceMoyenne=[0 for i in range(n)]
    for i in range(n):
        minimum.append(distanceTchebychev(300, clustersParValeurs[i][0], kmeans.cluster_centers_[i]))
        for j in range(len(clustersParValeurs[i])):
            distanceTmp=distanceTchebychev(300,clustersParValeurs[i][j],kmeans.cluster_centers_[i])
            if distanceTmp<minimum[i]:
                positionCentre[i]=j
            distanceMoyenne[i]=distanceMoyenne[i]+distanceTmp
        distanceMoyenne[i]=distanceMoyenne[i]/len(clustersParValeurs[i])
    centreString=""
    for i in range(n):
        centreString=centreString+" "+words[positionCentre[i]]
    return centreString, distanceMoyenne
#//////////////////////////////////////////////////////////////

#permet de trouver les clusters avec un paramètre entier n 
def KMEANS(n):
    kmeans = KMeans(n_clusters=n, random_state=0).fit(coordinates)
    clustersParValeurs,clustersParMots=trouverCluster(n,kmeans)
    centreString,distanceMoyenne=trouverDistanceEtCentre(n,clustersParValeurs,kmeans)
    return clustersParValeurs,clustersParMots,centreString,distanceMoyenne,kmeans
#///////////////////////////////////////////////////////////////


#permet de trouver les clusters avec un paramètre entier n ainsi qu'un paramètre p selon la distance de Minkowski
def KMEANSMinkowski(n,p):
    kmeans = KMeans(n_clusters=n, random_state=0).fit(coordinates)
    clustersParValeurs,clustersParMots=trouverCluster(n,kmeans)
    centreString,distanceMoyenne=trouverDistanceEtCentreMinkowski(n,clustersParValeurs,kmeans,p)
    return clustersParValeurs,clustersParMots,centreString,distanceMoyenne
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////

#permet de trouver les clusters avec un paramètre entier n selon la distance de Tchebychev
def KMEANSTchebychev(n):
    kmeans = KMeans(n_clusters=n, random_state=0).fit(coordinates)
    clustersParValeurs,clustersParMots=trouverCluster(n,kmeans)
    centreString,distanceMoyenne=trouverDistanceEtCentreTchebychev(n,clustersParValeurs,kmeans)
    return clustersParValeurs,clustersParMots,centreString,distanceMoyenne
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////

#permet de comparer les distances moyennes entre les différentes clusterisations
def comparaisonDistanceMoyenne(jusqua):
    listeDistanceMoyenne=[]
    for i in range(1,jusqua+1):
        valeurMoyenne=0
        listeDesDistanceDeI=KMEANS(i)[3]
        for j in range(i):
            valeurMoyenne=listeDesDistanceDeI[j]+valeurMoyenne
        valeurMoyenne=valeurMoyenne/i
        listeDistanceMoyenne.append(valeurMoyenne)
    return listeDistanceMoyenne
#//////////////////////////////////////////////////////////////////////////////

#permet de comparer les distances moyennes entre les différentes clusterisations selon la distance de Minkowski avec un parametre p
def comparaisonDistanceMoyenneMinkowski(jusqua,p):
    listeDistanceMoyenne=[]
    for i in range(1,jusqua+1):
        valeurMoyenne=0
        listeDesDistanceDeI=KMEANSMinkowski(i,p)[3]
        for j in range(i):
            valeurMoyenne=listeDesDistanceDeI[j]+valeurMoyenne
        valeurMoyenne=valeurMoyenne/i
        listeDistanceMoyenne.append(valeurMoyenne)
    return listeDistanceMoyenne
#//////////////////////////////////////////////////////////////////////////////

#permet de comparer les distances moyennes entre les différentes clusterisations selon la distance de Minkowski avec un parametre p
def comparaisonDistanceMoyenneTchebychev(jusqua):
    listeDistanceMoyenne=[]
    for i in range(1,jusqua+1):
        valeurMoyenne=0
        listeDesDistanceDeI=KMEANSTchebychev(i)[3]
        for j in range(i):
            valeurMoyenne=listeDesDistanceDeI[j]+valeurMoyenne
        valeurMoyenne=valeurMoyenne/i
        listeDistanceMoyenne.append(valeurMoyenne)
    return listeDistanceMoyenne
#//////////////////////////////////////////////////////////////////////////////


def trouverMin(liste):
    indicemin=0
    valeurmin=liste[indicemin]
    for i in range(len(liste)):
        if liste[i]<valeurmin:
            indicemin=i
    return i

#n=561
#p=2
#plt.plot([i for i in range(1, n+1)], comparaisonDistanceMoyenneTchebychev(n))
#plt.show(

#clustersParValeurs,clustersParMots,centreString,distanceMoyenne,kmeans = KMEANS(9)
#print (kmeans.labels_)
#inertia = []
#for i in range (1,20) :        
#    clustersParValeurs,clustersParMots,centreString,distanceMoyenne,kmeans = KMEANS(i)
#    inertia.append(kmeans.inertia_)
#plt.plot([i for i in range(1,20)], inertia)
#plt.show()

clustersParValeurs,clustersParMots,centreString,distanceMoyenne,kmeans=KMEANS(40)
for i in range(len(clustersParMots)):
    listeDesMots="cluster numero "+str(i)+" : "
    for j in clustersParMots[i]:
        listeDesMots=listeDesMots+j+" "
    print(listeDesMots)