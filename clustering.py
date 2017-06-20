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

%# get coordinates of all the points
nPoints = length(curve);
allCoord = [1:nPoints;curve]';              %'# SO formatting

%# pull out first point
firstPoint = allCoord(1,:);

%# get vector between first and last point - this is the line
lineVec = allCoord(end,:) - firstPoint;

%# normalize the line vector
lineVecN = lineVec / sqrt(sum(lineVec.^2));

%# find the distance from each point to the line:
%# vector between all points and first point
vecFromFirst = bsxfun(@minus, allCoord, firstPoint);

%# To calculate the distance to the line, we split vecFromFirst into two 
%# components, one that is parallel to the line and one that is perpendicular 
%# Then, we take the norm of the part that is perpendicular to the line and 
%# get the distance.
%# We find the vector parallel to the line by projecting vecFromFirst onto 
%# the line. The perpendicular vector is vecFromFirst - vecFromFirstParallel
%# We project vecFromFirst by taking the scalar product of the vector with 
%# the unit vector that points in the direction of the line (this gives us 
%# the length of the projection of vecFromFirst onto the line). If we 
%# multiply the scalar product by the unit vector, we have vecFromFirstParallel
scalarProduct = dot(vecFromFirst, repmat(lineVecN,nPoints,1), 2);
vecFromFirstParallel = scalarProduct * lineVecN;
vecToLine = vecFromFirst - vecFromFirstParallel;

%# distance to line is the norm of vecToLine
distToLine = sqrt(sum(vecToLine.^2,2));

%# plot the distance to the line
figure('Name','distance from curve to line'), plot(distToLine)

%# now all you need is to find the maximum
[maxDist,idxOfBestPoint] = max(distToLine);

%# plot
figure, plot(curve)
hold on
plot(allCoord(idxOfBestPoint,1), allCoord(idxOfBestPoint,2), 'or')