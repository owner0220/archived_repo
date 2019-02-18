def binarysum(arr):
    for i in range(1,1<<len(arr)):
        arrlist=[]
        flag=0
        for j in range(len(arr)):
            if i & (1<<j) != 0:
                # s += arr[j]
                arrlist.append(arr[j])
                flag+=1
        if flag == 3:
            print(arrlist)
        # if s==0:
        #     return True
    return False

print(binarysum([1,2,3,-6]))