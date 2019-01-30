# Python활용 SQL

### Background

- SQL
- Django Model

### Goal 

- Django Modeling



### Problem

1. 자신의 반에 있는 사람들의 데이터를 저장하는 Student모델을 생성합니다.

    Student모델이 가져야 할 필드는 아래와 같습니다.



 name(이름) : CharField

email(이메일) : CharField

birthday(생년월일) : dateField

age(나이) : IntegerField





2. 모델 마이그레이션 작업을 거친 후 Admin페이지에서 주변 학생들의 이름을 세명 저장합니다.





3. 저장 후 Admin페이지에서 학생들의 목록을 보기 쉽게 만들기 위해서 \_\_str\_\_메소드를  오버라이드 하여 name 이 출력되게 만듭니다.