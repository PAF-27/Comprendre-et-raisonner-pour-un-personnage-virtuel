# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:34:06 2017

@author: zainabhabas
"""

import numpy as np 
from sklearn.cluster import KMeans
import matplotlib.pyplot as pl


#permet de décoder le fichier texte contenant la projection des frames sur un espace en 300 dimensions
f= open("result_word2vec.txt",'r',encoding='UTF8')
words=[]
tmp=[]
coordinates=[]
for line in f:
    t=line.split()
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
f.close()
#//////////////////////////////////////////////////////////////////////////////


#permet de décoder le fichier texte contenant la projection des image schemas sur un espace en 300 dimensions
#permet de décoder le fichier texte contenant la projection des image schemas sur un espace en 300 dimensions
f2= open("image_schema_word2vec.txt",'r',encoding='UTF8')
words2=[]
tmp=[]
coordinates2=[]
for line in f2:
    t=line.split()
    for j in range (1, len(t)) :
        string=t[j]
        if string.startswith('-'):
            string=string.replace('-','')
            float(string)
            t[j]=-float(string)
        else :
            t[j]=float(string)
    words2.append(t[0])
    tmp=t[1:len(t)]
    coordinates2.append(tmp)
f2.close()
#////////////////////////////////////////////////////////////////////////////////////


#fonction de calcul de distance
def distance(n, x, y):
    res=0
    for i in range(n):
         res=res+abs(float(x[i])-float(y[i]))
    return res
#///////////////////////////////////////////////////////////////////////////


#fonction de calcul de distance de minkowski avec un parametre p
def distanceMinkowski(n,x,y,p):
    res=0
    for i in range(n):
         res=res+(float(x[i])-float(y[i]))**p
    return res**(1/p)
#////////////////////////////////////////////////////////////////////////


#fonction de calcul de distance de tchebychev
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
        print(i)
        print(len(kmeans.cluster_centers_))
        print(len(clustersParValeurs[i]))
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

#permet de calculer le centre et l'inertie de chaque cluster
def trouverInertie(n,clustersParValeurs,kmeans):
    distanceCarreCentresTmp=[0 for i in range(len(clustersParValeurs))]
    inertie=[0 for i in range(len(clustersParValeurs))]
    for i in range(len(clustersParValeurs)):
        for point in clustersParValeurs[i]:
            for centre in kmeans.cluster_centers_:
                distanceCarreCentresTmp[i]=(distance(n,point,centre))**2
            inertie[i]=inertie[i]+min(distanceCarreCentresTmp)
    inertieTotale=sum(inertie)
    inertieMoyenne=inertieTotale/len(clustersParValeurs)
    return inertieTotale,inertieMoyenne,inertie
#//////////////////////////////////////////////////////////////


#permet de trouver les clusters avec un paramètre entier n 
def KMEANS(n):
    kmeans = KMeans(n_clusters=n, random_state=0).fit(coordinates)
    clustersParValeurs,clustersParMots=trouverCluster(n,kmeans)
    centreString,distanceMoyenne=trouverDistanceEtCentre(n,clustersParValeurs,kmeans)
    return clustersParValeurs,clustersParMots,centreString,distanceMoyenne,kmeans
#///////////////////////////////////////////////////////////////


#permet de trouver les clusters avec un paramètre entier n  et une liste de n centres pour l'initialisation
def KMEANSInit(n, coordinatesCenters, coordinates):
    kmeans = KMeans(n_clusters=n, init=coordinatesCenters,n_init=1).fit(coordinates)
    clustersParValeurs,clustersParMots=trouverCluster(n,kmeans)
    #centreString,distanceMoyenne=trouverDistanceEtCentre(n,clustersParValeurs,kmeans)
    #return clustersParValeurs,clustersParMots,centreString,distanceMoyenne,kmeans
    return clustersParValeurs,clustersParMots,kmeans
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

#ce code permet d'avoir la liste des 10 mots les plus proches du centre pour chaque cluster en initialisant les clusters aux image schemas
nombreDeClusters=45

"""
coordonneesCentres=np.asarray(coordinates2)
clustersParValeurs,clustersParMots,centreString,distanceMoyenne,kmeans=KMEANSInit(nombreDeClusters, coordonneesCentres, coordinates)
motsLesPlusProches=motsLesPlusProchesKMEANS(clustersParValeurs,clustersParMots,kmeans)
for i in range(len(motsLesPlusProches)):
    dansUnCluster="cluster numero "+str(i)+" : "
    for j in motsLesPlusProches[i]:
        dansUnCluster=dansUnCluster+" | "+j
    dansUnCluster=dansUnCluster+" |\n"
    print(dansUnCluster)
print()
"""

#permet de lister tous les elements dans un cluster
def lister(words,labels,i):
    res=[]
    for j in range(len(labels)):
        if labels[j]==i:
            res.append(words[j])
    return res

#/////////////////////////////////////////////////////////////////////////////////////////////////////

#code pour lister tous les elements des clusters
clustersParValeurs,clustersParMots,centreString,distanceMoyenne,kmeans=KMEANS(nombreDeClusters)
print(kmeans.labels_)
for i in range(len(clustersParMots)):
    listeDesMots="cluster numero "+str(i)+" : "
    for j in clustersParMots[i]:
        listeDesMots=listeDesMots+j+" "
    print(listeDesMots+"\n")
"""
#code pour forcer les centres et lister tous les elements des clusters
coordonneesCentres=np.asarray(coordinates2)
clustersParValeurs,clustersParMots,centreString,distanceMoyenne,kmeans=KMEANSInit(nombreDeClusters, coordonneesCentres, coordinates)
print(kmeans.labels_)
for i in range(len(clustersParMots)):
    listeDesMots="cluster numero "+str(i)+" : "
    for j in clustersParMots[i]:
        listeDesMots=listeDesMots+j+" "
    print(listeDesMots+"\n")
#///////////////////////////////////////////////////////////////////////////////:
""" 


"""
#code permettant de calculer l'inertie totale et moyenne en fonction d'un nombre de clusters
clustersParValeurs, kmeans=KMEANS(9)[0],KMEANS(9)[4]
inertieTotale,inertieMoyenne,inertie=trouverInertie(300,clustersParValeurs,kmeans)
print(inertieTotale)
print(inertieMoyenne)
#print(inertie)
#inertie de 5854.46 pour 9 clusters
"""

"""
#code permettant de tracer l'inertie totale en fonction du nombre de clusters
n=20
listeInertieTotale=[]
listeInertieMoyenne=[]
for i in range(1,n):
    clustersParValeurs, kmeans=KMEANS(i)[0],KMEANS(i)[4]
    inertieTotale,inertieMoyenne,inertie=trouverInertie(300,clustersParValeurs,kmeans)
    listeInertieTotale.append(inertieTotale)
    listeInertieMoyenne.append(inertieMoyenne)
print(listeInertieTotale)
pl.plot([i for i in range(1, n)], listeInertieTotale)
pl.show()
#/////////////////////////////////////////////////////////////////////////////////////
#point interessant à 9 clusters
"""


"""
#ce code permet d'avoir la liste des 10 mots les plus proches du centre pour chaque cluster
nombreDeClusters=9
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

"""
#code permettant de tracer la distance moyenne choisie en fonction du nombre de clusters
n=561
p=10
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