#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w13_wordbrainsolver.py
"""
import json
import numpy as np
import itertools
import sys
#w13_wordbrainsolver small_word_list.txt large_word_list.txt <puzzles.txt >solutions.txt

#with open('small_word_list.txt', "r") as small_list:
#    smallwords = list(small_list)

#list of dictionaries
all_puzzles = []

WORDS = []

def make_puzzles(puz):
    all_puzzles.append(puz)

def make_perms(word, n):
    return [''.join(p) for p in itertools.permutations(word, n)]


# apply gravity

# check adjacent

if __name__ == '__main__':
    
    #with open(sys.argv[1], "r") as small_list:
        #words = sorted(list(small_list))
    
    #with open('large_word_list.txt', "r") as large_list:
    #    largewords = list(large_list)
    with open(sys.argv[2], "r") as large_list:
        WORDS = sorted(list(large_list))
    
    while True:
        inline = input("")    
        try:
            #makes line a dictionary        
            puzzline = json.loads(inline)
            all_puzzles.append(puzzline)
            #print(all_puzzles)
        except:
            break
    
    
    
    # print(all_puzzles[0]['grid'][0][0]) this works down the letter
    # print(all_puzzles)
    
    letters = []
    for i in range(len(all_puzzles[2]['grid'])):
        letters.append(all_puzzles[2]['grid'][i])
        print(all_puzzles[2]['grid'][i])
    
    
    print(letters)
    
    let = [[y for y in x] for x in [x for x in all_puzzles[2]['grid']]]
    l = np.array(let)
    l = np.rot90(l)
    l = np.flipud(l)
    print(l)   
    
    grid = []
    for r in range(len(l)):
        grid.append(l[r])
        
    print(grid[0][0])
    rows = len(grid)
    cols = len(grid[0])
    size = all_puzzles[2]['size']
    
    if(size != rows and size != cols):
        print("Error size conflict")
    
    lengths = [int(x) for x in all_puzzles[2]['lengths']]
    print(lengths)
    print(len(lengths))
    
