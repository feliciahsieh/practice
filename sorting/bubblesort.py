#!/usr/bin/python3
# bubblesort
import time


def bubblesort(array=[23, 6, 1, 90, 30, 39, 99, 15, 88, 0]):
    print("START:\n{}\n".format(array))

    for i in range(len(array)):
        for j in range(0, len(array) - 1):
            if (array[j] > array[j + 1]):
                print("{}".format(array))
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


startTime = time.time()
result = bubblesort()

print("\nFINAL:\n{}".format(result))

print("Execution took {:1.6f} sec".format(time.time() - startTime))
