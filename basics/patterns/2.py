# Pattern - 2
# *
# * *
# * * *
# * * * *
# * * * * *
def pattern(num: int):
    '''
    Method to print the Pattern
    '''
    for i in range(1, num + 1):
        for _ in range(i):
            print("*", end=" ")
        print("")


if __name__ == "__main__":
    pattern(6)
