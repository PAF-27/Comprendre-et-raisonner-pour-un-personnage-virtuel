# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:45:49 2017

@author: cleme
"""
import numpy as np 
from sklearn.cluster import KMeans
fresultat=open('C:\\Users\\cleme\\Desktop\\image_schemas_a_utiliser_extraites.txt','w',encoding='UTF8')
fframes= open('C:\\Users\\cleme\\Desktop\\image_schemas_a_utiliser.txt','r',encoding='UTF8')
fdata=open('C:\\Users\\cleme\\numberbatch-en-17.04b.txt','r',encoding='UTF8')
compteurFrames=0
compteurMots=0
fdata.readline()
words=[]
tartiflette=[]
for line in fdata:
    t=line.split()
    compteurMots=compteurMots+1
    mot=t[0]
    frame=fframes.readline()
    frame=str(frame)
    frame=frame.lower()
    tartiflette=frame.split()
    frame=tartiflette[0]
    while (frame!="process"):
        if frame==mot:
            print(mot+" "+frame)
            compteurFrames=compteurFrames+1
            print(compteurFrames)
            fresultat.write(frame+" ")
            for j in range (1, len(t)) :
                string=t[j]
                fresultat.write(string+" ")
            fresultat.write("\n")
            frame=fframes.readline()
            frame=str(frame)
            frame=frame.lower()
            tartiflette=frame.split()
            frame=tartiflette[0]
        else :
            frame=fframes.readline()
            frame=str(frame)
            frame=frame.lower()
            tartiflette=frame.split()
            frame=tartiflette[0]
        #print(mot+" "+frame)
    
    fframes.close()
    fframes=open('C:\\Users\\cleme\\Desktop\\image_schemas_a_utiliser.txt','r',encoding='UTF8')
fresultat.close()