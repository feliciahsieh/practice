#!/usr/bin/python3
"""fibonacciWebSvc - finds Fibonacci sequence of n size
   Arguments: n - number of Fibonacci elements to return
   Returns: Fibonacci sequence as a list
   Linter: pycodestyle v2.4.0
"""


def fibonacci(n=0):
    """The web service accepts a number, n, as input and
    returns the first n Fibonacci numbers, starting from 0.
    I.e. given n=5, output shows sequence [0, 1, 1, 2, 3].
    """

    # Validate user data value, n
    try:
        n = int(n)

    except Exception as e:
        print("ERROR: {}".format(e))
        return

    if n < 0:
        print("Fibonacci: Sequence number should be greater than 0")
        return

    if n == 0:
        return []
    if n == 1:
        return [0]
    result = [0, 1]
    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])

    return result
