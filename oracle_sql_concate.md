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
