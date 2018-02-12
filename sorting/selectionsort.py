# selection sort
array = [23, 6, 1, 90, 30, 39, 99, 15, 88, 0]
print("{}".format(array))

for i in range(0, len(array)):
    min = i
    for j in range(i, len(array)):
        if (array[min] > array[j]):
            min = j
    array[i], array[min] = array[min], array[i]
    print("{}".format(array))
print("final:\n{}".format(array))
