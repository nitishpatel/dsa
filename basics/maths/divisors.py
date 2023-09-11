import math


def sumOfAllDivisors(n: int) -> int:
    # Write your code here

    total = 0
    for x in range(1, n+1):
        root = math.sqrt(x)
        arry = []
        for i in range(1, int(root)+1):
            if x % i == 0:
                arry.append(i)
                if (x/i) != i:
                    arry.append(x/i)
            arry.sort()
        total += int(sum(arry))

    return total
