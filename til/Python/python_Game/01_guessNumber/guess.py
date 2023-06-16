import random

guessesTaken = 0

print("안녕 이름이 뭐야?")
myName = input()

number = random.randint(1, 20)
print("그래 ",myName,"나는 지금 1에서 20사이 숫자를 생각하고 있는데..")

while guessesTaken < 6:
    print("맞춰봐")
    guess = input()
    guess = int(guess)

    guessesTaken += 1

    if guess < number:
        print("Up!!")

    if guess > number:
        print("Down!!")

    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print("오~!!",myName,"! 내가 생각한 수를",guessesTaken,"번 만에 맞췄어!!")

if guess != number:
    number = str(number)
    print("내가 생각한 수는",number,"였어 다음번엔 꼭 맞춰 보시게나")
    


