#!/bin/python3

import sys

def solve(grades):
    g = []
    for i in grades:
        if i < 38:
            g.append(i)
        else:
            mult = int(i/5)
            diff = int(((mult + 1) * 5) - i)
            if diff < 3:
                g.append((mult + 1) * 5)
            else:
                g.append(i)
    return (g)

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
