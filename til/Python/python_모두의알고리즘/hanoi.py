def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, "->", to_pos)
        return
    hanoi(n-1,from_pos,aux_pos,to_pos)
    print(from_pos,"->",to_pos)
    hanoi(n-1,aux_pos,to_pos,from_pos)


cnt = 0
def hanoi2(n,from_,aux_,to_):
    global cnt
    if n == 1:
        cnt += 1
        print(from_, "에서", to_ , "로 옮긴다.")
        return
    hanoi2(n-1,from_,to_,aux_)
    hanoi2(1,from_,aux_,to_)
    hanoi2(n-1,aux_,from_,to_)

hanoi2(3,1,2,3)
print(cnt)