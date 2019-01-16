> python ver_3.7.2

# Built-in Functions_bin()

- 사용법 :

  ` bin(x)`

  인자값으로  int 형을 넣는다.

- 기능 :

  - 입력한 int 숫자를 이진법으로 변환해 0b를 앞에 붙여 문자형으로 리턴해준다.

- 리턴값 :

  문자형 (string)

```python
bin(2)				    # '0b10'
print(type(bin(3.0)))   # ERROR

#같은 결과를 이런 방법으로도 사용 가능하다.
print(format(2, '#b'))	# '0b10'
print(format(2, 'b'))	# '10'		
```

