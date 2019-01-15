> python ver_3.7.2

# Built-in Functions_all()

- 사용법 :

  ` all(iterable)`

  괄호 안에 for로 돌릴수 있는 iterable한 인자를 넣어서 사용한다.

- 기능 :

  - 인자 값이 모두 들어 있거나 아무것도 없으면 True, 한두개 없을 때 False

- 리턴값 :

  부울타입 (True / False)

- **내부 구현 코드**

```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

