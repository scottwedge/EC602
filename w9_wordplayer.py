#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w9_wordplayer.py
"""

import itertools
import sys

ext = False

# with open('big_wordlist.txt', "r") as word_list:
#   words = list(word_list)

with open(sys.argv[1], "r") as word_list:
    words = list(word_list)


def compress_wordlist(biglist, l):
    return [biglist.strip() for biglist in biglist if len(biglist) == l + 1]


def compare(a, b):
    return set(a) & set(b)


def test(word, n):
    perms = [''.join(p) for p in itertools.permutations(word, n)]
    newlist = compress_wordlist(words, n)
    return compare(perms, newlist)


if __name__ == '__main__':
    while(not ext):
        user_input = input()
        wrd = user_input.split()
        try:
            inword = wrd[0]
        except:
            inword = ""
        try:
            n = int(wrd[1])
        except:
            n = ""
        if(len(inword) > 0 and n > 0):
            res = test(inword, n)
            res = list(res)
            sorted_res = sorted(res)
            for n in range(len(sorted_res)):
                print(sorted_res[n])
            print(".")
        elif(n == 0):
            ext = True
        else:
            print(".")
