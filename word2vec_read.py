#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 15:58:41 2017

@author: XIAJin
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import math
import os
import random
import zipfile

import numpy as np
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf

# Read the data into a list of strings.
def read_data(filename):
  """Extract the first file enclosed in a zip file as a list of words."""
  with zipfile.ZipFile(filename) as f:
    data = tf.compat.as_str(f.read(f.namelist()[0])).split()
  return data

def build_dataset(words, n_words):
  """Process raw inputs into a dataset."""
  count = [['UNK', -1]]
  count.extend(collections.Counter(words).most_common(n_words - 1))
  dictionary = dict()
  for word, _ in count:
    dictionary[word] = len(dictionary)
  data = list()
  unk_count = 0
  for word in words:
    if word in dictionary:
      index = dictionary[word]
    else:
      index = 0  # dictionary['UNK']
      unk_count += 1
    data.append(index)
  count[0][1] = unk_count
  reversed_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
  return data, count, dictionary, reversed_dictionary


filename = './text8.zip'
vocabulary = read_data(filename)
print('Data size', len(vocabulary))

vocabulary_size = 50000
data, count, dictionary, reverse_dictionary = build_dataset(vocabulary,
                                                            vocabulary_size)
frame_file = open("frames.txt", "r")
lines = frame_file.readlines()
frames = []
for line in lines:
    line = line.lower()
    tmp = line.split()
    frame = tmp[0]
    frames.append(frame)
    
words = dictionary.keys()
def find_frames(words, frames):
    frames_in_words = []
    for word in words:
        for frame in frames:
            if frame == word:
                frames_in_words.append(word)
                break
    return frames_in_words
frames_in_words = find_frames(words,frames)    

