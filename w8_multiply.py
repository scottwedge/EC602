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
    if(float(sys.argv[2]) <= 0 or float(sys.argv[3]) <= 0 or float(sys.argv[4]) <= 0):
        exit(1)
    if (sys.argv[2] == "UNREADABLE" or sys.argv[3] == "UNREADABLE" or sys.argv[4] == "UNREADABLE"):
        exit(2)
elif(len(sys.argv)==6):
    file1 = sys.argv[3];
    file2 = sys.argv[4];
    file3 = sys.argv[5];
    m = int(sys.argv[2]);
    n = m;
    l = m;
    if(float(sys.argv[2]) <= 0):
        exit(1)
    if(sys.argv[2] == "UNREADABLE"):
        exit(2)
else:
    exit(1)

#for arg in sys.argv:
#   print(arg)

if(os.path.isfile(file1) == False):
    exit(2)
if(os.path.isfile(file2) == False):
    exit(2)

#f = open('xtest10.txt','r')
#f = open(file1, 'r')
#A=[]
#for line in f.readlines():
#    A.append(line.split())
#f.close

#f = open('xtest11.txt','r')
#f = open(file2, 'r')
#B=[]
#for line in f.readlines():
#    B.append(line.split())
#f.close

A = np.loadtxt(file1)
B = np.loadtxt(file2)

dimA = A.shape
dimB = B.shape

if(dimA[0] != m or dimA[1] != n or dimB[1] != l):
    exit(3)

C = np.dot(A,B)

if (dtype == "int"):
    C=np.array(C).astype(int)
    np.savetxt(file3, C, fmt='%i')
elif (dtype == "double"):
    C=np.array(C).astype(float)
    np.savetxt(file3, C, fmt='%10.5f')
else:
    exit(1)

#np.savetxt('xtest12.txt', C)
#np.savetxt(file3, C)
print(C)

if(os.path.isfile(file3) == False):
    exit(4)
