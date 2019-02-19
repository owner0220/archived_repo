import sys

with open("input.txt","r") as read:
    sys.stdin = read

    for tc in range(1,11):
        view = 0
        N = int(input())
        h = list(map(int,input().split()))
        for i in range(2,N-2):
            # t = max(h[i-2],h[i-1],h[i+1],h[i+2])
            left = h[i-2] if h[i-2]>h[i-1] else h[i-1]
            right = h[i+1] if h[i+1]>h[i+2] else h[i+2]
            t = left if left>right else right
            if(h[i]>t):
                view+=h[i]-t
        print(f"#{tc} {view}")