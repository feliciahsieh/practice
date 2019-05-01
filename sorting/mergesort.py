#!/usr/bin/python3
# mergesort using recursion
import time


def mergesort(array=[23, 6, 1, 90, 30, 39, 99, 15, 88, 0]):
    print("Splitting", array)
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1

        print("Merging  ", array)
        return array


startTime = time.time()

print("START:\n")
result = mergesort()
print("\nFINAL:\n{}".format(result))
print("MERGESORT Execution time: {} sec".format(time.time() - startTime))
