import sys
sys.stdin = open("sample_input (1).txt",'r')


arr = []
for num in range(1, 13):
    arr.append(num)

T = int(input())

for i in range(T):
    # 숫자 2개 첫째는 부분집합 갯수, 뒤에는 부분집합합
    case = list(map(int, input().split()))

    # 모든 경우의 수를 생각
    casecnt = 0
    for j in range(1 << 12):
        cnt = 0
        tempsum = 0
        for k in range(12):
            if j & (1 << k) != 0:
                cnt += 1
                tempsum += arr[k]
        if cnt == case[0] and tempsum == case[1]:
            casecnt += 1
    print("#{} {}".format(i + 1, casecnt))
