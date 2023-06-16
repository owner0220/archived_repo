

# 03_DB_PROJECT

### 파일구조

```
03_db/
        README.md
        01_create_table.sql
        02_crud.sql
        03_select.sql
        04_expression.sql
        05_order.sql
        pjt.sqlite3
```

**03_db/**

**01_create_table.sql**

- movies Table 생성
  - SQL의 **CREATE TABLE ... VALUES** 활용
- header, mode 설정
  - SQL **header, mode** 옵션
- 전체 데이터 출력
  - SQL의 **SELECT ... FROM** 활용



**02_crud.sql**

- Create ; 데이터 삽입
  - SQL의 **INSERT INTO ... VALUES** 활용
- Read ; 특정 영화코드 데이터 출력
  - SQL의 **SELECT ... FROM ... WHERE** 활용
- Update ; 특정 데이터의 특정 컬럼 값 수정
  - SQL의 **UPDATE ... SET ... WHERE** 활용
- Delete ; 특정 데이터 삭제
  - SQL의 **DELETE FROM ... WHERE ...** 활용



**03_select.sql**

- 원하는 데이터 찾기 
  - SQL의 **DISTINCT, WHERE, BETWEEN, AND** 활용



**04_expression.sql**

- SQL 안의 함수 활용 
  -  **SUM, AVG, MIN, MAX, COUNT**



**05_order.sql**

- 정렬하기 
  - **ORDER BY**
    - **ASC, DESC**
  - **LIMIT**



**pjt.sqlite3**

- 위의 SQL 파일들을 01부터 05까지 순서대로 실행한 결과를 저장한 데이터 파일