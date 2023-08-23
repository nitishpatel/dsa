# Pattern - 1
#   * * * *
#   * * * *
#   * * * *
#   * * * *
def main(num: int):
    '''
    Method to print the Pattern
    '''
    for _ in range(0, num):
        for _ in range(0, num):
            print("*", end=" ")
        print("")


if __name__ == "__main__":
    main(4)
