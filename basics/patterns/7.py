# Pattern - 7
#     *
#    ***
#   *****
#  *******
# *********
def pattern(num: int):
    '''
    Method to print the Pattern
    '''
    for i in range(num):
        for _ in range(num - i - 1):
            print(" ", end="")
        for _ in range(2 * i + 1):
            print("*", end="")
        print("")


if __name__ == "__main__":
    pattern(5)
