# Pattern - 4
# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def printTriangle(self, N):
    # Code here
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print("")
