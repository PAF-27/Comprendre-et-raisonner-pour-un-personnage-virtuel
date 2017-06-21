# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:34:06 2017

@author: zainabhabas
"""

import numpy as np 
from sklearn.cluster import KMeans
import matplotlib.pyplot as pl


>>>>>>> origin/clement

#permet de décoder le fichier texte contenant la projection des frames sur un espace en 300 dismension
f= open("C:\\Users\\cleme\git\\Comprendre-et-raisonner-pour-un-personnage-virtuel\\resultat.txt",'r',encoding='UTF8')
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
#//////////////////////////////////////////////////////////////////////////////


#fonction de calcul de distance
def distance(n, x, y):
    res=0
    for i in range(n):
         res=res+abs(float(x[i])-float(y[i]))
    return res

    
    
    
n=40
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

#///////////////////////////////////////////////////////////////////////////


#fonction de calcul de distance de minkowski avec un parametre p
def distanceMinkowski(n,x,y,p):
    res=0
    for i in range(n):
         res=res+(float(x[i])-float(y[i]))**p
    return res**(1/p)
#////////////////////////////////////////////////////////////////////////




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


#fonction de calcul de distance de tchebychev    
def distanceTchebychev(n,x,y):
    distanceParCoordonnees=[0 for i in range(n)]
    for i in range(n):
        distanceParCoordonnees[i]=abs(x[i]-y[i])
    return max(distanceParCoordonnees[i] for i in range(n))


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

    return clustersParValeurs,clustersParMots,centreString,distanceMoyenne,kmeans
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////


#permet de trouver les clusters avec un paramètre entier n selon la distance de Tchebychev
def KMEANSTchebychev(n):
    kmeans = KMeans(n_clusters=n, random_state=0).fit(coordinates)
    clustersParValeurs,clustersParMots=trouverCluster(n,kmeans)
    centreString,distanceMoyenne=trouverDistanceEtCentreTchebychev(n,clustersParValeurs,kmeans)

    return clustersParValeurs,clustersParMots,centreString,distanceMoyenne,kmeans
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



#Code permettant de trouver l'indice de l'élément dont la valeur est minimuale dans une liste

def trouverMin(liste):
    indicemin=0
    valeurmin=liste[indicemin]
    for i in range(len(liste)):
        if liste[i]<valeurmin:
            indicemin=i

    return i

n=561
p=2



def elbowPoint(points):
  secondDerivative = []
  for i in range(1, len(points) - 2):
    secondDerivative.append(points[i+1] + points[i-1] - 2*points[i])
    
  max_index = secondDerivative.index(max(secondDerivative))
  elbow_point = max_index + 1
  return elbow_point

#187
points   = comparaisonDistanceMoyenneTchebychev(n)
max_point = elbowPoint(points)

print(max_point)

pl.plot([max_point for i in range(1,11)] , [i for i in range(1, 11)] )
pl.plot([i for i in range(1, n+1)], points)
pl.show()

            valeurmin=liste[indicemin]
    return indicemin
#///////////////////////////////////////////////////////////////////////////////////

def trouverMax(liste):
    indicemax=0
    valeurmax=liste[indicemax]
    for i in range(len(liste)):
        if liste[i]>valeurmax:
            indicemax=i
            valeurmax=liste[indicemax]
    return indicemax

#variables possibles
n=561
p=10
#/////////////////////////////////////////////////////////////////////////////////

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
#///////////////////////////////////////////////////////////////////////////////

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
#/////////////////////////////////////////////////////////////////////////

#permet de trouver la liste des mots les plus proches pour chaque clusters
def motsLesPlusProchesKMEANS(clustersParValeurs,clustersParMots,kmeans):
    mots=[]
    for i in range(len(clustersParValeurs)):
        mots.append(motsLesPlusProchesUnCluster(clustersParValeurs[i],clustersParMots[i],10,kmeans.cluster_centers_[i]))
    return mots
#////////////////////////////////////////////////////////////////////////////////////////


#ce code permet d'avoir la liste des 10 mots les plus proches du centre pour chaque cluster
nombreDeClusters=36
clustersParValeurs,clustersParMots,centreString,distanceMoyenne,kmeans=KMEANS(nombreDeClusters)
motsLesPlusProches=motsLesPlusProchesKMEANS(clustersParValeurs,clustersParMots,kmeans)
for i in range(len(motsLesPlusProches)):
    dansUnCluster="cluster numero "+str(i)+" : "
    for j in motsLesPlusProches[i]:
        dansUnCluster=dansUnCluster+" | "+j
    dansUnCluster=dansUnCluster+" |\n"
    print(dansUnCluster)
#///////////////////////////////////////////////////////////////////////////////////////////


"""
#code permettant de tracer la distance moyenne choisie en fonction du nombre de clusters
listeDistanceMoyenne=comparaisonDistanceMoyenne(n)
pl.plot([i for i in range(1, n+1)], listeDistanceMoyenne)
pl.show()
valeurEn10=listeDistanceMoyenne[9]
coeff=valeurEn10/552
valeurTheorique=[coeff*(562-i) for i in range(561)]
ecart=[abs(valeurTheorique[i]-listeDistanceMoyenne[i]) for i in range(len(listeDistanceMoyenne))]
elbow=trouverMax(ecart)
print(ecart)
print(elbow)
#resultat : 316 clusters 
#////////////////////////////////////////////////////////////////////////////////////////////"""

