#!/bin/python3

import sys

def sockMerchant(n, ar):
    sockSet = set(ar)
    total = []
    sockList = list(sockSet)
    for i in range(len(sockSet)):
        total.append(ar.count(sockList[i]))

    count = 0
    for i in range(len(total)):
        count += total[i] // 2

    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
