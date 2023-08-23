# Pattern - 5
# Output:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1


def pattern(num: int):
    '''
    Func to print the pattern
    '''
    # Code Here
    for i in range(num, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print("")


if __name__ == "__main__":
    pattern(5)
