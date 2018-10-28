#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    if n <= 0:
        print()
    for i in range(0, n):
        print(" "*(n-i-1), "#"*(i+1), "\n", end="", sep="")

if __name__ == '__main__':
    n = int(input())

    staircase(n)
