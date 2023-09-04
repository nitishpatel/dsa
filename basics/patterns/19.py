def print_pattern(N):
    for i in range(N, 0, -1):
        for j in range(i):
            print("*", end="")

        for j in range(2 * (N - i)):
            print(" ", end="")

        for j in range(i):
            print("*", end="")

        print()

    for i in range(0, N + 1):
        for j in range(i):
            print("*", end="")

        for j in range(2 * (N - i)):
            print(" ", end="")

        for j in range(i):
            print("*", end="")

        print()


# Test the function
print_pattern(5)
