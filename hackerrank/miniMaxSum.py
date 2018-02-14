#!/bin/python3

import sys

def miniMaxSum(arr):
    sum=0
    min=arr[0]
    max=arr[0]
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
        sum += i
    leastSum = sum - max
    mostSum = sum - min
    print("{} {}".format(leastSum, mostSum))

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
