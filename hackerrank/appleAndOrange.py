#!/bin/python3

import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Complete this function
    nApples = 0
    nOranges = 0

    # calc Apples
    aToHouseStart = s - a
    aToHouseEnd = t - a

    for i in apples:
        if i >= aToHouseStart and i <= aToHouseEnd:
            nApples += 1
    # calc Oranges
    oToHouseStart = s - b
    oToHouseEnd = t - b

    for j in oranges:
        if j >= oToHouseStart and j <= oToHouseEnd:
            nOranges += 1

    print("{} {}".format(nApples, nOranges))

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)
