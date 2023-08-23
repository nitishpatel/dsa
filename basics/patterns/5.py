# Pattern - 5
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *

def pattern(num: int):
    '''
    Func to print the pattern
    '''
    # Code Here
    for i in range(num, 0, -1):
        for _ in range(i, 0, -1):
            print("*", end=" ")
        print("")


if __name__ == "__main__":
    pattern(5)
