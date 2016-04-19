count = 0
array1 = []
for value in A:
    if value not in array1:
        array1.append(value)
    else:
        count += 1
