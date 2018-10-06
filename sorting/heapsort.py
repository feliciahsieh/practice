#!/usr/bin/python3
# heap sort
import time


def heapify(arr, leng, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    # check left child
    if left < leng and arr[index] < arr[left]:
        largest = left

    # check right child
    if right < leng and arr[largest] < arr[right]:
        largest = right

    # Change root if needed
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, leng, largest)


def heapsort(array=[23, 6, 1, 90, 39, 30, 99, 15, 88, 0]):
    print("START:\n{}\n".format(array))

    length = len(array)
    # Build max heap
    for i in range(length, -1, -1):
        heapify(array, length, i)

    # Remove Largest element and reheapify
    for i in range(length-1, 0, -1):
        # swap root and leaf (leaf becomes largest value)
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)

        print("i:{} {}".format(i, array))
    return array


startTime = time.time()

result = heapsort()
print("\nFINAL:\n{}".format(result))
print("Execution took {:1.6f} sec".format(time.time() - startTime))
