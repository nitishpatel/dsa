def printTriangle(self, num):
    # Code here
    for i in range(num):
        for _ in range(i + 1):
            print("*", end=" ")
        print("")

    # Print the lower half of the pattern
    for i in range(num - 1):
        for _ in range(num - i - 1):
            print("*", end=" ")
        print("")
