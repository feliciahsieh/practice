#!/bin/python3

import sys

def timeConversion(s):
    # strip min, sec out of string
    tStr = s[2:len(s)-2]
    # check for am/pm
    if "AM" in s or "am" in s:
        if s[0:2] == '12':
            tStr = '00' + tStr
        else:
            tStr = s[0:2] + tStr
    else:
        if s[0:2] == '12':
            tStr = '12' + tStr
        else:
            tStr = str((int(s[0:2]) + 12)) + tStr
    return tStr

s = input().strip()
result = timeConversion(s)
print(result)
