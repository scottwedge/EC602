#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w11_duplicatefinder.py
"""
from skimage import io, img_as_float
import numpy as np
import glob
import hashlib
import re


def transform(item):
    return int(re.sub("[^0-9]", "", item))


def transform2(item):
    return int(re.sub("[^0-9]", "", item[0]))


def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.3 * r + 0.6 * g + 0.1 * b
    return gray


def crop(pngfile):
    image = img_as_float(io.imread(pngfile))
    white = np.array([1, 1, 1])
    mask = np.abs(image - white).sum(axis=2) < 0.05
    coords = np.array(np.nonzero(~mask))
    top_left = np.min(coords, axis=1)
    bottom_right = np.max(coords, axis=1)

    out = image[top_left[0]:bottom_right[0]+1,
                top_left[1]:bottom_right[1]+1]
    outgray = rgb2gray(out)
    return(outgray)


def variations(cropped):
    var = []
    cropped1 = cropped
    for i in range(0, 4):
        var.append(cropped1)
        cropped1 = np.rot90(cropped1)
    cropped2 = np.fliplr(cropped)
    for i in range(0, 4):
        var.append(cropped2)
        cropped2 = np.rot90(cropped2)
    return var


if __name__ == '__main__':

    photolist = glob.glob("*.png")

    croplist = {}
    for photo in photolist:
        croplist[photo] = crop(photo)

    success = []
    for i in croplist.keys():
        n = croplist[i]
        if i not in success:
            var = variations(n)
            for compkey in croplist.keys():
                compmat = croplist[compkey]
                for j in var:
                    j = j.copy(order='C')
                    if(hashlib.md5(j).hexdigest() ==
                       hashlib.md5(compmat).hexdigest()):
                            success.append(compkey)
        success.append(":::")

    outlisttop = []
    outlist = []
    j = ""
    for i in success:
        if(i != ":::"):
            outlist.append(i)
        else:
            if(j == ":::"):
                print("", end="")
            else:
                outlisttop.append(sorted(outlist, key=transform))
                outlist = []
        j = i

    f = open('answers.txt', 'w')
    finallist = sorted(outlisttop, key=transform2)
    for i in finallist:
        for j in i:
            if(j == i[-1]):
                f.write(j)
            else:
                f.write(j + " ")
        f.write("\n")
    f.close()

    f = open('answers.txt', 'r+')
    m = hashlib.sha256()
    m.update(f.read().encode('utf-8'))
    print(m.hexdigest())
    f.close()
