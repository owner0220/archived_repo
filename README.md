# Herit(Here + it) | Toy_project

- 영화에 관련된 스틸컷, 예고편, 패러디, 촬영장을 연결해주는 웹앱서비스

**프로젝트 기간** `19.04.30~19.04.30`

**Tech Stack**

- **언어 :** Python, HTML5, CSS, Sql
- **프레임웍 :** Django, Bootstrap
- **환경 :** C9, bash

---

---



#### 세부내용

##### Web Crawling & API | 웹크롤링, API 활용

###### 목표

-  Python 이해, 활용
- 웹크롤러 및 API 활용, 프로그래밍을 통해 데이터 수집 및 원하는 형태로 가공 및 DB 저장
- CRUD구현, REST API 서버 구축 , 반응형 웹 페이지 구현

###### 활용데이터

- 영화 진흥 위원회 오픈 API
- 네이버 영화 검색 API
- 해외 영화 정보 API (The movie DB)
- **사용 라이브러리**
  - 크롤링
    - requests, beautifulsoup4
  - REST API
    - djangorestframework, django-rest-swagger
  - 더미데이터 및 데이터 입력
    - Faker
    - django-seed
    - django-import-export
  - 모델링_확인
    - django-extentions
  - 간편로그인, 회원가입
    - django-allauth

###### 개발 환경

```python
c9
bash == 4.3.11
Python == 3.6.7
```