#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:06:31 2017

@author: XIAJin
"""

import gensim

#
word2vecs = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

frame_file = open("frames.txt", "r")
lines = frame_file.readlines()
frames = []
for line in lines:
    line = line.lower()
    tmp = line.split()
    frame = tmp[0]
    frames.append(frame)
frame_file.close()

words = []
vectors = []
for frame in frames:
    if frame in word2vecs:
        words.append(frame)
        vectors.append(word2vecs[frame])
    
result_word2vec = open("result_word2vec.txt","w")
        
for i in range(len(words)):
   result_word2vec.write(words[i])
   for number in vectors[i]:
       result_word2vec.write(' ')
       result_word2vec.write(str(number))
   result_word2vec.write('\n')

result_word2vec.close()

"""
# extrare image schema
image_file = open("image_schemas_a_utiliser","r")
images = []
for line in image_file.readlines():
    line = line.lower()
    tmp = line.split()
    image = tmp[0]
    images.append(image)
schemas = []
schemas_vectors = []
for image in images:
    if image in word2vecs:
        schemas.append(image)
        schemas_vectors.append(word2vecs[image])
image_file.close()
        
# write to file
result_word2vec = open("image_schema_word2vec.txt","w")
for i in range(len(schemas)):
   result_word2vec.write(schemas[i])
   for number in schemas_vectors[i]:
       result_word2vec.write(' ')
       result_word2vec.write(str(number))
   result_word2vec.write('\n')

result_word2vec.close()
"""