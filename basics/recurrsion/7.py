def reverseArray(arr, start, end):
    if start >= end:
        return arr

    arr[start], arr[end] = arr[end], arr[start]
    return reverseArray(arr, start + 1, end - 1)


print(reverseArray([1, 2, 3, 4, 5], 0, 4))
