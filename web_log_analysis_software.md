### Web log analysis software
- Web log analysis software(web log analyzer)는 웹 분석 소프트웨어로 서버 로그를 parse(분석)하여 언제, 어떻게, 누가 웹서버를 방문했는지 기록하고 데이터베이스에 저장해서 관리한다.

### Common indicators
- 총 방문 수, 총 방문객 수
- 방문 체류 시간, 마지막 방문
- 인증된 유저, 마지막 인증 방문
- 일주일동안 가장 많은 방문객 시간
- 방문객의 도메인 위치, 나라
- 호스트 리스트
- 총 페이지 뷰
- 많이 본 페이지, 리스트, 나간 페이지
- file types
- 접속자 OS
- 접속자 브라우저
- 접속자 로봇 확인
- HTTP referer
- 검색 엔진 키워드 분석
- HTTP errors
- Some of the log analyzers also report on who is on the site, conversion tracking, visit time and page navigation.

### HTTP referrer
- 일반적으로 리퍼러는 이 요청을 유도한 이전 항목의 URL
- JavaScript에서 document.referrer를 사용해 클라이언트 리퍼러 정보에 액세스 가능
- 예를 들어 사용자의 검색엔진 쿼리를 기반으로 웹페이지를 개별화 하는데 사용할 수 있다. (그러나, https와 함께 구글 검색을 사용할 때와 같이 리퍼러 필드에 항상 검색어가 포함되는 것은 아니다.

#### 리퍼러 숨기기
- 대부분의 웹서버는 모든 트래픽의 로그를 유지 관리하고 각 요청에 대해 웹 브라우저에서 보낸 HTTP 리퍼러를 기록해서 개인 정보 보호 문제가 제기되어 리퍼러 방지 시스템이 개발되었습니다.
- 참조 자 필드를 비우거나 부정확한 데이터로 대체해 작동

참조 : https://en.wikipedia.org/wiki/HTTP_referer

### Webalizer
- 웹 로그 분석 소프트웨어로 웹 서버 관리 도구 중 하나.
- 조회수, 방문수, 리퍼러, 방문 국가 및 다운로드 데이터 양 포함
- 통계를 그래픽으로 볼 수 있으며 날짜, 시간 또는 달과 같은 다른 시간 프레임으로 표시된다.
```
webalizer -p -F clf -n en.wikipedia.org -o reports logfiles/access_log
```
- 쉘 프롬프트에서 위와 같은 코드로 실행
- logfiles/access_log 로그 파일을 기반으로 분석
- -p 설정 incremental mode로 구동
- -F CLF 로그 포맷으로 분석
- -n en.wikipedia.org 도메인 네임(report links) 그리고 실행 하는 현재 폴더에 서브 폴더 생성
- -h 완료된 리스트를 보기 위한 옵션
