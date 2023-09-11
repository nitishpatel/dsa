def highLowFreqElements(n, edges):
    array = [0] * (n + 1)

    for edge in edges:
        if 1 <= edge <= n:
            array[edge] += 1

    print(array)


x = 6
y = [1, 2, 3, 1, 1, 4]

print(highLowFreqElements(x, y))
