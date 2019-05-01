#!/usr/bin/python3
# quicksort using helper function
import time


def quickSort2(alist=[23, 6, 1, 90, 30, 39, 99, 15, 88, 0]):
    print("START:\n{}\n".format(alist))
    alist = quickSortHelper(alist, 0, len(alist) - 1)
    return alist


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        print(alist)
        quickSortHelper(alist, splitpoint + 1, last)
        print(alist)
    return alist

def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


startTime = time.time()
result = quickSort2()
print("\nFINAL:\n{}".format(result))
print("QUICKSORTb Execution took {:1.6f} sec".format(time.time() - startTime))
