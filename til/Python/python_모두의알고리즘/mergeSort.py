def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr
    mid = n//2
    g1 = merge_sort(arr[:mid])
    g2 = merge_sort(arr[mid:])

    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result



def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return

    mid = n//2
    g1 = arr[:mid]
    g2 = arr[mid:]
    merge_sort(g1)
    merge_sort(g2)

    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            arr[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            arr[ia] = g2[i2]
            i2 += 1
            ia += 1
    while i1 < len(g1):
        arr[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        arr[ia] = g2[i2]
        i2 += 1
        ia += 1
        