# bubblesort
array = [23, 6, 1, 90, 30, 39, 99, 15, 88, 0]

print(id(array))
for i in range(len(array)):
    for j in range(0, len(array) - 1):
        if (array[j] > array[j + 1]):
            print("{}".format(array))
            #temp = array[j]
            #array[j] = array[j + 1]
            #array[j + 1] = temp
            array[j], array[j + 1] = array[j + 1], array[j]
print("FINAL:\n{}".format(array));
print(id(array))
