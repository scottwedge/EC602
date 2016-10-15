# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w6_dft.py
10/17/16
Siggi&John
"""

import unittest
import numpy as np

def DFTTestCase():
    def test_type(self):
        z = DFT((1, 4, 1+1j, 3-2j, 4-6j))
        self.assertIsInstance(z,ndarray,"Not a sequence of numbers")
        
    def test_shape(self):
        y = np.array([1, 4, 1+1j, 3-2j, 4-6j])
        z = DFT((1, 4, 1+1j, 3-2j, 4-6j))
        self.assertEqual(z.shape, y.shape)
    
    def test_fft(self):
        for i in range(10)
            x1 = (random.random()*2)-1
            i1 = j*(random.random()*2)-1
            x2 = (random.random()*2)-1
            i2 = j*(random.random()*2)-1
            x3 = (random.random()*2)-1
            i3 = j*(random.random()*2)-1
            x4 = (random.random()*2)-1
            i4 = j*(random.random()*2)-1
            x = (x1+i1, x2+i2, x3+i3, x4+i4)
            DFTfft = DFT(x)
            z = np.asarray(x, dtype=complex)
            numpfft = np.fft.fft(z)
            self.assertAlmostEqual(numpfft,DFTfft)