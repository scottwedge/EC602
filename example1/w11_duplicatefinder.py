#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w11_duplicatefinder.py


from os import listdir
import re

import numpy as np

for photo in photolist:
    print(hashlib.md5(imread(photo)).hexdigest())

#print(imread(photolist[5]))
print(hashlib.md5(rgb2gray(imread(photolist[5]))).hexdigest())
#print(imread(photolist[7]))
print(hashlib.md5(rgb2gray(imread(photolist[7]))).hexdigest())

# hash photos
# compare hashes
# 3 rotations then flip and 3 rotations
np.rot90(matrix)
"""
from skimage import io, img_as_float
import matplotlib.pyplot as plt
import numpy as np
import glob
import hashlib

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.3 * r + 0.6 * g + 0.1 * b

    return gray

def crop(pngfile):
    image = img_as_float(io.imread(pngfile))
    white = np.array([1, 1, 1])
    mask = np.abs(image - white).sum(axis=2) < 0.05
    
    # Find the bounding box of those pixels
    coords = np.array(np.nonzero(~mask))
    top_left = np.min(coords, axis=1)
    bottom_right = np.max(coords, axis=1)
    
    out = image[top_left[0]:bottom_right[0]+1,
                top_left[1]:bottom_right[1]+1]
    outgray = rgb2gray(out)
    print(pngfile)    
    print(outgray)
    print(outgray.shape)
    #print(hashlib.md5(outgray).hexdigest())
    #plt.imshow(out)
    #plt.show()
    return(outgray)

def variations(cropped):
    var = []
    cropped1 = cropped
    for i in range(0,4):
        var.append(cropped1)
        cropped1 = np.rot90(cropped1)
    cropped2 = np.fliplr(cropped)
    for i in range(0,4):
        var.append(cropped2)
        cropped2 = np.rot90(cropped2)
    return var

photolist = glob.glob("*.png")
print(photolist)

croplist = []
for photo in photolist:
    croplist.append(crop(photo))
    #find a way to make photo the key to croplist[index]

var0 = variations(croplist[0])
#print(var0)
success = []
for i in croplist:
    i = i.copy(order='C')
    var = variations(i)
    for j in var:
        j = j.copy(order='C')
        if(hashlib.md5(j).hexdigest() == hashlib.md5(i).hexdigest()):
            success.append(i)
    print(hashlib.md5(i).hexdigest())
print(success)
"""
for i in range(0,len(var0)):
    plt.imshow(var0[i])
    plt.show()
    var0[i] = var0[i].copy(order='C')
    print(hashlib.md5(var0[i]).hexdigest())
    if(hashlib.md5(croplist[10]).hexdigest() == hashlib.md5(var0[i]).hexdigest()):
        print('YAY')
        
"""