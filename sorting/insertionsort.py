# insertion sort

array = [23, 6, 1, 90, 39, 30, 99, 15, 88, 0]

print("START: {}".format(array))

# Traverse through 1 to len(arr)
for i in range(1, len(array)):
    key = array[i]

    # Move elements of array[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    j = i - 1
    while j >= 0 and key < array[j] :
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key
    print("{}".format(array))

print("FINAL: {}".format(array))
