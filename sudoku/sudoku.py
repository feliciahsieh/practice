#!/usr/bin/python3
# Sudoku.py - solves a sudoku 9x9 puzzle from a json file

import json
import numpy as np
from pprint import pprint
import time

EMPTYCELL = 0
GRIDSIZE = 9

fullSet = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def createPossible(grid=[[]], P=[[]]):
    # Create Possible values of 1..9 for each Cell

    for row in range(0, GRIDSIZE):
        for col in range(0, GRIDSIZE):
            if grid[row][col] == 0:
                # Create possible values in row and subract from full set
                r = fullSet - set(grid[row])

                # Create possible values in column and subtract
                c = r - set(grid[:, col])

                # Create possible values in cube and subtract
                rowStart = (row//3) * 3
                colStart = (col//3) * 3
                P[row][col] = list(c - set(
                    grid[rowStart:rowStart+3, colStart:colStart+3].flatten()))
    return P


def updateGrid(g=[[]], p=[[]]):
    # Process grid with Possible array values as cells are solved

    for row in range(0, GRIDSIZE):
        for col in range(0, GRIDSIZE):
            # Found correct cell value = Only 1 possible value
            if np.size(p[row, col]) == 1:
                singleton = p[row][col][0]
                g[row][col] = singleton

                # Remove from Possible list
                p[row, col].remove(singleton)

                # Remove from Possible in row
                for c in range(0, GRIDSIZE):
                    if singleton in p[row, c]:
                        p[row, c].remove(singleton)

                # Remove from Possible in col
                for r in range(0, GRIDSIZE):
                    if singleton in p[r, col]:
                        p[r, col].remove(singleton)

                # Remove from Possible in cube
                rowStart = row//3*3
                colStart = col//3*3
                for i in range(rowStart, rowStart+3):
                    for j in range(colStart, colStart+3):
                        if singleton in p[i, j]:
                            p[i, j].remove(singleton)
    return g, p


def isSolved(grid=[[]]):
    # Checks if sudoku puzzle is completely solved in row, column, and 3x3 cube

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
    for cRow in range(0, GRIDSIZE, 3):
        for cCol in range(0, GRIDSIZE, 3):
            isCubeGood &= (
                set(grid[cRow:cRow+3, cCol:cCol+3].flatten()) == fullSet)
    #print("isSolved: Cubes are Good...{}".format(isCubeGood))
    return isRowGood and isColGood and isCubeGood


def printStatus(grid=[[]]):
    # Print status of cubes. Used for testing only

    unique, counts = np.unique(grid, return_counts=True)
    print("counts: {}".format(dict(zip(unique, counts))))
    return counts


def printGrid(grid=[[]]):
    # Print entire sudoku grid. Used for output and testing

    for row in range(0, GRIDSIZE):
        print("{}".format(grid[row]))


def printP(P=[[]]):
    # Print Possible values. Used for testing only

    for row in range(0, GRIDSIZE):
        for col in range(0, GRIDSIZE):
            if col % 3 == 0:
                print("\nP({},{})---".format(row, col), end="")
            print("{}  ".format(P[row][col]), end="")
    print()


def initialize():
    # P is an array of Possible values for each cell

    P = np.empty(shape=[GRIDSIZE, GRIDSIZE], dtype=object)
    for r in range(0, GRIDSIZE):
        for c in range(0, GRIDSIZE):
            P[r, c] = []
    return P

def sudoku():
    # Solves Easy-rated sudoku puzzles iteratively

    with open('sudoku.json', encoding='utf-8') as f:
        data = json.loads(f.read())

    for num in range(len(data['puzzle'])):
        grid = np.array(data['puzzle'][num], dtype=np.uint8)

        print("\nThe original sudoku is:")
        printGrid(grid)

        possibleValues = initialize()

        possibleValues = createPossible(grid, possibleValues)
        while not isSolved(grid):
            #printStatus(grid)
            grid, possibleValues = updateGrid(grid, possibleValues)
            #count = printStatus(grid)
            #print("{} left to fill".format(count[0]))

        print("\nThe solution is:")
        printGrid(grid)


# Main program
start = time.time()
sudoku()
end = time.time()
print("Time to run: {}".format(end - start))
# time to run iteratively: 0.02588820457458496
