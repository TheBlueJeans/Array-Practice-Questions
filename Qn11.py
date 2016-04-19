repeat = []
for value in A:
    if value not in repeat:
        repeat.append(value)
    else:
        print(value)
        break
