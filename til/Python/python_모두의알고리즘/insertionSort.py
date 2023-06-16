def find_ins_idx(arr,v):
    for i in range(0, len(arr)):
        if v < arr[i]:
            return i

    return len(arr)

def ins_sort(arr):
    result = []
    while arr:
        value = arr.pop(0)
        ins_idx = find_ins_idx(result,value)
        result.insert(ins_idx, value)
    return result


def insSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key

d=[2,3,5,1,6]
insSort(d)
