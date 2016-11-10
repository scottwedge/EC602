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

#innum = "8"

"""
def search(wrd, num):
    while i<=len(wrd):
      it=itertools.permutations(wrd,i)
      for y in it:
        a.append("".join(y))
      i+=1 
    a.sort(key=len,reverse=True)
    possible_words=[]
    for x in a:
      if uk.check(x) and x not in possible_words :
        possible_words.append(x) 
    
    possible_words.sort(key=len,reverse=True)
    for x in possible_words:
      print(x)
"""

with open('big_wordlist.txt', "r") as word_list:
    words = list(word_list)

#def get_input():
#    return raw_input('enter the word: ').rstrip('\r\n')

def compress_wordlist(biglist, l):
    return [biglist.strip() for biglist in biglist if len(biglist) == l+1]

def get_permutations(ent, i):
    perms = [''.join(p) for p in itertools.permutations(ent, i)]    
    return perms

def sort(permutations):
    return sorted(permutations)

def compare(a,b):
    #b = b.rstrip()
    return set(a) & set(b)

def test(word, n):
    p = get_permutations(word, n)
    newlist = compress_wordlist(words, n)
    return compare(p,newlist)

if __name__ == '__main__':
    # from timeit import Timer
    inword = 'berdache'
    word = inword#get_input()
    n = 8;
    res = test(word, n)
    #res = [''.join(p) for p in itertools.permutations('berdache', n-1)]
    print(res)
    # t = Timer("test(word)", "from __main__ import test, word")
    # print t.timeit(number=500)
