### wget 사용

1. 사용법
네트워크 상에서 데이터를 다운로드 받는다. 유저와의 상호작용이 필요 없으므로 - non interactive - 자동화된 다운로더 시스템을 구성할 수 있다.

2. 설명
GNU wget은 상호작용을 필요로 하지 않는 다운로드 프로그램으로 Web(:12)으로 부터 파일들을 가져올 수 있다. HTTP, HTTPS, FTP 프로토콜을 지원하며, HTTP proxy에서 데이터를 가져올 수도 있다.
wget이 상호작용을 필요로 하지 않는다는 것은, 백그라운드 상태에서 작동할 수 있음을 의미한다. 사용자는 로그인(:12)을 하지 않은 상태에서도 cron이나 Damon을 이용 wget을 실행시킬 수 있다. 또한 cookie, Form action을 지원해서 사용자 액션을 시뮬레이션 할 수도 있다.
wget은 HTML과 XHTML 페이지를 다운로드 받아서 로컬 파일시스템에 저장한다. 이때 파일이름과 디렉토리 구조까지를 그대로 로컬시스템에 구축함으로써, backup, mirror 사이트 구축등에 사용할 수도 있다. 또한 recursive 다운로드를 지원해서, 사이트 전체를 쉽게 내려받을 수 있다.
wget은 느리거나 불안정한 네트워크 환경에서도 매우 잘 작동하는 견고한 프로그램이다. 네트워크 환경이 불안해서 도중에 연결이 끊겼다면, 연결이 끊긴 시점부터 다운로드 받는 기능도 가지고 있다.

3. 옵션
3.1. Start Up
-V, --version : wget의 버전을 보여주고 종료한다.
-h, --help : 도움말을 보여준다.
-b, --background : 백그라운드에서 작동하도록 한다.
-e, --execute=COMMAND : wgetrc를 읽어서 명령을 실행한다.

3.2. Logging and input file
-o, --output-file=FILE : 메시지들을 파일로 남긴다.
-a, --append-output=FILE : 메시지들을 파일에 추가한다
-d, --debug : 디버그 내용을 출력한다.
-q, --quiet : 메시지들을 표준출력(:12)하지 않는다.
-nv, --non-verbose : 기본옵션을 제거한다.
-i, --input-file=FILE : 다운로드 받을 URL(:12)주소를 파일에서 찾는다.
-F, --force-html : HTML과 같은 파일을 입력값으로 취급한다.
-B, base=URL, sslcertfile=FILE, --sslcertkey=KEYFILE : 파일이나 링크들의 SSL(:12)인증을 위해서 URL, keyfile을 사용한다.

3.3. 다운로드
--bind-address=ADDRESS : 로컬 호스트의 주소를 설정한다.
-t, --tries=NUMBER : 설정한 숫자 만큼 다시 시도한다. 0은 무한대
-O, --output-document=FILE : 문서를 파일로 쓴다.
-c, --continue : 연결이 끊긴 시점부터, 이어서 파일을 다운로드 받는다.
-N, --timestamping : 로컬에 있는 것보다, 새롭지 않으면 파일을 다시 받지 않는다.
-S, --server-response : 서버의 응답을 출력한다.
--spider : 다운로드 하지 않는다.
-T, timeout=SECONDS : 종료된 시간을 초단위로 설정한다.
-w, --wait=SECONDS : 연결을 위해 기다리는 시간을 초단위로 설정한다.
-Y, --proxy=on/off : 프락시 모드를 켜고 끈다.
-Q, --quota=NUMBER : 숫자만큼 분담하도록 설정한다.

3.4. 디렉토리 관리
-nd, --no-directories : 디렉토리를 생성하지 않는다.
-x, --force-directories : 디렉토리를 강제로 생성한다.
-nH, --no-host-directories : 호스트 이름의 디렉토리를 생성하지 않는다.
-P, --directory-prefix=PREFIX : 파일들이 저장될 디렉토리를 지정한다.

3.5. HTTP 옵션
--http-user=USER : http 유저 아이디를 설정한다.
--http-passwd=PASS : http 패스워드 암호를 설정한다.
-C, --cache=on/off : 서버측의 캐쉬 데이터를 허용하는게 보통이나, 제거할 수도 있다.
-E, --html-extension : 모든 text/html 형식의 문서들과 .html 파일을 같이 확장해서 저장한다.
-s, --save-headers : 파일에 HTTP헤더를 저장한다.
-U, --user-agent=AGENT : Wget이 아닌, 다른 브라우저로 AGENT를 설정한다.
--no-http-keep-alive : HTTP의 keep-alive를 제거한다.
--cookies=off : cookie를 사용하지 않는다.
--load-cookies=FILE : 쿠키의 값을 파일에서 읽어들인다.
--save-cookies=FILE : 세션이 끝난 이후 전달받은 cookie값을 저장한다.

3.6. FTP 옵션
-nr, --dont-remove-listing : .listing 파일에 있는건 지우지 않는다.
-g, --glob=on/off : 하나의 파일이름으로 할지를 결정한다.
--passive-ftp : passive 모드로 전송한다.
--retr-symlinks : 복구중에 링크가 걸린 파일을 가져온다.

3.7. Recursive retrieval
-r, --recursive : 웹데이터를 재귀적으로 가져온다. 대상 웹서버에 무리를 줄 수 있으니, 주의해서 사용해야 한다.
-l, --level=NUMBER
--delete-after : 다운로드 받은후 로컬파일을 삭제한다.
-k, convert-links : 관계없는 링크를 관련있는 링크로 변환한다.
-K, --backup-converted : 변환하기 전에, 원본파일을 .orig 파일로 백업한다.
-m, --mirror : -r -N -l inf -nr 옵션과 사용할 수 있다.
-p, --page-requisites : 모든 이미지와 HTML 페이지등을 가져온다.

3.8. Recursive accept/reject
-A, --accept=LIST : 받아들일 것을 확장하기 위해서 콤마로 분리된 리스트로 받아들인다.
-R, --reject=LIST : 받아들이지 않을 것을 콤마로 분리된 리스트로 받아들인다.
-D, --domains=LIST : 받아들일 도메인을 콤마로 분리된 리스트로 받아들인다.
--exclude-domains=LIST : 거절할 도메인을 콤마로 분리된 리스트로 받아들인다
--follow-ftp : HTML 문서에서의 FTP 링크를 따라간다
--follow-tags=LIST : HTML태그에서 따라갈 콤마로 분리된 리스트로 받아들인다.
-G, --ignor-tags : 무시할 HTML 태그를 콤마로 분리된 리스트로 받아들인다.
-H, --span-hosts : 반복할때에 다른 호스트로도 가게 한다.
-L, --relative : 관계있는 링크만 따라간다.
-l, --include-directories=LIST : 허용할 디렉토리를 리스트로 받아들인다.
-nh, --no-host-lookup : DNS의 검색 호스트를 사용하지 않는다.
-np, --no-parent : 상위 디렉토리를 올라가지 않도록 한다.

4. 예제
HTTPS 서버의 문서 가져오기 : 때때로 쿠키 값을 요구하는 경우가 있는데, 이때는 --load-cookie로 쿠키 파일을 가져올 수 있다. 이 쿠키파일은 mozilla 브라우저의 쿠키파일이다. HTTPS(:12) 서버의 상당수가 self-signed 인증서를 가지고 있는데, 이 경우 증명된 인증서가 아니라고 해서 문서를 읽어오지 않는다. 이럴때는 --no-check-certificate 옵션을 주면 된다.

### wget 대량 파일 다운로드 
```
wget -a download.log -c --tries=0 --no-cache --no-cookies --retry-connrefuesed --timeout=2 --wait=1 -r --no-passive-ftp --ftp-user="safww@www.com" --ftp-password=qwert ftp:<다운받을 주소> -O <저장할 위치와 이름>
```

다운받을 때 스트림을 저장하는 버퍼가 제때 클리어링 되지 않으면 프로세스가 무한 대기에 빠질수 있다는 이야기를 듣고
no cache, no cookies 옵션을 주었다.
 
검색키워드 : 
what can be possible with wget buffer size
wget clean buffer
wget download in chunks   (검색을 하니 용량이 큰 파일들 다운로드 하는 방법이 나와서)
wget download in a bulk   (벌크 단위로 개수가 많은 것을 찾아봄)
wget 대량 다운로드
