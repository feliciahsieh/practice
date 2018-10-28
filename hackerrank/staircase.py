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
    for i in range(1, n+1):
        print(" "*(n-i), "#"*i, "\n", end="", sep="")

if __name__ == '__main__':
    n = int(input())

    staircase(n)
