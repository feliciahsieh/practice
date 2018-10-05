#!/usr/bin/python3
# quicksort using recursion and python3 lists
import time

startTime = time.time()

array = [23, 6, 1, 90, 30, 39, 99, 15, 88, 0]
print("START:\n{}\n".format(array))

def mergeSort(array):
    print("Splitting",array)
    if len(array) > 1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

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

mergeSort(array)
print("\nFINAL:\n{}".format(array))
print("Execution time: {} sec".format(time.time() - startTime))
