#!/bin/python3

import sys

def breakingRecords(score):
    min = max = score[0]
    qtyMax = qtyMin = 0
    for i in score[1:]:
        if i > max:
            qtyMax += 1
            max = i
        elif i < min:
            qtyMin += 1
            min = i
    return [qtyMax, qtyMin]

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))
