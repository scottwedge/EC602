#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w11_duplicatefinder.py


from os import listdir
import re
from skimage.io import imread
import numpy as np
import hashlib
import glob

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

photolist = glob.glob("*.png")
print(photolist)

for photo in photolist:
    print(hashlib.md5(imread(photo)).hexdigest())

#print(imread(photolist[5]))
print(hashlib.md5(rgb2gray(imread(photolist[5]))).hexdigest())
#print(imread(photolist[7]))
print(hashlib.md5(rgb2gray(imread(photolist[7]))).hexdigest())

# hash photos
# compare hashes
"""
from skimage import io, img_as_float
import matplotlib.pyplot as plt
import numpy as np

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

image = img_as_float(io.imread('kiwi8.png'))
# Select all pixels almost equal to white
# (almost, because there are some edge effects in jpegs
# so the boundaries may not be exactly white)
white = np.array([1, 1, 1])
mask = np.abs(image - white).sum(axis=2) < 0.05

# Find the bounding box of those pixels
coords = np.array(np.nonzero(~mask))
print(coords)
top_left = np.min(coords, axis=1)
print(top_left)
bottom_right = np.max(coords, axis=1)
print(bottom_right)

out = image[top_left[0]:bottom_right[0]+1,
            top_left[1]:bottom_right[1]+1]
print(out)
outgray = rgb2gray(out)
print(outgray)
print(out.shape)
plt.imshow(out)
plt.show()