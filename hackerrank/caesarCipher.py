#!/bin/python3

import sys

def caesarCipher(s, k):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    newAlphabet = ALPHABET[k:] + ALPHABET[0:k]
    print(ALPHABET)
    print(newAlphabet)
    encoded = ''
    for c in s:
        if c.isalpha():
            if c.isupper():
                q = ALPHABET.find(c.lower())
                encoded += newAlphabet[q].upper()
            else:
                q = ALPHABET.find(c)
                encoded += newAlphabet[q]
        else:
            encoded += c
    return encoded

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
