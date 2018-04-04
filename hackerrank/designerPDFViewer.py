#!/bin/python3

import sys
from string import ascii_lowercase

def designerPdfViewer(h, word):
    d = {}
    i = 0
    for c in ascii_lowercase:
        d[str(c)] = h[i]
        i += 1

    max = 0
    for j in range(len(word)):
        if d[word[j]] > max:
            max = d[word[j]]
    return max * len(word)

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)
