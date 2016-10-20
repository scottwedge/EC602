# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w6_dft_test.py
10/17/16
Siggi&John
"""

#import DFT
import unittest
import numpy as np


authors = ['jfkeis@bu.edu','sigurdur@bu.edu']

class DFTTestCase(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_type(self):
        z = DFT((1, 4, 1+1j, 3-2j, 4-6j))
        self.assertIsInstance(z,np.ndarray)
        
    def test_shape(self):
        y = np.array([1, 4, 1+1j, 3-2j, 4-6j])
        z = DFT((1, 4, 1+1j, 3-2j, 4-6j))
        self.assertEqual(z.shape, y.shape)

    def test_fft(self):
        for N in range(2,21):
            x = [0]*N
            for i in range(0, 10):
                for j in range(0,N):
                    x1 = (2*np.random.random())-1
                    i1 = (2*np.random.random())-1
                    x[j] = complex(x1,i1)
                    DFTfft = DFT(x)
                    z = np.asarray(x, dtype=complex)
                    numpfft = np.fft.fft(z)
                    for k in range(0,N):
                        self.assertAlmostEqual(numpfft[k],DFTfft[k])

    def test_input(self):
        self.assertRaises(ValueError,DFT,'soccer')
    
    def test_explicit(self):
        try:
            DFT(bytearray([1,4]))
        except:
            self.fail('foo')
