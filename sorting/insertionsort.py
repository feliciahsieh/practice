# insertion sort
# DOESN'T WORK YET
array = [23, 6, 1, 90, 30, 39, 99, 15, 88, 0]

print("START: {}".format(array))

if array is None:
    exit(0)

i = 0
while (i + 1) != len(array):
    if array[i] > array[i + 1]:
        curr = i + 1
        array[i], array[i + 1] = array[i + 1], array[i]
        if (curr - 1) == -1:
            i = curr
        print("swap: {}".format(array))

        while (curr - 1) != -1:
            if array[curr] >= array[curr - 1]:
                break;
            prev = curr - 1
            array[prev], array[curr] = array[curr], array[prev]
            if curr - 1 == -1:
                i = curr
            print("swap: {}".format(array))
    else:
        i += 1

print("FINAL: {}".format(array))
