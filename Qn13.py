highest2 = [None, None]
for value in A:
    if highest2 == [None, None]:
        highest2[1] = value
    elif highest2[0] == None:
        if value > highest2[1]:
            highest2[0] = highest2[1]
            highest2[1] = value
        else:
            highest2[0] = value
    elif value > highest2[1]:
        highest2[0] = highest2[1]
        highest2[1] = value
    elif value > highest2[0]:
        highest2[0] = value
print(highest2)
