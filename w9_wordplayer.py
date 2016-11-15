#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w9_wordplayer.py
11/10/16
Siggi&John
"""

import itertools
import sys

#innum = "8"
ext = False;

#with open('big_wordlist.txt', "r") as word_list:
#    words = list(word_list)

with open(sys.argv[1], "r") as word_list:
    words = list(word_list)

#def get_permutations(ent, i):
#    perms = [''.join(p) for p in itertools.permutations(ent, i)]    
#    return perms

#def sort(permutations):
#    return sorted(permutations)

def compress_wordlist(biglist, l):
    return [biglist.strip() for biglist in biglist if len(biglist) == l+1]

def compare(a,b):
    return set(a) & set(b)

def test(word, n):
    perms = [''.join(p) for p in itertools.permutations(word, n)]  
    sorted_perms = sorted(perms)
    newlist = compress_wordlist(words, n)
    return compare(sorted_perms,newlist)

if __name__ == '__main__':
    while(ext == False):
        user_input = input()
        wrd = user_input.split()
        #print(wrd)
        inword = wrd[0]
        n = int(wrd[1])  # could not convert string to int: 'e'
        #print(inword)
        #print(n)
        #from timeit import Timer
        #inword = 'berdache'
        #n = 8;
        res = test(inword, n)
        res = list(res)
        #for i in res:        
        #    print(res[i])
        #ext = True
        if(n == 0):
            ext = True
        #t = Timer()
        #print(t.timeit(number=500))
