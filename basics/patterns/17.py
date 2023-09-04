# Input: 4
# Output:
#    A
#   ABA
#  ABCBA
# ABCDCBA
import string


def print_17(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")

        # Print characters in ascending order
        for j in range(i):
            print(chr(65 + j), end="")

        # Print characters in descending order (excluding the first character)
        for j in range(i - 2, -1, -1):
            print(chr(65 + j), end="")

        # Move to the next line
        print()


print_17(4)
