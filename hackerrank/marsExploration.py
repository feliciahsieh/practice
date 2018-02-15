#!/bin/python3

import sys

def marsExploration(s):
    qtyS1 = qtyO = qtyS2 = 0
    for i in range(0, len(s), 3):
        if s[i] != 'S':
            qtyS1 += 1
        if s[i+1] != 'O':
            qtyO += 1
        if s[i+2] != 'S':
            qtyS2 += 1
    return qtyS1 + qtyO + qtyS2

if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)
