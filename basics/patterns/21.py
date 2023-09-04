def print_pattern(N):
    for i in range(N):
        if i == 0 or i == N - 1:
            print("*" * N)
        else:
            print("*" + " " * (N - 2) + "*")


# Test the function
print_pattern(4)
