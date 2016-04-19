try:
    num = int(input("Enter \n"))
    A.index(num)
    print("Exists")
except ValueError:
    print("Doesn't exists")
