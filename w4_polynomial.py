# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w4_polynomial.py
10/2/16
Siggi&John
"""
# -*- coding: utf-8 -*-
"""
Provides the class Complex() to mimic the built-in complex class.
"""

class Polynomial():

    def __init__(self,coef = {}):
        exp = len(coef) - 1
        result = {}
        for c in coef:
            if (c != 0):
                result[exp] = c
            exp -= 1
        self.coef = result
    
    def exponents(self):
        return self.coef.keys()
        
    def __getitem__(self,key):
        return self.coef[key]        
        
    def __setitem__(self,key, newcoef):
        self.coef[key] = newcoef
        
    def __delitem__(self,key):
        del self.coef[key]
        
    def __str__(self):
        res = ""        
        for i in reversed(sorted(self.exponents())):
            if(self[i]!=0):
                if len(res) > 0:
                    res = res + " + "
                res = res + str(self[i]) + "x^" + str(i)
            
        return res
            

    def __add__(self,a):
        "Add a+b"
        psum = self
        for k in a.exponents():
            if k in psum.exponents():
                psum[k] += a[k]
            else:
                psum[k] = a[k]
                
        return psum
    
    def __sub__(self,a):
        "Subtract a-b"
        psum = self
        for k in a.exponents():
            if k in psum.exponents():
                psum[k] +=  -1 * a[k]
            else:
                psum[k] = a[k]
                
        return psum

    def __radd__(self,a):
        "Add a+self"
        psum = self
        for k in a.exponents():
            if k in psum.exponents():
                psum[k] += a[k]
            else:
                psum[k] = a[k]
                
        return psum

    def __rsub__(self,a):
        "Subtract b-self"
        psum = self
        for k in a.exponents():
            if k in psum.exponents():
                psum[k] += -1 * a[k]
            else:
                psum[k] = a[k]
                
        return psum

    def __mul__(self,a):
        "Return self*a."
        result = Polynomial([])
        for exp1 in self.exponents():
            for exp2 in a.exponents():
                newexp = exp1 + exp2
                newcoef = self[exp1] *  a[exp2]
                try:
                    result[newexp] += newcoef
                except KeyError:
                    result[newexp] = newcoef
        return result

    def __eq__(self,a):
        "Return if a == b"
        if len(self.coef) != len(a.coef):
            return False
        
        for i in self.coef:
            if self[i] != a[i]:
                return False
        
        return True

    def deriv(self):
            newpoly = Polynomial([])
            #length = len(self.coef)
            for i in self.coef:
                try:
                    newpoly[i-1] = self[i]*(i)
                except KeyError:
                    newpoly[i-1] = self[i]*(i)
                
            return newpoly
            
"""       
    def eval(self):
        newpoly = Polynomial([])
        length = len(self.coef)
        for i in self.coef:
            newpoly[i] = self[i] * x ** length - 1
            length -= length
        return newpoly
    
"""      
    
        
def main():
    p1 = Polynomial([1,2,3,0,5])
    print(p1)
    p1[3] = 3.1
    p1[8] = 7
    print(p1)
    p2 = Polynomial([1,1,2])
    print(p2)
    p3 = p1 + p2
    p4 = p1 - p2
    p5 = p1 * p2
    p6 = Polynomial([1,2,3])
    p7 = Polynomial([1,2,3])
    print(p3)
    print(p4)
    print(p5)
    print(p6 == p7)
    print(p1.deriv())

if __name__ == '__main__':
    main()