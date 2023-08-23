# User function Template for python3

def print_diamond(num: int):
    '''
    Method to print diamond
    '''
    for i in range(num):
        for _ in range(num - i - 1):
            print(" ", end="")
        for _ in range(i + 1):
            print("*", end=" ")
        print("")

    for i in range(num):
        for _ in range(i):
            print(" ", end="")
        for _ in range(num - i):
            print("*", end=" ")
        print("")


if __name__ == "__main__":
    print_diamond(5)
