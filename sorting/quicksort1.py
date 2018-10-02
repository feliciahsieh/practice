#!/usr/bin/python3
# quicksort
import time

startTime = time.time()

array = [23, 6, 1, 90, 30, 39, 99, 15, 88, 0]
print("START:\n{}\n".format(array));

def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        print("l:{} e:{} g:{}".format(less, equal, greater))
        return quicksort(less) + equal + quicksort(greater)  # Join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # Base case: when one element left in array
        return array


array = quicksort(array)
print("\nFINAL:\n{}".format(array))
print("Execution took {:1.6f} sec".format(time.time() - startTime))
