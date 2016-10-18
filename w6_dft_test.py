# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w6_dft.py
10/17/16
Siggi&John
"""

import DFT
import unittest
import numpy as np
import random
import sys

class DFTTestCase(unittest.TestCase):
    def test_type(self):
        z = DFT((1, 4, 1+1j, 3-2j, 4-6j))
        self.assertIsInstance(z,np.array,"Not a sequence of numbers")
        
    def test_shape(self):
        y = np.array([1, 4, 1+1j, 3-2j, 4-6j])
        z = DFT((1, 4, 1+1j, 3-2j, 4-6j))
        self.assertEqual(z.shape, y.shape)
    
    def test_fft(self):
        for i in range(0, 10):
            x1 = (random.random()*2)-1
            i1 = (random.random()*2)-1
            i1 = complex(0,i1)
            x2 = (random.random()*2)-1
            i2 = (random.random()*2)-1
            i2 = complex(0,i2)
            x3 = (random.random()*2)-1
            i3 = (random.random()*2)-1
            i3 = complex(0,i3)
            x4 = (random.random()*2)-1
            i4 = (random.random()*2)-1
            i4 = complex(0,i4)
            x = (x1+i1, x2+i2, x3+i3, x4+i4)
            DFTfft = DFT(x)
            z = np.asarray(x, dtype=complex)
            numpfft = np.fft.fft(z)
            self.assertAlmostEqual(numpfft,DFTfft)