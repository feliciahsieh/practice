#!/bin/python3

import os
import sys

def catAndMouse(x, y, z):
    cat1 = abs(z - x)
    cat2 = abs(y - z)
    if cat1 == cat2:
        return "Mouse C"
    elif cat1 < cat2:
        return "Cat A"
    else:
        return "Cat B"

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        f.write(result + '\n')

    f.close()
