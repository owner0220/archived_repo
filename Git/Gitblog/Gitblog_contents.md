
### 블로그 포스팅하기
  - GitHub에 생성한 블로그는 Jekyll 테마에 의해 포스트 등이 자동 반영되어 나타납니다.
    ※ 단, md 파일로 만들어야 한다는 점과 경로, 파일명이 규칙에 맞게 되어 있어야 하는 점에 주의해야 합니다.
  - 1. 오른쪽 상단 about us을 만들어 gitpitch 슬라이드 URL 연결
      - _data폴더를 생성해 navigation.yml 파일을 생성해 아래와 같이 작성 합니다.
        ```
        main:
          - title: about us
            url : https://gitpitch.com/깃헙아이디/깃헙레포지토리
        ```
  - 2. 포스팅하기
        - _posts폴더를 생성 yyyy-mm-dd-제목.md 형식으로 포스팅 합니다.
        - 파일 내용은 아래와 같은 예시
        ```
        ---
        title: 자기 주도 학습
        ---
        
        # 주제 1
        
        연습
        
        * 주제 2
        
        연습 2
        ```
