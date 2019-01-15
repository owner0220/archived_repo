> python ver_3.7.2

# Built-in Functions_abs()

- 사용법 :

  ` abs(x)`

  괄호 안에 인자를 넣어서 사용한다.

- 기능 :

  - 절대값을 계산해 준다. (정수, 실수 모두 계산해 준다. 복소수는 그 크기를 계산해 준다.)

- 리턴값 :

  넣은 인자 타입 (단, 복소수는 크기를 계산했기에 float를 반환한다.)

```python
print(type(abs(3)))     # <class 'int'>
print(type(abs(3.0)))   # <class 'float'>
print(type(abs(2+3j)))  # <class 'float'>
```