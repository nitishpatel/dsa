import math


def checkprime(x: int) -> int:
    # Write your code here

    root = math.sqrt(x)
    arry = []
    for i in range(1, int(root)+1):
        if len(arry) > 2:
            print("BREAKING")
            break
        if x % i == 0:
            arry.append(i)
            if (x/i) != i:
                arry.append(x/i)
            arry.sort()

    print(arry)
    return 'YES' if len(arry) == 2 else 'NO'


print(checkprime(1973))
