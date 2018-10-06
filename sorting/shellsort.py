#!/usr/bin/python3
# shellsort
import time


def shellsort(array=[23, 6, 1, 90, 30, 39, 99, 15, 88, 0]):
    print("START:\n{}\n".format(array))

    gaps = [4, 2, 1]
    for gap in gaps:
        for i in range(0, len(array)-gap):
            if (i+gap) < len(array):
                # swap if out of order
                if array[i] > array[i+gap]:
                    array[i], array[i+gap] = array[i+gap], array[i]
                    j = i - gap
                    while array[i] < array[j] and j > 0:
                        array[i], array[j] = array[j], array[i]
                        j -= gap
                    print(array)
    return array


startTime = time.time()
result = shellsort()
print("\nFINAL:\n{}".format(result))
print("Execution took {:1.6f} sec".format(time.time() - startTime))
