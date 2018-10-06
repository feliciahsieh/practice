#!/usr/bin/python3
# selection sort
import time

startTime = time.time()

def selectionsort(array=[23, 6, 1, 90, 30, 39, 99, 15, 88, 0]):
    print("START:\n{}\n".format(array))
    for i in range(0, len(array)):
        min = i
        for j in range(i, len(array)):
            if (array[min] > array[j]):
                min = j
        array[i], array[min] = array[min], array[i]
        print("{}".format(array))
    return array

result = selectionsort()
print("\nFINAL:\n{}".format(result))
print("Execution took {:1.6f} sec".format(time.time() - startTime))
