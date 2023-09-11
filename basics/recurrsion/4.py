def printToN(i, n):
    if i > n:
        return
    print(n-i+1)
    printToN(i+1, n)


x = 4
printToN(1, x)
