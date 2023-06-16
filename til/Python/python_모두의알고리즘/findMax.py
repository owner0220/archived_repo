def find_max(arr):
    n = len(arr)
    max_v = arr[0]
    for i in range(1, n):
        if arr[i] > max_v:
            max_v = arr[i]
    return max_v


def find_max_idx(arr):
    n = len(arr)
    max_idx = 0
    for i in range(i,n):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

