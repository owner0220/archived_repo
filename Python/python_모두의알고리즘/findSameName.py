def find_same_name(arr):
    n = len(arr)
    result = set()
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                result.add(arr[i])
    return result


def find_same_name2(arr):
    name_dict = dict()
    for name in arr:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result

