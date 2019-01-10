> python ver_3.7.2

# Boolean Operations

### 부울 연산자 - or

### ` x or y`

- 과정 : 

  if x is false, then y, else x

  만약  x가 False 이면, y를

  이외 경우에는 x를 return

- 기능 :

  논리 판단

- 리턴 :

  둘 중 먼저 True 인 인자를 그대로 리턴

```python
print(2 or 3)   # 2를 출력한다.
print("" or 3)  # 3을 출력한다.
print(0 or 3)   # 3을 출력한다.
print(None or 3)# 3을 출력한다.
```



### 개념으로 기억할 것

#### 있으면 True / 없으면 False

※ 문자가 있으면 True / 없으면 False     (띄어 쓰기도 문자이기 때문에 True)

※ 숫자가 있으면 True / 0이면 False       (음수도 숫자가 있는것 이기에 True)

※  None 은  없는 것을 말하니까 False