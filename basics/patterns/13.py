# Input: 5

# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

def print_13(num: int):
    start = 1
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(start, end=" ")
            start += 1
        print()


print_13(5)
