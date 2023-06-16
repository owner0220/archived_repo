# API Project

### **파일 트리 구조**

```
**movie/**
​    ├─────images                            
​    │       └ *.jpg                            
​    │                                                       
​    ├─────    app.py                       
​    ├─────    01_boxoffice.py    
​    ├─────    02_movie.py  
​    ├─────    03_movie_naver.py    
​    ├─────    04_images_down.py    
​    ├─────    boxoffice.csv
​    ├─────    movie.csv
​    ├─────    movie_naver.csv
​    └─────    README.md
```



### 폴더 및 파일 설명

**movie/**



**images/**    :   movie_naver.csv의 thumb_url 조회, jpg 파일이 저장된 폴더

- 영진위 영화 대표코드(movieCd.)jpg 형태 43개  ex) 20010291.jpg



**app.py**      : 

- #===을 구분으로 1번 : boxoffice.csv    2번 : movie.csv   3번 : movie_naver.csv  4번 : 이미지 저장
 
**01_boxoffice.py**      : 

- boxoffice.csv 생성
 
**02_movie.py**      : 

- movie.csv 생성
 
**03_movie_naver.py**      : 

- movie_naver.csv 생성
 
**04_images_down.py**      : 

- 이미지  생성



**boxoffice.csv**    : 

- 영화 대표코드, 영화명, 해당일 누적관객수, 조회일



**movie.csv**    :

- 영화 대표코드, 영화명 (국문), 영화명 (영문), 개봉연도, 상영시간,장르, 감독명, 관람등급, 배우1,배우2,배우3



**movie_naver.csv**    :

- 영진위 영화 대표코드, 영화 썸네일 이미지의 URL,  하이퍼텍스트 link, 유저 평점



**※ 주의!!! **
csv 파일들은 첫줄에 기본적으로 열에 해당하는 데이터를 표현하기 위해
미리 아래와 같은 내용으로 첫줄을 입력한 파일을 만들었기에
각 파일에 데이터를 지우고 다시 테스트할때는 아래와 같은 내용의 첫줄을 선입력 해줘야 한다.


**boxoffice.csv**
movie_code,title,audience,recorded_at

**movie.csv**
movie_code,movie_name_ko,movie_name_en,movie_name_og,prdt_year,genres,directors,watch_grade_nm,actor1,actor2,actor3

**movie_naver.csv**
movie_code,thumb_url,link_url,user_rating