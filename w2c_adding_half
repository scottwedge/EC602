# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w2c_addinghalf.py
9/7/16
Siggi&John
"""
# w2c_adding_half.py

from math import inf

def number_from_half(s : str):
    """return the number represented by s, a binary16 stored as a 4-character hex number"""
    sbin = bin(int(s,16))[2:]
    sstr = str(sbin)
    
    while len(sstr)<16:
        sstr = '0' + sstr

    sign = int(sstr[0])
    exp = int(sstr[1:6],2)
    frac = float("1." + str(int(sstr[6:],2)))
    newnum = (-1)**sign * frac * 2.0**(exp-15)
    
    return newnum

def main():
    """add all binary16 numbers from standard input until a non-number is entered, then print the total.
    Numbers are represented in 4-character hex string format, one per line"""
    
    #f = open('test_ah_1.txt', 'r')
    sum = 0
    
    while True:
        try:
            
            myinput = input("Enter hex number (exit to exit): ")
            #myinput = f.readline()
            sum = sum + number_from_half(myinput)
        except ValueError:
            print(sum)
            break
            


if __name__ == '__main__':
    main()
