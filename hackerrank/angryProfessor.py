#!/bin/python3

import sys

def angryProfessor(k, a):
    onTime = late = 0
    for i in range(len(a)):
        if a[i] <= 0:
            onTime += 1
        elif a[i] > 0:
            late += 1

    if onTime >= k:
        return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = list(map(int, input().strip().split(' ')))
        result = angryProfessor(k, a)
        print(result)
