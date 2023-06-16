def search_list(arr, x):
    n = len(arr)
    for i in range(0, n):
        if x == arr[i]:
            return i


    return -1