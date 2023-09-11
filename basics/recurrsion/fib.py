def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Test the function
n = 4  # Change this to the desired value of n
result = fibonacci(n)
