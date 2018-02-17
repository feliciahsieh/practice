#!/bin/python3

import sys

def caesarCipher(s, k):
    # Complete this function
    res = ''
    for i in s:
        if i.isalpha():
            a = 'A' if i.isupper() else 'a'
            res += chr(ord(a) + ( ord(i) - ord(a) + k) % 26)
        else:
            res += i
    return res

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
