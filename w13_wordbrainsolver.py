#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w13_wordbrainsolver.py
"""

"""
Input example
{"grid": ["hos", "equ", "era"], "size": 3, "lengths": [3,6]}
{"grid": ["yeho", "slnl", "onca", "nnab"], "size": 4, "lengths": [5,5,6]}
{"grid": ["niba", "capt", "haos", "nwmn"], "size": 4, "lengths": [4,5,3,4]}
{"grid": ["vittm","aposi","nvami","merep","oordb"],"size":5,"lengths":[4,7,7,7]}
"""

import json
import numpy as np
from collections import Counter
import itertools
import sys
from pprint import pprint
import re

#w13_wordbrainsolver small_word_list.txt large_word_list.txt <puzzles.txt >solutions.txt

#with open('small_word_list.txt', "r") as small_list:
#    smallwords = list(small_list)

#list of dictionaries
all_puzzles = []

def make_puzzles(puz):
    all_puzzles.append(puz)

def make_perms(word, n):
    return [''.join(p) for p in itertools.permutations(word, n)]

"""
def make_game(game)
    make array of specified size
    populate with grid values
    all possible permutations of lengths
        make permutations of one length and subtract
        make permutations of another length
        repeat
    
"""

with open(sys.argv[1], "r") as small_list:
    words = list(small_list)

#with open('large_word_list.txt', "r") as large_list:
#    largewords = list(large_list)
with open(sys.argv[2], "r") as large_list:
    largewords = list(large_list)

puzzles = {}
while True:
    inline = input("")
    try:
        #makes line a dictionary        
        puzzline = json.loads(inline)
        puzzles.update(puzzline)
        make_puzzles(puzzles)
        #print(puzzline)
    except:
        break

# print(all_puzzles[0]['grid'][0][0]) this works down the letter
for i in all_puzzles:
    print(i)

for i in range (0, all_puzzles[0]['size']):
    for j in range (0, all_puzzles[0]['size']):
        word1 = all_puzzles[0]['grid'][i][j] + all_puzzles[0]['grid'][i+1][j+1]
        print(word1)
