array1 = []
for value in A:
    exists = False
    for repeat in array1:
        if value == repeat[0]:
            exists = True
            repeat[1] += 1
    if exists == False:
        array1.append([value, 0])
for repeat in array1:
    if repeat[1] == 0:
        print(repeat[0])
