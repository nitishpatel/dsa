# Input: 5

# Output:
# 1                 1
# 1 2             2 1
# 1 2 3         3 2 1
# 1 2 3 4     4 3 2 1
# 1 2 3 4 5 5 4 3 2 1

# Path: basics/patterns/13.py

def print_pattern(num):
    for i in range(1, num + 1):
        # Print numbers in ascending order
        for j in range(1, i + 1):
            print(j, end=" ")

        # Add spaces
        for j in range(2 * (num - i)):
            print(" ", end=" ")

        # Print numbers in descending order
        for j in range(i, 0, -1):
            print(j, end=" ")

        print()


print_pattern(5)
