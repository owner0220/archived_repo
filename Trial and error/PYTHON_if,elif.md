#PYTHON_if,elif
아 화나....

#### 1번 코드
``` python
elif (cnt == 5 and bonus == 0):
    result="3등"

elif (cnt == 5 and bonus == 1):
    result="2등"
```
---

#### 2번코드
``` python
elif (cnt == 5):
    result="3등"

elif (cnt == 5 and bonus == 1):
    result="2등"
```

**1번 코드**로 해야 2등이 출력되네?
이건 뭐 스위치 구문도 아니고 if else 구분도 아니고
코딩 규칙을 간단하게 하려고 그런건가?


는 무식을.... 증명....했네...ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ

Doc 보기를 습관화하자

> **w3schools** - Python If ... Else 
> <https://www.w3schools.com/python/python_conditions.asp>

**if**
These conditions can be used in several ways, most commonly in "if statements" and loops.
An "if statement" is written by using the if keyword.

``` python
a = 33
b = 200
if b > a:
  print("b is greater than a")
```

**Elif**
The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

``` python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```
In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".


**Else**
The else keyword catches anything which isn't caught by the preceding conditions.

``` python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```
  
