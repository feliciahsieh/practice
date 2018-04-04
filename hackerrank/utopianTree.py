#!/bin/python3

import sys

def utopianTree(n):
    if n == 0:
        return 1
    if n == 1:
        return 2

    spring = 1 # doubles height
    summer = 1 # increases height by 1
    height = 1

    #print('cycle: ', 0, ' height: ', height, ' spring: ', spring, ' summer: ', summer)

    for i in range(1, n + 1):
        if i%2==0: #even (Summer)
            height = spring + 1
            summer = height
        else: #odd (Spring)
            height = summer * 2
            spring = height

        #print('cycle: ', i, ' height: ', height, ' spring: ', spring, ' summer: ', summer)
    return height

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        print(result)
