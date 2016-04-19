A = [1, 2, 45, 127, 9, 13, 83, 4, 5, 6, 7]
lowest = min(A)
k = int(input("Enter \n"))
array1 = [lowest] + [None]*(k-1)
for value in A:
    if None in array1:
        if value != lowest:
            for i in range(len(array1)):
                if array1[i] == None or array1[i] > value:
                    array1 = (array1[:i] + [value] + array1[i:])[:-1]
                    break
    elif array1[-1] > value:
        if value != lowest:
            for i in range(len(array1)):
                if array1[i] > value:
                    array1 = (array1[:i] + [value] + array1[i:])[:-1]
                    break
print(array1[-1])
