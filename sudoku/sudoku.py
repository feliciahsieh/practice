#!/usr/bin/python3

import numpy as np


EMPTYCELL = 0
GRIDSIZE = 9

grid = np.array([
    [3, 6, 0, 2, 0, 5, 0, 0, 0],
    [0, 1, 5, 4, 0, 3, 0, 8, 0],
    [0, 0, 4, 9, 1, 0, 0, 0, 0],

    [4, 5, 7, 0, 0, 0, 0, 9, 1],
    [0, 0, 2, 0, 0, 0, 3, 0, 0],
    [8, 3, 0, 0, 0, 0, 7, 6, 4],

    [0, 0, 0, 0, 9, 4, 8, 0, 0],
    [0, 2, 0, 3, 0, 6, 1, 4, 0],
    [0, 0, 0, 8, 0, 2, 0, 7, 9]
], dtype=np.uint8)
#grid = np.array([
#    [4, 5, 0, 8, 0, 0, 9, 0, 0],
#    [0, 9, 0, 0, 5, 6, 0, 0, 4],
#    [1, 0, 0, 0, 0, 0, 0, 0, 7],

#    [2, 6, 0, 5, 4, 0, 0, 9, 0],
#    [0, 0, 4, 1, 0, 2, 3, 0, 0],
#    [0, 7, 0, 0, 6, 9, 0, 4, 8],

#    [7, 0, 0, 0, 0, 0, 0, 0, 9],
#    [8, 0, 0, 4, 9, 0, 0, 7, 0],
#    [0, 0, 9, 0, 0, 3, 0, 2, 5]
#], dtype=np.uint8)

# P is an array of Possible values for each cell
P = np.empty(shape=[GRIDSIZE, GRIDSIZE], dtype=object)
for r in range(0, GRIDSIZE):
    for c in range(0, GRIDSIZE):
        P[r, c] = []

fullSet = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def createPossible():
    # Create possible values for each Cell
    for row in range(0, GRIDSIZE):
        for col in range(0, GRIDSIZE):
            if grid[row][col] == 0:
                # Create possible values in rows
                r = fullSet - set(grid[row])

                # Create possible values in columns
                c = r - set(grid[:, col])

                # Create possible values in cubes
                rowStart = (row//3) * 3
                colStart = (col//3) * 3
                P[row][col] = list(c - set(
                    grid[rowStart:rowStart+3, colStart:colStart+3].flatten()))

def updateGrid():
    # Process grid with Possible array values
    for row in range(0, GRIDSIZE):
        for col in range(0, GRIDSIZE):
            # Found correct cell value = Only 1 possible value
            if np.size(P[row, col]) == 1:
                singleton = P[row][col][0]
                grid[row][col] = singleton

                # Remove from Possible list
                P[row, col].remove(singleton)
                # Remove from Possible in row
                for c in range(0, GRIDSIZE):
                    if singleton in P[row, c]:
                        P[row, c].remove(singleton)

                # Remove from Possible in col
                for r in range(0, GRIDSIZE):
                    if singleton in P[r, col]:
                        P[r, col].remove(singleton)

                # Remove from Possible in cube
                rowStart = row//3*3
                colStart = col//3*3
                for i in range(rowStart, rowStart+3):
                    for j in range(colStart, colStart+3):
                        if singleton in P[i, j]:
                            P[i, j].remove(singleton)

def isSolved():
    # Check each row
    isRowGood = True
    for row in range(0, GRIDSIZE):
        isRowGood &= (set(grid[row]) == fullSet)
    #print("isSolved: Rows are Good...{}".format(isRowGood))

    # Check each column
    isColGood = True
    for col in range(0, GRIDSIZE):
        isColGood &= (set(grid[:, col]) == fullSet)
    #print("isSolved: Cols are Good...{}".format(isColGood))

    # Check each cube
    isCubeGood = True
    for cubeRow in range(0, GRIDSIZE, 3):
        for cubeCol in range(0, GRIDSIZE, 3):
            isCubeGood &= (set(grid[cubeRow:cubeRow+3, cubeCol:cubeCol+3].flatten()) == fullSet)
    #print("isSolved: Cubes are Good...{}".format(isCubeGood))
    return isRowGood and isColGood and isCubeGood

def printStatus():
    unique, counts = np.unique(grid, return_counts=True)
    #print("counts: {}".format(dict(zip(unique, counts))))
    return counts

def printGrid():
    for row in range(0, GRIDSIZE):
        print("{}".format(grid[row]))

def printP():
    for row in range(0, GRIDSIZE):
        for col in range(0, GRIDSIZE):
            if col%3 == 0:
                print("\nP({},{})---".format(row,col), end="")
            print("{}  ".format(P[row][col]), end="")
    print()

# main program
print("The original sudoku is:")
printGrid()

createPossible()
while not isSolved():
    updateGrid()
    count = printStatus()
    #print("{} left to fill".format(count[0]))

print("\nThe solution is:")
printGrid()
