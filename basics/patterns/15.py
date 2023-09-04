# Input: 5

# Output:
# ABCDE
# ABCD
# ABC
# AB
# A
import string


def print_14(N: int):
    alphabets = list(string.ascii_uppercase)
    for i in range(N, 0, -1):
        for j in range(0, i):
            print(alphabets[j], end=" ")
        print()


print_14(5)
