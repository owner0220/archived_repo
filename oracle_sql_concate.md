### 여러 칼럼을 하나의 칼럼으로 만들 때 유용한 방법
- 여러 칼럼의 예시
```
SELECT ID, NAME, PHONENUMBER, POSITION FROM A;
```
- 항목 간에 구분자 | 가 있고 하나의 칼럼으로 만드는 방법
```
SELECT ID || '|' || NAME || '|' || PHONENUMBER || '|' || POSITION FROM A;
```
※ 여기서 하나의 칼럼으로 묶이는 셀렉트 구문은 꼭 한줄로 이어 쓰여야 한다.
안되는 예시 1
```
SELECT
ID || '|' || NAME || '|' || PHONENUMBER || '|' || POSITION FROM A;
```
올바른 예시 
```
#방법 1
SELECT ID || '|' || NAME || '|' || PHONENUMBER || '|' || POSITION FROM A;

#방법 2
SELECT ID || '|' || NAME || '|' || PHONENUMBER || '|' || POSITION
FROM A;
```

### 발생할 수 있는 에러로그
```
ORA-00923 : FROM 키워드가 있어야 할 곳에 없습니다.
```
- 하나의 칼럼에 하나의 Alias를 쓸수 있다. 여러 칼럼을 하나의 칼럼으로 만들기 때문에 SELECT 문에 있는 AS를 모두 제거하거나 하나만 남겨야 한다.
