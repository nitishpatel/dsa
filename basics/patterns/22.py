# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4
n = 4

for i in range(1, n+1):
    for j in range(1, n+1):
        print(max(i, j, n-i+1, n-j+1), end=' ')
    print()
