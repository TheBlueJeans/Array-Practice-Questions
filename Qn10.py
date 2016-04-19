B = [8, 9, 3, 5]
C = [5, 10, 12]
intersection = []
for value in A:
    if value in B and value in C:
        intersection.append(value)
print(intersection)
