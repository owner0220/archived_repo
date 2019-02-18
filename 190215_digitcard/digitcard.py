import sys

sys.stdin = open("test.txt",'r')

T = int(input())

for _ in range(T):
    inputlength = int(input())
    digit = list(input())
    diction = dict()
    
    #뽑은 카드를 딕션으로 저장
    for item in digit:
        if item not in diction:
            diction[item]=1
        else:
            diction[item]+=1

    #많이 뽑힌 숫자를 먼저 가린다.
    maxtemp=digit[0]
    for item in set(digit):
        #큰 숫자를 찾는다.
        if diction[item] > diction[maxtemp]:
            maxtemp = item
        #같은 것들 중에 큰 숫자를 저장
        if diction[maxtemp]==diction[item] and int(item) > int(maxtemp):
            maxtemp = item

    print("#{}".format(_+1),maxtemp,diction[maxtemp])




