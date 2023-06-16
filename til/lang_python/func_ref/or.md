> python ver_3.7.2

# Boolean Operations

### 부울 연산자 - or

- 사용법 :

  ` x or y`

  두 인자 사이에 넣어서 사용한다.

- 기능 :

  - 만약  x가 False 이면, y를 리턴 

    이외 경우에는 x를 리턴

- 리턴값 :

  리턴되는 인자형태

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