# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:34:06 2017

@author: zainabhabas
"""

import numpy as np 
from sklearn.cluster import KMeans
import random
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.mixture import GMM


#permet de décoder le fichier texte contenant la projection des frames sur un espace en 300 dimensions
f= open("frames_word2vec.txt",'r',encoding='UTF8')
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
    kmeans = KMeans(n_clusters=n, random_state=0,max_iter=1000,n_init=100).fit(coordinates)
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
nombreDeClusters= 46

# visualisation
def plot_with_labels(low_dim_embs, words,labels, filename='tsne.png'):
    label_set = set(labels)
    color_map = {}
    r = lambda: random.randint(0,255)
    for label in label_set:
        random_color = format('#%02X%02X%02X' % (r(),r(),r()))
        color_map[label] = random_color
    
    assert low_dim_embs.shape[0] >= len(words), 'More words than embeddings'
    plt.figure(figsize=(18, 18))  # in inches
    for i, label in enumerate(words):
        x, y = low_dim_embs[i, :]
        plt.scatter(x, y,color = color_map[labels[i]])
        plt.annotate(label,
        xy=(x, y),
        xytext=(5, 2),
        textcoords='offset points',
        ha='right',
        va='bottom')

    plt.savefig(filename)

# reverdiction
def getframe2label(clustersParMots):
    frame2label = {}
    for cluster in clustersParMots:
        for frame in cluster:
            frame2label[frame] = clustersParMots.index(cluster)
    return frame2label


#permet de lister tous les elements dans un cluster
def lister(words,labels,i):
    res=[]
    for j in range(len(labels)):
        if labels[j]==i:
            res.append(words[j])
    return res

words = words + words2
coordinates = coordinates + coordinates2

# delete the word
blacklist = ["departing","dressing","authority","frequency","emergency","request","placing","chatting","surpassing","sequence","indicating","purpose","emitting","employing","memorization","lending","exporting","system","attack","animals"]
blacklist.append("eclipse")
blacklist.append("front")
blacklist.append("desiring")
blacklist.append("offering")
blacklist.append("patrolling")
blacklist.append("difficulty")
blacklist.append("extradition")
blacklist.append("halt")
blacklist.append("receiving")
blacklist.append("substance")
blacklist.append("origin")
blacklist.append("summarizing")
blacklist.append("artificiality")
blacklist.append("getting")
blacklist.append("inspecting")
blacklist.append("desirability")
blacklist.append("subversion")

print(len(blacklist))
for black_word in blacklist:
    index = words.index(black_word)
    del words[index]
    del coordinates[index]
    
#code pour lister tous les elements des clusters
clustersParValeurs,clustersParMots,centreString,distanceMoyenne,kmeans = KMEANS(nombreDeClusters)
print(kmeans.labels_)
for i in range(len(clustersParMots)):
    listeDesMots="cluster numero "+str(i)+" : "
    for j in clustersParMots[i]:
        listeDesMots=listeDesMots+j+" "
    print(listeDesMots+"\n")
    
# visualisation    
tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000)
low_dim_embs = tsne.fit_transform(coordinates[:])
frame2label = getframe2label(clustersParMots)
labels = []
for word in words:
    labels.append(frame2label[word])
plot_with_labels(low_dim_embs, words,labels)

print("Using GMM")
kmeans = KMeans(n_clusters = 44,random_state =0).fit(coordinates)
centroids = kmeans.cluster_centers_

clf = GMM(n_components = 44, init_params= "wc")
clf.means_= np.array(centroids)
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