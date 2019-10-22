import time
def solve(content):
    '''
    '''
    N, M = content[0].split()
    print str(N)
    print str(M)
    bestPathes= []
    slope = content[1:]
    for i in range(0, int(M)):
        pos = (0, i)
        if walkable(slope, pos):
            newPath = findPossiblePathsFromPos(slope=slope,  pos= pos, lastMove=(0,0))
            if newPath>-1:
                bestPathes.append(newPath)
    return min(bestPathes or [-1])

MOVES = [(1, 0), (0, 1), (0, -1)]

def walkable(slope, pos):
    try: 
        return slope[pos[0]][pos[1]] == '.'
    except IndexError:
        return False

def canPass(slope, pos, move):
    newPos = (pos[0] + move[0], pos[1] + move[1])
    if walkable(slope, newPos):
        return newPos


def findPossiblePathsFromPos(slope, pos, lastMove):
    minAv=None
    # printSlopeWPos(slope,pos)
    avMoves = MOVES[:]
    ## No infinite loop
    if lastMove == (0,1):
        avMoves.remove((0,-1))
    if lastMove == (0,-1):
        avMoves.remove((0,1))
    ## Ending
    if pos[0]==len(slope)-1:
        return 0
    for move in avMoves:
        newPos = canPass(slope, pos, move)
        if newPos:
            underLen = findPossiblePathsFromPos(slope, newPos, move)
            if underLen != None:
                minAv = min((1+underLen), (minAv or underLen+2))
                if underLen == len(slope) - pos[0]-1:
                    break
    if not minAv:
        dontComeBack(slope, pos)
    return minAv

def dontComeBack(slope, pos):
    # Dead position don't come back
    lineSplit = list(slope[pos[0]])
    lineSplit[pos[1]] = 'X'
    slope[pos[0]] = ''.join(lineSplit)

def printSlopeWPos(slope,pos):
    slopeWPos = slope[:]
    lineSplit = list(slopeWPos[pos[0]])
    lineSplit[pos[1]] ='O'
    slopeWPos[pos[0]]= ''.join(lineSplit)
    for l in slopeWPos:
        print l
    print ''
    print ''
    print ''
    print ''
    print ''
    time.sleep(0.5)
