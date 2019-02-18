a=[1,2,3,4,5]
def binarysearch(arr,key):
    left = 0
    right = len(arr)-1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == key:
            return True
        if key > arr[middle]:
            left = middle + 1
            print("왼쪽",left)
        else:
            right = middle - 1
            print("오른쪽",right)
    return False

print(binarysearch(a,1))

