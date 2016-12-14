# Copyright 2016, Howard Zeng
# All rights reserved

import sys

POSITION = None
FILE = None
DIC = None
PRE_DIC = None

class Trie:

    def __init__(self):
        self.root = []
        self.isWord = False
        for l in range(26):
            self.root.append(None)
        
    def addKey(self, iWord):
        if len(iWord) == 0:
            self.isWord = True
        else:
            # 65 is ord('A')
            let = ord(iWord[0]) - 97
            if self.root[let] == None:
                newTree = Trie()
                newTree.addKey(iWord[1:])
                self.root[let] = newTree
            else:
                self.root[let].addKey(iWord[1:])

    def pre(self, iLetter):
        return self.root[ord(iLetter) - 65]

def createTrie(iDictionaryFile):
    global FILE
    global DIC
    global PRE_DIC

    FILE = iDictionaryFile
    DIC = []
    PRE_DIC = Trie()

    with open(FILE) as f:
        lines = f.readlines()

    for line in lines:
        DIC.append(line.strip('\n'))
        
    for word in DIC:
        PRE_DIC.addKey(word)

def applyGravity(g, rows, cols):
    global POSITION
    
    for r in range(rows-1):
        for c in range(cols):
            if g[r+1][c] == POSITION:
                for hold in reversed(range(r+1)):
                    g[hold+1][c] = g[hold][c]
                g[0][c] = POSITION

def solAppend(s, ans):
    if s:
        ans.append(s)

# Traverses grid in all of the 8 directions on a 2d grid
def traverse(solution, grid, x, y, remain, row, col, wrd, stp, branch):
    global POSITION
    global DIC
    
    if (x >= col) or (y >= row) or (x < 0) or (y < 0) or (grid[x][y] == POSITION):
        return False
        
    if [x, y] in stp:
        return False
    
    newSteps = list(stp)
    newSteps.append([x, y])
    wrd += grid[x][y]
    remain -= 1
    letter = wrd[-1]
    branch = branch.pre(letter)
    
    if branch == None:
        return False
    
    if remain == 0:
        if branch.isWord == True:
            return [grid, wrd, newSteps]
        else:
            return False
        

    checkSol = traverse(solution, grid, x + 1, y, remain, row, col, wrd, newSteps, branch)
    solAppend(checkSol, solution)
    
    checkSol = traverse(solution, grid, x, y + 1, remain, row, col, wrd, newSteps, branch)
    solAppend(checkSol, solution)
    
    checkSol = traverse(solution, grid, x - 1, y, remain, row, col, wrd, newSteps, branch)
    solAppend(checkSol, solution)
  
    checkSol = traverse(solution, grid, x, y - 1, remain, row, col, wrd, newSteps, branch)
    solAppend(checkSol, solution)

    checkSol = traverse(solution, grid, x + 1, y + 1, remain, row, col, wrd, newSteps, branch)
    solAppend(checkSol, solution)

    checkSol = traverse(solution, grid, x - 1, y - 1, remain, row, col, wrd, newSteps, branch)
    solAppend(checkSol, solution)
        
    checkSol = traverse(solution, grid, x + 1, y - 1, remain, row, col, wrd, newSteps, branch)
    solAppend(checkSol, solution)
        
    checkSol = traverse(solution, grid, x - 1, y + 1, remain, row, col, wrd, newSteps, branch)
    solAppend(checkSol, solution)

if __name__ == "__main__":
    
    # For enumeration
    xCounter = 0
    yCounter = 1
    gridCounter = 0
    wordCounter = 1
    stepCounter = 2

    inputFile = sys.argv[1]
    
    with open(inputFile) as f:
        info = f.readlines()
    
    # Extract the dictionary file (first line of the input file)
    createTrie(info[0].strip('\n'))
    
    # Extract information of the number of rows, columns, and words (second line of the input file)
    rcw = info[1].strip('\n').split(" ")
    if len(rcw) != 3:
        print("ERROR: The first line of " + inputFile + " should contain only <Number of Rows> <Number of Columns> <Number of Words>")
    
    rows = int(rcw[0])
    cols = int(rcw[1])
    ansWords = int(rcw[2])
    
    # Extract the number of letters in each word (third line of the input file)
    wordLens = info[2].strip('\n').split(" ")
    for i in range(len(wordLens)):
        wordLens[i] = int(wordLens[i])
    
    if len(wordLens) != ansWords:
        print("ERROR: The second line of " + inputFile + " should have the same number of numbers as the number of words")
    
    
    # Extract the letter grid (the rest of the lines)
    info = info[3:]
    
    grid = []
    for row in info:
        row = row.strip('\n')
        line = row.split(" ")
        grid.append(line)
    
    solPool = [[grid,[]]]
    
    for runs in range(ansWords):
        posSol2 = []
        for ans in solPool:
            posSol1 = []
            for r in range(rows):
                for c in range(cols):
                    solution = traverse(posSol1, ans[gridCounter], r, c, wordLens[runs], rows, cols, "", [], PRE_DIC)
                    if solution:
                        posSol1.append(solution)

            for posSol in posSol1:
                tempList = list(ans[wordCounter])
                tempList.append(posSol[wordCounter])
                
                nextGrid = []
                for row in range(rows):
                    tempRow = list(posSol[gridCounter][row])
                    nextGrid.append(tempRow)
                
                for stepTaken in posSol[stepCounter]:
                    x = stepTaken[xCounter]
                    y = stepTaken[yCounter]
                    nextGrid[x][y] = POSITION

                applyGravity(nextGrid, rows, cols)
                posSol2.append([nextGrid, tempList])
        
        solPool = posSol2

    solPool.sort()
    for ans in solPool:
        print(ans[wordCounter])