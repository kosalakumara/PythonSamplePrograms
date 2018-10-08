array = [23,12,4,34,56,24,100]
length = len(array)


for i in range(length-1):
    for j in range(length - 1 - i):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp


print(array)
