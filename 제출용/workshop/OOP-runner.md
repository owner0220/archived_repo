# OOP

### Background

- 객체지향프로그래밍
- 클래스, 인스턴스

### Goal

- 클래스에 대한 이해



### Problem

- 다음과 같은 클래스  Runner 가 있다.

```python
class Runner:
    hp = 100
    distance = 41195
    minute = 0
    
    def run_per_10_minute(self):
        self.hp -= 7
        self.distance -= 3000
        self.minute += 10
        if self.hp <= 0:
            print("쓰러졌습니다.")
        if self.distance <= 0:
            print(f"도착! 걸린시간 : {self.minute}분")
    def walk_per_10_minute(self):
        self.hp += 3
        self.distance -= 1500
        self.minute += 10
        if self.distance <= 0:
            print(f"도착! 걸린시간 : {self.minute}분")
my_runner = Runner()
```

-  Runner클래스의 인스턴스인 my_runner를 이용해서 쓰러지지 않고 최종 목적지까지 가는 코드를 작성하세요.

**정답 :**

```python
while (my_runner.hp > 0 and my_runner.distance > 0):
    if 0 < my_runner.hp <=6:
        my_runner.walk_per_10_minute()
    my_runner.run_per_10_minute()
```



