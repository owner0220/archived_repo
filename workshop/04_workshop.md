

# Python 1. 파이썬 기초

### Background

- String, List, Dictionary
- If
- for



### Goal

- Python programming 언어의 기본 문법이해
- 반복문에 대한 이해
- 조건문에 대한 이해



### Problem

1. 두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로
   의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.



**정답 :**

```python
#문제 정답
n = 5
m = 4
a = "*"*n
b = f"{a}\n"*m
print(b)
```



```python
#응용
garo=int(input("가로길이"))
sero=int(input("세로길이"))
print(("*"*garo+"\n")*sero)
```







2. 다음 딕셔너리에서 평균 점수를 출력하시오



**정답 :**

```pyhton
student = {'python':80, 'algorithm':78, 'django':95, 'flask':80}

a=0
for score in student.values():
    a=score+a
print(a/len(student))
```







3. 다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다. for문을 이용하여 각 혈액형
   별 학생수의 합계를 구하시오.



**정답 :**

```python

```

