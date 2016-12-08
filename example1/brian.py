#!/usr/bin/env python
# Wordbrain solver
 
import bisect
import copy
import sys
 
WORDS = []
 
def is_word(word):
    ind = bisect.bisect_left(WORDS, word)
    if ind == -1:
        return False
    return WORDS[ind] == word
 
def is_prefix(word):
    ind = bisect.bisect_left(WORDS, word)
    if ind == -1:
        return False
    return WORDS[ind].startswith(word)
 
def is_valid(grid, row, col):
    n = len(grid)
    if row < 0 or col < 0 or row >= n or col >= n:
        return False
    return grid[row][col] != '*'
 
def solve(grid, row, col, words, word, word_lengths):
    new_word = word + grid[row][col]
    tmp = grid[row][col]
    grid[row][col] = '*'
    if not is_prefix(new_word):
        grid[row][col] = tmp
        return
    if is_word(new_word) and len(new_word) in word_lengths:
        new_grid = copy.deepcopy(grid)
        new_words = list(words)
        new_words.append(new_word)
        new_word_lengths = list(word_lengths)
        new_word_lengths.remove(len(new_word))
        sol(new_grid, new_words, new_word_lengths)
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if is_valid(grid, row+dx, col+dy):
                solve(grid, row+dx, col+dy, words, new_word, word_lengths)
    grid[row][col] = tmp
 
def normalize(grid):
    n = len(grid)
    for row in range(n):
        for col in range(row):
            grid[row][col], grid[col][row] = grid[col][row], grid[row][col]
    for row in range(n):
        grid[row] = filter(lambda a: a != '*', grid[row])
        grid[row] = (n-len(grid[row]))*['*'] + grid[row]
    for row in range(n):
        for col in range(row):
            grid[row][col], grid[col][row] = grid[col][row], grid[row][col]
 
SOLUTIONS = set()
 
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
 
def main():
    if len(sys.argv) < 3:
        print("Example: %s fhfs,lsik,arce,gatn 4,4,8" % sys.argv[0])
        sys.exit(1)
    grid = [[y for y in x] for x in [x for x in sys.argv[1].split(',')]]
    word_lengths = [int(x) for x in sys.argv[2].split(',')]
    #grid = [[x for x in 'fhfs'],
    #        [x for x in 'lsik'],
    #        [x for x in 'arce'],
    #        [x for x in 'gatn']]
    #word_lengths = [4, 4, 8]
    with open('/usr/share/dict/words') as f:
        for word in f:
            WORDS.append(word.strip())
    sol(grid, [], word_lengths)
 
if __name__ == '__main__':
    main()