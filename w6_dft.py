# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w6_dft.py
10/17/16
Siggi&John
"""
#import numpy as np
from numpy import zeros,exp,array,pi

#array(object, dtype=complex)

def DFT(x):
        
    try:
        y = array(x, dtype=complex)
        N = y.shape[0]
        n = range(N)
        n = array(n)
        k = n.reshape((N, 1))
        M = exp(-2j * pi * k * n / N)
        FT = M@y
    except:
        raise ValueError
  
    #print(FT) 
    return FT

def main():
    #DFT((1, 4, 1+1j, 3-2j, 4-6j))
    #DFT((1,2,3,'a'))

if __name__ == '__main__':
    main()

### Recreate input signal from DFT results and compare to input signal
##fnList2 = InverseDFT(FmList)
##for n in range(N):
##    print fnList[n], fnList2[n].real

#DFTTestCase()
#numpy.fft.fft