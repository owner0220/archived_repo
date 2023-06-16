def binary_search(arr, x):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1