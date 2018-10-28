#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    #Better solution
    #if ((x1<x2) && (v1<v2))
    #    print("NO")
    #else:
    #    if((v1!=v2) && ((x2-x1)%(v1-v2))==0)
    #        print("YES")
    #    else
    #        print("NO")

    if type(x1) is int and type(v1) is int and type(x2) is int and type(v2) is int:
        kx1 = x1
        kx2 = x2
        count = 0
        while count <=5000:
            kx1 += v1
            kx2 += v2
            #print("{} ?= {} ".format(kx1,kx2), end="")
            if (kx1 == kx2):
                return "YES"
            count += 1
    return "NO"

if __name__ == '__main__':
    fptr = open("a.txt", 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
