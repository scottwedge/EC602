# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu
<<<<<<< HEAD
=======

>>>>>>> 318940eb26d0d40c9eeea05e1574534f9d78e415
w5_testpoly.py
10/2/16
Siggi&John
"""

import unittest
import sys

authors = ['jfkeis@bu.edu','sigurdur@bu.edu']

class PolynomialTestCase(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_init(self):
        z = Polynomial()
        self.assertIsInstance(z,Polynomial,"Not a polynomial")
    
    def test_deriv(self):
        p10 = Polynomial([1,2,3,1,5])
        self.assertEqual(p10.deriv(),Polynomial([4,6,6,1]))
      
    def test_add(self):
        p1 = Polynomial([1,2,3,0,5])
        p2 = Polynomial([1,2,2])
        self.assertEqual(p1+p2, Polynomial([1,2,4,2,7]))

    def test_radd(self):
        p1 = Polynomial([1,2,3,0,5])
        p2 = Polynomial([1,2,2])
        self.assertEqual(p2+p1, Polynomial([1,2,4,2,7]))

    def test_sub(self):
        p1 = Polynomial([1,2,3,0,5])
        p2 = Polynomial([1,2,2])
        self.assertEqual(p1-p2, Polynomial([1,2,2,-2,3]))

    def test_assign(self):
        p7 = Polynomial([])
        p7[2] = 3
        p7[1] = 2
        self.assertEqual(p7, Polynomial([3,2,0]))

    def test_rsub(self):
        p1 = Polynomial([1,2,3,0,5])
        p2 = Polynomial([1,2,2])
        self.assertEqual(p2-p1, Polynomial([-1,-2,-2,2,-3]))

    def test_eq(self):
        p11 = Polynomial([3,2,1])
        p12 = Polynomial([3,2,1])
        self.assertTrue(p11==p12)
        
    def test_neg(self):
        p13 = Polynomial([])
        p13[-3] = 3
        p14 = Polynomial([])
        p14[-3] = 3
        self.assertEqual(p13,p14)
<<<<<<< HEAD

    def test_sparse_zeros(self):
        n = 10000
        p = Polynomial([0]*n)
        q = Polynomial()

        p_size =sum(sys.getsizeof(getattr(p,x)) for x in vars(p))
        q_size =sum(sys.getsizeof(getattr(q,x)) for x in vars(q))        
        factor_increase = p_size/q_size
        self.assertEqual(p,q)
        self.assertLess(factor_increase,10,msg='Implementation not sparse, init with {} zeros'.format(n))
    
"""
=======
    
    
    
        """

>>>>>>> 318940eb26d0d40c9eeea05e1574534f9d78e415
    
        
    def test_rmult(self):
        p5 = Polynomial([1,2,3,0,5])
        p6 = Polynomial([1,2,2])        
        self.assertEqual(p6*p5, Polynomial([1,3,7,7,11,5,10]))
    
    def test_eval(self):
        p9 = Polynomial([1,2,3])
        self.asssertEqual(p9.eval(3),18)     
        
    def test_eval(self):
        p9 = Polynomial([1,2,3])
        self.asssertEqual(p9.eval(3),18) 
<<<<<<< HEAD
=======

>>>>>>> 318940eb26d0d40c9eeea05e1574534f9d78e415
    def test_mult(self):
        p5 = Polynomial([1,2,3, 0, 5])
        p6 = Polynomial([3,0,2])        
        self.assertEqual(p5*p6, Polynomial([3,6,12,6,24,15]))
    
    
<<<<<<< HEAD
 """ 
=======
 """       
    
        
    
>>>>>>> 318940eb26d0d40c9eeea05e1574534f9d78e415
