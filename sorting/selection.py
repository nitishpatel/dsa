from typing import List


def selectionSort(arr: List[int]) -> None:
    # Write your code here
    for i in range(0, len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Driver code to test above

arr = [64, 25, 12, 22, 11]
print(selectionSort(arr))
