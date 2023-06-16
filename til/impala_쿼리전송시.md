### 대량의 쿼리문 전송시

1. 추천 방법
```
hive -f test.hql
```
test.hql 안에 쿼리문을 몰아 넣는다.
ex)
```
create table A (q string, qq string, ww int);
create table B (q string, qq string, ww int);
create table C (q string, qq string, ww int);
create table D (q string, qq string, ww int);
create table E (q string, qq string, ww int);
...
```

※ cli 환경에서 hive로 보내는 것이 아래처럼 여러줄 명령어를 실행하는 것보다 더 빠르다.
```
hive -f 1.hql
hive -f 2.hql
hive -f 3.hql
...
```
