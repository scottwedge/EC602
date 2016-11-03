# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w5_testpoly.py
10/6/16
Siggi&John
"""
# -*- coding: utf-8 -*-

import unittest

authors=['jfkeis@bu.edu','sigurdur@bu.edu']



class PolynomialTestCase(unittest.TestCase):
    "empty class"

    def setUp(self):
        pass

    def test_add(self):
    	#try:
    		x = Polynomial([1,1,1])
    		y = Polynomial([2,2,2])
    		self.assertEqual(x+y, Polynomial([3,3,3]))
    	#except