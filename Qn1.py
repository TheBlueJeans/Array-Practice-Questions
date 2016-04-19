count = 0
array1 = []
array2 = []
for value in A:
    if value not in array1:
        array1.append(value)
    elif value in array1:
        if value not in array2:
            array2.append(value)
print(len(array2))
