#!/bin/python3

import sys

def beautifulDays(i, j, k):
    count = 0
    for a in range(i, j):
        original = a
        reversed = int(str(a)[::-1])
        diff = abs(reversed - original)
        if (diff % k) == 0:
            count += 1
    return count

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)
