#!/usr/bin/python3

import sys

fibonacci = __import__('fibonacciWebSvc').fibonacci

if len(sys.argv) == 2:
    result = fibonacci(sys.argv[1])
    if result is not None:
        print(result)
else:
    print("Usage: ./virtustream.py [n]")
