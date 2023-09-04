# Input: 5

# Output:
# A
# AB
# ABC
# ABCD
# ABCDE
import string


def print_14(N: int):
    alphabets = list(string.ascii_uppercase)
    for i in range(0, N):
        for j in range(0, i+1):
            print(alphabets[i], end=" ")
        print()


print_14(5)
