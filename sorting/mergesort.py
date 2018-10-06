#!/usr/bin/python3
# quicksort using recursion and python3 lists
import time

startTime = time.time()

print("START:\n")

def mergeSort(array=[23, 6, 1, 90, 30, 39, 99, 15, 88, 0]):
    print("Splitting",array)
    if len(array) > 1:
        mid = len(array) // 2
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
        return array

result = mergeSort()
print("\nFINAL:\n{}".format(result))
print("Execution time: {} sec".format(time.time() - startTime))
