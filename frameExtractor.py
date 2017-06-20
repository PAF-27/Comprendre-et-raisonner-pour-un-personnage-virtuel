# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 17:25:09 2017

@author: zainabhabas
"""

fdata = open("/Users/zainabhabas/Documents/workspace/Comprendre-et-raisonner-pour-un-personnage-virtuel/numberbatch-en-17.04b.txt", "r",encoding='UTF8')
fframes = open("/Users/zainabhabas/Documents/workspace/Comprendre-et-raisonner-pour-un-personnage-virtuel/ListedesFrames.txt", "r",encoding='UTF8')
fresultat=open("/Users/zainabhabas/Documents/workspace/Comprendre-et-raisonner-pour-un-personnage-virtuel/resultat.txt",'w',encoding='UTF8')

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
    
    while (frame!="worry"):
        
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
    fframes=open("/Users/zainabhabas/Documents/workspace/Comprendre-et-raisonner-pour-un-personnage-virtuel/ListedesFrames.txt", "r",encoding='UTF8')
fresultat.close()
    