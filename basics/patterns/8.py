def pattern(num: int):
    for i in range(num):
        for _ in range(i):
            print(" ", end="")
        for _ in range((2 * (num - i)) - 1):
            print("*", end="")
        print("")
