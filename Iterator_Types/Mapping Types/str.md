> python ver_3.7.2

# Mapping Types

### 매핑 타입 - dict

- 사용법 :

  class **dict** (**kwarg)

  class **dict** (mappnig, **kwarg)

  class **dict** (iterable, **kwarg)

  

- 기능 :

  - 아무것도 없을때는 빈 딕셔너리를 리턴한다.
  - key, value로 구분되어 기록된다.
  - 같은 key값으로 다른 value 값이 입력된다면 마지막에 입력된 value 값으로 저장된다.

- 리턴 :

  딕셔너리

```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e
True
```