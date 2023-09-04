import string


def print_14(N: int):
    for i in range(1, N + 1):
        # Print characters in descending order starting from 'E'
        for j in range(N, N - i, -1):
            print(chr(j + 64), end=" ")

        # Move to the next line
        print()


print_14(5)
