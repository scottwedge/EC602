import sys

DIC_FILE = None
HOLD = None
DICT = None
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

    def prefix(self, lttr)
        return, self.root[ord(lttr) - 65]

    def isKey(self, wrd)
        if (len(wrd) == 0):
            return True
        else:
            letter = ord(wrd[0]) - 65
            if self.root[letter] == None:
                return False
            else
                return isKey(wrd[1:])

def prefixesTrie(dict):
    global DIC_FILE
    global HOLD
    global DICT
    global PRE_DIC

    DIC_FILE = dict
    HOLD = '-'
    DICT = []
    PRE_DIC = TriePrefix()

    with open(DIC_FILE) as w:
        l = w.readLines()

    for line in l:
        DICT.append(line.strip('\n'))

    for w in DICT:
        PRE_DIC.createKey(w)

def trace(solution, grid, x, y, letters, row, col, word, step, preTree):
    global HOLD
    global DICT


if __name__ == "__main__":
    global HOLD
    global PRE_DIC

    #get dictionary file

    #get rows columns and words
    rows = 0;
    cols = 0;
    ansWords = 0;

    #get lengths of words

    #check to see that lengths add up

    #get letter grid in rows

    solved = [[gird,[]]]
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
                    sol = trace(possibleSol, grp[nGrid]),
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
                    newX = nextPath[]
                    newY = nextPath[]
                    nextGrid[newX][newY] = HOLD;

                #apply gravity
                applyGravity(nextGrid, rows, cols)
                possibleSol2.append([nextGrid, wList])

        solved = possibleSol2

    #print final solution
    solved.sort()
    for s in solved:
        print(s[nWord])



