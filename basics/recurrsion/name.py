def printName(i, n):
    if i > n:
        return
    print("Hello World")
    printName(i+1, n)


x = 4
printName(1, x)
