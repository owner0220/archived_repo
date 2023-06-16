### 블로그 만들기
  - GitHub는 Page 기능을 제공하는데, Jekyll과 같은 테마를 적용해 이를 블로그처럼 활용할 수 있습니다.
  - 덕분에 GitHub가 코드 관리뿐만 아니라 기술 블로그나 포트폴리오로 사용되는 경우도 적잖게 볼 수 있습니다.
    - [Theme] (https://github.com/topics/jekyll-theme)   (링크를 타고 마음에 드는 테마를 선택)
    - 테마마다 설정 방법이 조금씩 상이하므로 편의상 첫 번째 나오는 mmistakes / minimal-mistakes를 권장합니다.
    - 1. _config.yml 파일을 찾아 클릭합니다.
    - 2. [Raw] 버튼 또는 연필 아이콘을 클릭해서 문서의 내용을 복사합니다.
    - 3. 자신의 블로그 Repository로 돌아와 _config.yml 파일을 만들어 내용을 붙여 넣기 합니다.
    - 4. 내용 중 아래 것들로 수정해 줍니다.
        ```
        remote_theme             : "mmistakes/minimal-mistakes"
        title                    : "팀명"
        description              : "한 줄 소개"
        url                      : "https://사용자명.github.io" \# 예: https://ssafy2018.github.io"
        baseurl                  : "Repository명" \# "public"
        ```
    - 5. 블로그의 시작 페이지 역할을 할 index.html을 만들고 layout 값을 적어 저장합니다.
        ```
        ---
        layout: home
        ---
        ```
    - 6. Repository의 Settings 메뉴로 들어가 Github Pages 의 브랜치명을 선택 save를 통해 page를 활성화 합니다.</br>
           **Source**</br> 
             GitHub Pages is currently disabled. Select a source below to enable GitHub Pages for this repository</br>
    - 7. 잠시 기다리면 Settings에 해당 Page가 배포되었다는 메시지가 나타나고 웹 브라우저에서 해당 주소로 접속할 수 있습니다.
