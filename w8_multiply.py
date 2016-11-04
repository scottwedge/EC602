# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w8_multiply
11/7/16
Siggi&John
"""

import numpy as np
#import matplotlib.pyplot as pyplot
#import math

f = open('xtest10.txt','r')
A=[]
for line in f.readlines():
    A.append(line.split())
f.close

f = open('xtest11.txt','r')
B=[]
for line in f.readlines():
    B.append(line.split())
f.close

a=np.array(A).astype('int')
b=np.array(B).astype('int')

C = np.dot(a,b)
print(C)
