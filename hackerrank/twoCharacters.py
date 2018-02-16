#!/bin/python3
# 8 out of 29 doesn't pass
# 10
# beabeefeab

import sys
import re

def twoCharaters(s):
    # Complete this function
    alphabet = sorted(set(s))
    # print("alphabet:{}".format(alphabet))

    a = []
    leng = len(alphabet)
    for c in range(leng-1):
        for d in range(c, leng):
            if c != d:
                a.append( (alphabet[c], alphabet[d]))
    # print("a: {}".format(a))

    maxResult = 0
    for i in range(len(a)):
        new = s.replace(a[i][0],"")
        new = new.replace(a[i][1],"")
        # print("no: {}{} new: {}".format(a[i][0], a[i][1], new))

        match = ''
        match = re.search(r'^((.)(?!\2).)(?:\1+\2?|\2)$', new)
        # print("match: {}".format(match))

        if match is not None and len(new) > maxResult:
            maxResult = len(new)

    return maxResult

if __name__ == "__main__":
    l = int(input().strip())
    s = input().strip()
    result = twoCharaters(s)
    print(result)
