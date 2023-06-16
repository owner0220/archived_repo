def quick_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    pivot = arr[-1]
    g1 = []
    g2 = []
    for i in range(0, n - 1):
        if arr[i] < pivot:
            g1.append(arr[i])
        else:
            g2.append(arr[i])

    return quick_sort(g1) + [pivot] + quick_sort(g2)


def quickSortSub(arr, start, end):
    if end - start <= 0:
        return
    pivot = arr[end]
    i = start
    for j in range(start, end):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[end] = arr[end], arr[i]

    quick_sort(arr,start,i-1)
    quick_sort(arr,i+1,end)

def quickSort(arr):
    quickSortSub(arr,0,len(arr)-1)
