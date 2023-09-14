
def merge(arr, low, mid, high):
    print(f"Currently merging: {arr[low:high+1]}")
    temp = []

    left = low
    right = mid+1

    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high+1):
        arr[i] = temp[i-low]


def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        print(f"Current array: {arr[low:high+1]}")
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)


arr = [6, 9, 3, 1, 5, 0, 12, -1, 8, 7, 4]
merge_sort(arr, 0, len(arr)-1)
print(arr)
