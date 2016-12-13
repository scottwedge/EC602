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

def sol(grid, words, word_lengths):
    normalize(grid)
    if not word_lengths:
        words.sort()
        solution = ' '.join(words)
        if solution not in SOLUTIONS:
            SOLUTIONS.add(solution)
            print("Solution: " + solution)
        return
    n = len(grid)
    for row in range(n):
        for col in range(n):
            if is_valid(grid, row, col):
                solve(copy.deepcopy(grid), row, col, list(words), '', list(word_lengths))

"""
def make_game(game)
    make array of specified size
    populate with grid values
    all possible permutations of lengths
        make permutations of one length and subtract
        make permutations of another length
        repeat
    
"""
# swap letters

# apply gravity

<<<<<<< HEAD
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
=======
# check adjacent

if __name__ == '__main__':
    
    with open(sys.argv[1], "r") as small_list:
        words = sorted(list(small_list))
    
    #with open('large_word_list.txt', "r") as large_list:
    #    largewords = list(large_list)
    with open(sys.argv[2], "r") as large_list:
        largewords = sorted(list(large_list))
    
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
    print(all_puzzles[0])
    
    
    letters = []
    for i in range(len(all_puzzles[0]['grid'])):
        letters.append(all_puzzles[0]['grid'][i])
        print(all_puzzles[0]['grid'][i])
    
    
    print(letters)
    let = [[y for y in x] for x in [x for x in all_puzzles[0]['grid']]]
    print(let)
    
    lengths = [int(x) for x in all_puzzles[0]['lengths']]
    print(lengths)
    
    #solve(let, [], lengths)
    
    """
    Answers = []
    def solve(grid, words, etc):
        if all words found:
            answers.append(new answers)
        
        for all possible new workds:
            csolve(newgrid, newwords, etc)
    """
>>>>>>> b686c131cd01201a355a547c3e93809e43b833fe
