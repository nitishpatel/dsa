from typing import List


def insertionSort(a: List[int], n: int) -> None:
    # write your code here
    for i in range(1, n):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

# Driver code to test above


arr = [64, 25, 12, 22, 11]

insertionSort(arr, len(arr))
print(arr)
