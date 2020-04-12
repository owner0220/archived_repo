# 황인식 포트폴리오

## Jekyll을 이용한 Github 블로그 [Code](https://github.com/owner0220/owner0220.github.io)

```html
개인프로젝트
프로젝트 기간 : 19.06 ~ 진행중
프로젝트 목표
 - Jekyll Theme을 이용하지 않고 만들어보자!
주요 기술
 - FrontEnd(HTML5,CSS,Bootstrap,scss), Jekyll, Markdown
```

#### LiveDemo : [바로가기](https://owner0220.github.io/)

> URL <https://owner0220.github.io/>





## 영화정보서비스(WATCHA) [Code](<https://github.com/owner0220/hodoo>)

```html
2인프로젝트
프로젝트 기간 : 19.05.06 ~ 19.05.17 (11일)
프로젝트 목표
 - Django Framework를 이용한 영화 정보 및 평가 관리, REST API 서버 제작
주요 기술
 - Restful API 서버 구축, 페이지별 권한설정, 상용서비스 연계(Kakao_플친)
 - 데이터 : Python, 웹크롤링, API 활용
 - DB : Django model 활용, SQL 조작
 - HTML5, CSS, BootStrap4, JavaScript
 - Git(SourceTree), GitHub
 - C9, Bash, AWS 배포
```

※ 페이지는 1920*1080 화면 비율에 최적화 되었습니다.(이외 해상도 지원 X)

#### Live Demo : [AWS서버](http://movielists-dev4.ap-northeast-2.elasticbeanstalk.com/)  \ [Heroku서버](<https://uphodoo.herokuapp.com/>)

> AWS url http://movielists-dev4.ap-northeast-2.elasticbeanstalk.com/  
>
> Heroku url https://uphodoo.herokuapp.com/

```html
테스트 계정   /    PW 
test        /   qqqq123!
```



## 학습_CodeShadowing

#### Bigdata [바로가기](<https://github.com/owner0220/bigdata>)

##### Bigdata_prj [바로가기](<https://github.com/owner0220/prj_bigdata>)





### Responsibe Web 설계 기록

#### 1. 만들려는 페이지 고민

페이지 설계 : onepage view

목적 : 잘 들어내고 잘 표현해 줄수 있는 페이지

내용 : 비전, 현재 능력, 준비중, 준비한 내용

- about
  - 간단한 현재 상황을 보여줄 수 있는 내용으로 구성
  - 프로젝트 경험, 학습 내용, 현재 관심있어서 하고 있는 것
  - git, stackoverflow, 연락책
- history (vision)
  - 개발과 관련지어진 나의 히스토리를 페이지네이션으로 연도별로 구현
    - 개괄 화면으로 major 한 내용들이 일생 곡선으로 표현
    - 연도를 클릭하면 해당하는 연도에 있었던 일들이 곡선으로 표현
- skill stack with prj
  - 프로젝트 내용 및 개발 내용 visual화
  - 그 프로젝트를 하면서 학습했던 내용 및 노력 결과 표현
- publish
  - 나의 학습 내용을 남들도 잘 알아 볼 수 있도록 재능 기부
  - wikidoc 스타일 + googleLab 학습 ui처럼 구성
- 학습내용 정리 (밟아온 my Road Map)
  - 



페이지 고민은 계속되고 예시들을 많이 볼 수록 더 좋은것들만 보여서

만들었던 페이지 구성이 계속 흔들려서 개발 기간이 길어졌다. SEO도 알아보고, 디자인 설계방법도 알아보고, 이전에 안다고 했던 부분들을 다시 찾아서 보고 있다. (MDN-CSS tutorial)

그니까 먼저 반응형 웹 개발을 확실히 알고 디자인을 잡고 가자!!



#### 2. 반응형

- breakpoint 설정
  - mobile vertical
  - mobile horizontal
  - tablet vertical
  - tablet horizontal
  - desktop
  - large

- 페이지 레이아웃 패턴 설정
  - Layout Shifter 형태
  - ![Layout Shifter](https://static.lukew.com/md-patterns3.png)

> https://www.lukew.com/ff/entry.asp?1514

- 레이아웃 설정 시 flexbox 선정 ( 다양한 웹엔진에서 기능 지원 )

> https://caniuse.com/#search=flexbox