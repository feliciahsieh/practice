#!/bin/python3

import sys

def hurdleRace(k, height):
    drinks = 0

    mx = max(height)
    drinks = mx - k
    if drinks >= 0:
        return drinks
    else:
        return 0

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]

    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)
