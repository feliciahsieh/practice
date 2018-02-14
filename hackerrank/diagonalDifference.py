#!/bin/python3

import sys

def diagonalDifference(a):
    posSlope = 0
    negSlope = 0
    column = len(a)
    for row in range(column):
        posSlope += a[row][column - 1 - row]
        negSlope += a[row][row]
    return abs(posSlope - negSlope)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
