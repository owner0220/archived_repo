# 06_Django Intro

```c
06_django / 
    django_06
    django_intro
    templates
    db.sqlite3
    manage.py
README.md
```

## 1. 영화 목록_URL : **/movies/**

- 데이터베이스에 존재하는 모든 영화 목록이 표시되며, 각 영화의 Title, Score 가 표시된다.
- Title 을 클릭 시, 해당 영화 정보 조회 페이지로 이동합니다.

## 2. 영화 정보 조회_URL : /movies/\<int:id>

- 동적으로 할당되는 부분으로 데이터베이스에 저장된 영화 정보의 Primary Key를 활용.
- 해당 Primary Key를 가진 영화의 모든 정보가 표시된다.
- 영화 정보의 최하단에는 목록, 수정, 삭제 링크가 있으며, 클릭 시 각각 영화 목록, 해당 영화 정보 수정 Form, 해당 정보 삭제 페이지로 이동합니다.

## 3. 영화 정보 삭제_URL : /movies/\<int:id>/delete

- 해당 페이지에 접근하는 URL은 동적으로 할당되는 부분이 존재합니다. 동적으로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다.
- 해당 Primary Key를 가진 영화 정보를 데이터베이스에서 삭제합니다.
- 영화 정보 목록 페이지로 Redirect 합니다.

### 사용한 라이브러리

- **django-bootstrap4**
  - 부트스트랩 폼 사용을 위한 설치

