import sys

DIC_FILE = None
HOLD = None
DICTO = None
PRE_DIC = None

class TriePrefix:
    def __init__(self):
        self.isWord = False
        self.root = []
        for n in range(26):
            self.root.append(None)

    def createKey(self, wrd):
        if (len(wrd) == 0):
            self.isWord = True
        else:
            #convert hex to dec
            letter = ord(wrd[0]) - 65
            if (self.root[letter] == None):
                newBranch = TriePrefix()
                newBranch.createKey(wrd[1:])
                self.root[letter] = newBranch
            else:
                self.root[letter].createKey(wrd[1:])

    def prefix(self, lttr):
        return self.root[ord(lttr) - 65]

    def isKey(self, wrd):
        if (len(wrd) == 0):
            return True
        else:
            letter = ord(wrd[0]) - 65
            if self.root[letter] == None:
                return False
            else:
                return isKey(wrd[1:])

def prefixesTrie(dic):
    global DIC_FILE
    global HOLD
    global DICTO
    global PRE_DIC

    DIC_FILE = dic
    HOLD = '-'
    DICTO = []
    PRE_DIC = TriePrefix()

    with open(DIC_FILE, "r") as f:
        l = f.readlines()

    for line in l:
        DICTO.append(line.strip('\n'))

    for w in DICTO:
        PRE_DIC.createKey(w)

def solAppend(s, ans):
    if s:
        ans.append(s)

def trace(solution, grid, x, y, letter, row, col, word, step, preTree):
    global HOLD
    global DICTO

    if [x,y] in step:
        return False

    if (x >= col) or (y >= row) or (x < 0) or (y < 0) or (grid[x][y] == HOLD):
        return False

    word += grid[x][y]
    nextStep = list(step)
    nextStep.append([x, y])
    preTree = preTree.prefix(word[-1])
    letter -= 1

    if preTree == None:
        return False

    if letter == 0:
        if preTree.isWord == True:
            return [grid, word, nextStep]
        else:
            return False

    #check paths
    checkSol = trace(solution, grid, x + 1, y, letter, row, col, word, nextStep, preTree)
    solAppend(checkSol, solution)

    checkSol = trace(solution, grid, x + 1, y + 1, letter, row, col, word, nextStep, preTree)
    solAppend(checkSol, solution)

    checkSol = trace(solution, grid, x, y + 1, letter, row, col, word, nextStep, preTree)
    solAppend(checkSol, solution)

    checkSol = trace(solution, grid, x - 1, y, letter, row, col, word, nextStep, preTree)
    solAppend(checkSol, solution)

    checkSol = trace(solution, grid, x, y - 1, letter, row, col, word, nextStep, preTree)
    solAppend(checkSol, solution)

    checkSol = trace(solution, grid, x - 1, y - 1, letter, row, col, word, nextStep, preTree)
    solAppend(checkSol, solution)

    checkSol = trace(solution, grid, x + 1, y - 1, letter, row, col, word, nextStep, preTree)
    solAppend(checkSol, solution)

    checkSol = trace(solution, grid, x - 1, y + 1, letter, row, col, word, nextStep, preTree)
    solAppend(checkSol, solution)

def applyGravity(grid, row, col):
    global HOLD
    global PRE_DIC
    for r in range(row - 1):
        for c in range(col):
            if (grid[r + 1][c] == HOLD):
                for t in reversed(range(r + 1)):
                    grid[t + 1][c] = grid[t][c]
                grid[0][c] = HOLD

if __name__ == "__main__":

    #get dictionary file

    #get rows columns and words
    rows = 0;
    cols = 0;
    ansWords = 0;

    #get lengths of words

    #check to see that lengths add up

    #get letter grid in rows

    inputFile = sys.argv[1]
    with open(inputFile) as f:
        info = f.readlines()

    prefixesTrie(info[0].strip('\n'))

    rcw = info[1].strip('\n').split(" ")
    if len(rcw) != 3:
        print("ERROR: The first line of " + inputFile + " should contain only <Number of Rows> <Number of Columns> <Number of Words>")

    rows = int(rcw[0])
    cols = int(rcw[1])
    ansWords = int(rcw[2])

    lets = info[2].strip('\n').split(" ")
    for i in range(len(lets)):
        lets[i] = int(lets[i])
    
    if len(lets) != ansWords:
        print("ERROR: The second line of " + inputFile + " should have the same number of numbers as the number of words")

    info = info[3:]
    
    grid = []
    for r in info:
        r = r.strip('\n')
        l = r.split(" ")
        grid.append(l)

    solved = [[grid,[]]]
    nGrid = 0;
    nWord = 1;
    nStep = 2;
    nx = 0;
    ny = 1;

    for runs in range(ansWords):
        possibleSol2 = []
        for grp in solved:
            possibleSol = []
            for r in range(rows):
                for c in range(cols):
                    sol = trace(possibleSol, grp[nGrid], r, c, lets[runs], rows, cols, "", [], PRE_DIC),
                    if sol:
                        possibleSol.append(sol)
            #let letters fall down
            for pSol in possibleSol:
                wList = list(grp[nWord])
                wList.append(pSol[nWord])

                #copy of temp sol
                nextGrid = []
                for r in range(rows):
                    nextGrid.append(list(pSol[nGrid][r]))

                for step in pSol[nStep]:
                    newX = step[nx]
                    newY = step[ny]
                    nextGrid[newX][newY] = HOLD;

                #apply gravity
                applyGravity(nextGrid, rows, cols)
                possibleSol2.append([nextGrid, wList])

        solved = possibleSol2

    #print final solution
    solved.sort()
    for s in solved:
        print(s[nWord])



