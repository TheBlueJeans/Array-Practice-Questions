highest = 0
lowest = None
for i in range(len(A)):
    if lowest == None or A[i] < lowest:
        lowest = A[i]
    elif A[i] > highest:
        highest = A[i]
print(lowest)
print(highest)
