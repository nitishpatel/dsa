from typing import List


def bubbleSort(arr: List[int], n: int):

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Driver code to test above

arr = [64, 25, 12, 22, 11]
n = len(arr)

bubbleSort(arr, n)
print(arr)
