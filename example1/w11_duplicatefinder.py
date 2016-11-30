#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w11_duplicatefinder.py
"""

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

print(imread(photolist[5]))
print(rgb2gray(imread(photolist[5])))
print(imread(photolist[7]))
print(rgb2gray(imread(photolist[7])))
# hash photos
# compare hashes