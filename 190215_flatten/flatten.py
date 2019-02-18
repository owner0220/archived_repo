import sys

sys.stdin = open("text.txt",'r')


for _ in range(10):
    T = int(input())

    boxes = list(map(int,input().split()))

    maxidx=0
    minidx=0

    for i in range(T):
        for j in range(100):
            if boxes[maxidx] < boxes[j]:
                maxidx = j

            if boxes[minidx] > boxes[j]:
                minidx = j
        boxes[maxidx]-=1
        boxes[minidx]+=1


    for j in range(100):
        if boxes[maxidx] < boxes[j]:
            maxidx = j

        if boxes[minidx] > boxes[j]:
            minidx = j
    print(boxes[maxidx]-boxes[minidx])




