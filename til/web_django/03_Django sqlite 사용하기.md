>PYTHON ver 3.6.7
>
>Linux / bash 창 /  c9.io 환경
>
>01,02 md 설명을 통해 기본 서버 세팅이 끝났다는 가정하게 진행

[TOC]



# Django SQLite3

### 1. Django에서 만든 Django Project

#### SQL 테이블 만들기

##### 1) models.py

```python
from django.db import models

# Create your models here.
class stclass(models.Model): 
    name = models.CharField(max_length=100)
    school = models.TextField()
    age = models.IntegerField()
    due_date = models.DateField()
    # def __str__(self):
    #     return self.title
```





### 2. Migration

- Models.py 에서 만든 SQL 테이블을 Python 코드로 실행 할 수 있도록 구조를 짜는 과정

  (python -> SQL ->python)

  - ###### bash 창에서 아래 명령을 입력

    ```bash
    python manage.py makemigrations
    ```

    - migrations 폴더 안에 번역파일인 ~~.py 파일이 생긴다.



### 3. Migrate

- Migration 으로 구조가 짜여 지면 실제로 sqlite3 에 반영하는 과정 (SQL 실행)

  - ###### bash 창에서 아래 명령을 입력

    ```bash
    python manage.py migrate
    ```
    - db.sqlite3 에 테이블 스키마가 입력된다.



---



### 4. DB 등록하기

#### App에 사용 DB 등록하기
- Django에서 만든 Django Project 안

##### 1) admin.py

```python
from django.contrib import admin
from .models import stclass
# Register your models here.
admin.site.register(stclass)
```



---

project 폴더 안의 manage.py 실행 할수 있는 폴더 레벨에서 아래 실행



### 5.  Admin 계정 만들기

#### 계정 등록하기

- ###### bash 창에 아래 명령을 입력

```bash
python manage.py createsuperuser
```

※ 이후에 나오는 아이디, 이메일, 비밀번호를 입력하면 등록 완료 된다.