# Django Web Framework

### 학습해야 할 내용

- SQLite RDBMS



### 아래 동작을 수행하기 위한 SQL 을 각각 작성하세요

1. 

**정답 :**

```sqlite
CREATE TABLE friends (
id INTEGER,
name TEXT,
location TEXT
);
```



2. 

**정답 :**

```sqlite
INSERT INTO friends VALUES(1, "Justin", "Seoul");
INSERT INTO friends VALUES(2, "Simon", "New York");
INSERT INTO friends VALUES(3, "Chang", "Las Vegas");
INSERT INTO friends VALUES(4, "John", "Sydney");
```



3. 

**정답 :**

```sqlite
ALTER TABLE friends ADD (married INTEGER);
```



4.

**정답 :**

```sqlite
INSERT INTO friends VALUES(1,"Justin","LA",1);
INSERT INTO friends VALUES(2,"Simon","New York",0);
INSERT INTO friends VALUES(3,"Chang","LasVegas",0);
INSERT INTO friends VALUES(4,"John","Sydney",1);
```



5.

**정답 :**

```sqlite
DELETE FROM friends WHERE married = 0;
```

