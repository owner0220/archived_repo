> python ver_3.7.2

# Built-in Functions_any()

- 사용법 :

  ` any(iterable)`

  괄호 안에 for로 돌릴수 있는 iterable한 인자를 넣어서 사용한다.

- 기능 :

  - 인자가 하나라도 값을 가지고 있으면 True 비어 있으면 False

- 리턴값 :

  부울타입 (True / False)

- **내부 구현 코드**

```python
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```

