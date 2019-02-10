> python ver_3.7.2

# Sequence Types 

### 시퀀스 유형 - list

- 사용법 :

  **list (** [*iterable*] **)**

- 기능 : 
  - iterable (list, tuple, dictionary, range, string)   ;   for 문으로 돌릴 수 있는것들
  - 마치 for 문으로 돌린듯 그 하나 하나 값들을 인자로 갖는 리스트를 만들어 준다.

- 리턴값 :

  리스트

ex)

`list('abc')` 은 `['a','b','c']` 로 반환

`list(  (1,2,3)  )`  은 `[1,2,3]`  로 반환





리스트가 자주 쓰는 기능

len(x) 리스트 길이(자료 개수)를 구합니다.

append(x) 자료 x를 리스트의 맨 뒤에 추가합니다.

insert(i,x) 리스트의 i번 위치에 x를 추가합니다.

pop(i) i번 위치에 있는 자료값을 리스트에서 삭제하고 그 값을 리턴해줍니다. i를 지정 하지 않으면 마지막 값을 빼내서 돌려줍니다.

clear() 리스트의 모든 자료를 지웁니다.  리스트 a의 모든 자료를 지울때는 a.clear()

x in a 어떤 자료 x가 리스트 a 안에 있는지 확인합니다.