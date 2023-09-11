def printToN(i, n):
    if i > n:
        return
    print(i)
    printToN(i+1, n)


x = 4
printToN(1, x)
