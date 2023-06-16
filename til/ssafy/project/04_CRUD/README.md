# 04) CRUD

```python
04_crud/
 ...
 ...
 ...
 README.md
```



### Python Web Framework

- Django

- C9 개발



class  **Movie** 

| 필드명      | 자료형  | 설명               |
| ----------- | ------- | ------------------ |
| title       | String  | 영화명             |
| title_en    | String  | 영화명(영문)       |
| audience    | Integer | 누적 관객수        |
| open_date   | Date    | 개봉일             |
| genre       | String  | 장르               |
| watch_grade | String  | 관람등급           |
| score       | Float   | 평점               |
| poster_url  | Text    | 포스터 이미지  URL |
| description | Text    | 영화소개           |

### 추가

- 부트스트랩
- static
- 추가 모듈 사용
  - django-import-export   :   엑셀, csv, 등 파일을 쉽게 임포트 익스포트 하게 해주는 모듈
  - django-seed : 규정해 놓은 Model 컬럼 특성에 맞게 더미 데이터를 생성
  - pandas : 엑셀을 읽어들일때 사용



**excel2sqlite3.py**

```python

import sqlite3
import pandas as pd

#단, 테이블이 존재 하지 않아야 데이터가 들어간다.
conn = sqlite3.connect("db.sqlite3")
dfs = pd.read_excel('data.xlsx', sheet_name=None)
for table, df in dfs.items():
    df.to_sql("insert_data", conn)

#주의 테이블의 타입중 datefield는 2018-01-01 00:00:00 형식으로 들어가기 때문에 슬라이싱해줘야 한다. 
cur = conn.cursor()
cur.execute("select * from insert_data")
rows = cur.fetchall()
for row in rows:
    cur.execute("insert into watchlist_movie (title,title_en,audience,open_date,genre,watch_grade,score,poster_url,description) values(?,?,?,?,?,?,?,?,?);",(row[1],row[2],row[3],row[4][0:11:1],row[5],row[6],row[7],row[8],row[9]))
    # cur.executemany("insert into 시트1 values()",row)
    print(row[4][0:11:1])
conn.commit()
conn.close()

```







#### 영화 TOP 3 list

##### 접근 URL :

- "/"



#### 영화 목록

접근 URL :

- /movies/



#### 영화 정보 생성 Form

접근 URL :

- /movies/new/



#### 영화 정보 생성

접근 URL :

- /movies/create/



#### 영화 정보 조회

접근 URL : 

- /movies/숫자/



#### 영화 정보 수정 Form

접근 URL : 

- /movies/숫자/edit/



#### 영화 정보 수정 

접근 URL : 

- /movies/숫자/update/



#### 영화 정보 삭제

접근 URL : 

- /movies/숫자/delete/