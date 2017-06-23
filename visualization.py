#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:28:41 2017

@author: XIAJin
"""
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

def plot_with_labels(low_dim_embs, labels, filename='tsne.png'):
  assert low_dim_embs.shape[0] >= len(labels), 'More labels than embeddings'
  plt.figure(figsize=(18, 18))  # in inches
  for i, label in enumerate(labels):
    x, y = low_dim_embs[i, :]
    plt.scatter(x, y)
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
plot_with_labels(low_dim_embs, words)