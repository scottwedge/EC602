#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w8_multiply
11/7/16
Siggi&John
"""

import numpy as np
import sys
import os.path

m = "";
n = "";
l = "";

dtype = sys.argv[1]

if(len(sys.argv)==8):
    file1 = sys.argv[5];
    file2 = sys.argv[6];
    file3 = sys.argv[7];
    m = int(sys.argv[2]);
    n = int(sys.argv[3]);
    l = int(sys.argv[4]);
elif(len(sys.argv)==6):
    file1 = sys.argv[3];
    file2 = sys.argv[4];
    file3 = sys.argv[5];
    m = int(sys.argv[2]);
    n = m;
    l = m;
else:
    exit(1)

if (m != l):
    exit(3)

for arg in sys.argv:
    print(arg)


if(os.path.isfile(file1) == False):
    exit(2)
if(os.path.isfile(file2) == False):
    exit(2)

#f = open('xtest10.txt','r')
f = open(file1, 'r')
A=[]
for line in f.readlines():
    A.append(line.split())
f.close

#f = open('xtest11.txt','r')
f = open(file2, 'r')
B=[]
for line in f.readlines():
    B.append(line.split())
f.close

if (dtype == "int" or dtype == "integer"):
    A=np.array(A).astype(int)
    B=np.array(B).astype(int)
elif (dtype == "double" or dtype == "dbl"):
    A=np.array(A).astype(float)
    B=np.array(B).astype(float)
else:
    exit(1)

dimA = A.shape
dimB = B.shape

if(dimA[0] != m or dimA[1] != n or dimB[1] != l):
    exit(3)

C = np.dot(A,B)

#np.savetxt('xtest12.txt', C)
np.savetxt(file3, C)
print(C)

if(os.path.isfile(file3) == False):
    exit(4)
