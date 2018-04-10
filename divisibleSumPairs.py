#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    #print("n: {} k: {} ar: {}".format(n, k, ar))
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            #print("({},{}): ".format(i,j))
            if (ar[i]+ar[j]) % k == 0:
                count+=1
    return count

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
