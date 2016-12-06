"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w13_wordbrainsolver.py
"""
import json
import numpy as np
from collections import Counter
import sys
from pprint import pprint

#w13_wordbrainsolver small_word_list.txt large_word_list.txt <puzzles.txt >solutions.txt

with open(sys.argv[1], "r") as small_list:
    words = list(small_list)

with open(sys.argv[2], "r") as large_list:
    words = list(large_list)

with open('puzzles.txt') as puzzle_file:    
    puzzles = json.load(puzzle_file)

pprint(puzzles)