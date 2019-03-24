def find_min_idx(arr):
    n = len(arr)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(arr):
    result = []
    while arr:
        min_idx = find_min_idx(arr)
        value = arr.pop(min_idx)
        result.append(value)
    return result

def selSort(arr):
    n = len(arr)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]