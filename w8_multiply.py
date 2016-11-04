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
#import matplotlib.pyplot as pyplot
#import math


"""
if len(sys.argv==8):
    file1 = sys.argv[5];
    file2.open(argv[6]);
    file3.open(argv[7]);
    m = int(argv[2]);
    n = int(argv[3]);
    l = int(argv[4]);
 
elif argc==6:
    file1.open(argv[3]);
    file2.open(argv[4]);
    file3.open(argv[5]);
    m = int(argv[2]);
else:
    exit(1)
"""

for arg in sys.argv:
    print(arg)

dtype = sys.argv[1]
file1 = sys.argv[5]
file2 = sys.argv[6]
file3 = sys.argv[7]

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

a=np.array(A).astype('int')
b=np.array(B).astype('int')

C = np.dot(a,b)

#np.savetxt('xtest12.txt', C)
np.savetxt(file3, C)
print(C)
