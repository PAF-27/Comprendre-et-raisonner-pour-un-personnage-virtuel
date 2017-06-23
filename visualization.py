#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:28:41 2017

@author: XIAJin
"""
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import random

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

# lire 
f= open("./resultat.txt",'r',encoding='UTF8')
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
words_size = len(words)

# visualization
tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000)
low_dim_embs = tsne.fit_transform(coordinates[:])
plot_with_labels(low_dim_embs, words,words)

 for cluster in clustersParMots:
    f.write(clustersParMots.index(cluster))
    f.write(" ")
    for word in cluster:
    f.write(" ") 
    f.write("\n")