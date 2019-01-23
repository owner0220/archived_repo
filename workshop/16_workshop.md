# Django Web Framework

### Background

- SQL 
- DB

### Goal

- 테이블의 수정 
-  데이터의 Update, Destroy



 저번 워크샵에서 아래 표와 같은 DB를 제작한 상태다.



1. 해당 테이블을 수정하여, 다음과 같이 컬럼을 추가하고, 데이터를 삽입하라.

**정답 :** 

```sqlite
ALTER TABLE bands ADD members INTEGER;
```



2. Id 가 3인 레코드의 members 를 5로 수정하라.

**정답 :**  

```sqlite
UPDATE bands SET members=5 WHERE Id=3;
```



3. Id 가 2인 레코드를 삭제하라

**정답 :**

```sqlite
DELETE FROM bands WHERE Id=2;
```

