# User function Template for python3
# Ouput Expected Pattern:
# Output:
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
def print_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if (i + j) % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()


if __name__ == "__main__":
    print_triangle(5)
