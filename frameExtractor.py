# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 17:25:09 2017

@author: zainabhabas
"""

fdata = open("C:\\Users\\cleme\Desktop\\numberbatch-en-17.04b.txt", "r",encoding='UTF8')
fframes = open("C:\\Users\\cleme\Desktop\\liste_des_frames.txt", "r",encoding='UTF8')
fresultat=open("C:\\Users\\cleme\Desktop\\test.txt",'w',encoding='UTF8')
compteurFrames=0
fdata.readline()
words=[]
tartiflette=[]
listeDesFrames=[]
indicesDesFrames=[0 for i in range(1223)]
listeDesFramesOubliees=[]
for line in fdata:
    t=line.split()
    mot=t[0]
    frame=fframes.readline()
    frame=str(frame)
    listeDesFrames.append(frame)
    frame=frame.lower()
    tartiflette=frame.split()
    frame=tartiflette[0]
    compteurFrames=0
    while (frame!="worry"):
        compteurFrames=compteurFrames+1
        if frame==mot:
            indicesDesFrames[compteurFrames]=1
            print(mot+" "+frame)
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
    fframes=open("C:\\Users\\cleme\Desktop\\liste_des_frames.txt", "r",encoding='UTF8')
print(indicesDesFrames)
print(listeDesFrames)
for i in range(len(indicesDesFrames)):
    if indicesDesFrames[i]==0:
        listeDesFramesOubliees.append(listeDesFrames[i])
print(listeDesFramesOubliees)
fresultat.close()
fframes.close()
fdata.close()