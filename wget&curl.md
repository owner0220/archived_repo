### wget VS curl 어떤게 더 나을까?
- 기본적으로 wget과 curl은 cli 유틸프로그램으로 하는 일이 같다.


### 결론적으로는
- 다운로드만 빨리 하고 싶다면 wget을 써라
- wget이 지원하지 않는 프로토콜이나 다른것과 상호작용을 하고 싶다면 curl을 쓰면 된다.


공통점
- FTP, HTTP(s)를 사용해서 파일을 다운로드 받을 수 있다.
- HTTP POST request를 할 수 있다.


개별적인 특징
curl
- curl은 프로그래머가 사용할 수 있는 API를 코드로 가지고 있고 cross-platform library인 libcurl을 사용한다.
- curl은 더 많은 프로토콜을 지원한다. 예를 들면 DICT, FILE, FTP, FTPS, Gopher, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMTP, SMTPS, Telnet, TFTP. 들을 지원한다.
- 재귀적 다운로드 미지원.
- 리눅스 기본 툴


```
# 단일 파일 다운로드
curl http://www.centos.org
```
```
# -o는 다운로드한 파일이름을 지정한 이름으로 다운로드 / -O는 URL의 파일 이름으로 저장
curl -o mygettext.html http://www.gnu.org/software/gettext/manual/gettext.html
```
```
# 한번에 여러 파일 다운로드 (같은 사이트에서 여러 파일 다운시 연결을 재활용하려고 시도한다.)
curl -O URL1 -O URL2
curl -O http://www.gnu.org/software/gettext/manual/html_node/index.html -O http://www.gnu.org/software/gettext/manual/gettext.html
```
```
# HTTP 위치 헤더 기반으로 수행된다.(리디렉션된 곳을 쫓아 다운로드)
curl -L http://www.google.com
```
```
# 중단된 다운로드 계속하기 (대용량 다운시 유용하다.)
curl -C - -O http://www.gnu.org/software/gettext/manual/gettext.html
```
```
# 데이터 전송 평균적 속도 제한
curl --limit-rate 1000B -O http://www.gnu.org/software/gettext/manual/gettext.html
```
```
# 특정 시간대 이후 수정된 파일 다운로드 (FTP, HTTP 모두 가능하다.) ※날짜표현식 궁금하면 curl_getdate 검색
지정된 날짜보다 늦게 수정된 경우에 다운로드 하는 방법
curl -z 21-Dec-11 http://www.example.com/yy.html
지정된 날짜보다 이전에 수정된 경우 다운로드
curl -z -21-Dec-11 http://www.example.com/yy.html
```
```
# curl에서 HTTP 인증 전달
curl -u username : 암호 URL
```
```
# FTP 서버에서 파일 다운로드
curl -u ftpuser : ftppass -O ftp : //ftp_server/public_html/xss.php
```
```
# 주어진 url 및 모든 파일, 디렉토리 다운
curl -u ftpuser : ftppass -O ftp : // ftp_server / public_html /
```
```
# 범위내 목록 다운로드
curl ftp://ftp.uk.debian.org/debian/pool/main/[az]/
```
```
# FTP서버에 파일 업로드 (범위로 여러 파일을 동시 업로드 가능하다.)
curl -u ftpuser : ftppass -T myfile.txt ftp://ftp.testserver.com
```
```
# Optionally we can use “.” to get the input from STDIN and transfer to the remote.
curl -u ftpuser : ftppass -T "{file1, file2}"ftp://ftp.testserver.com
```
```
# 표준입력에서 사용자 입력을 가져와서 myfile_1.txt 이름으로 FTP서버에 내용을 저장한다.
curl -u ftpuser : ftppass -T - ftp://ftp.testserver.com/myfile_1.txt
```
```
# Verbose 및 Trace Option을 사용한 추가 정보가 보인다. / 컬 실패 로그 확인에 사용
curl -v http://google.co.in
```
```
# DICT 사용 단어 정의 가져오기 (사전 서버 URL 필요하다.)
curl dict : //dict.org/d : bash
```
```
# 사용가능 모든 사전 나열
curl dict : //dict.org/show : db 
```
```
# 컴퓨터에서 bash 의미 검색
curl dict : //dict.org/d : bash : foldoc
```
```
# 프록시 사용 파일 다운로드 (프록시의 호스트와 포트를 지정해야 한다.)
curl -x proxysever.test.com:3128 http://google.co.in
```
```
# SMTP 사용 메일보내기 (보낸사람주소, 받는사람주소 및 메일 서버 IP 주소 지정) .이 나오기 전까지 메시지가 기록하고 . 이후에 메일을 보낸다.
curl --mail - blah@test.com --mail-rcpt foo@test.com smtp : //mailserver.com
제목 : 테스트
테스트 메일 입니다
.
```








wget
- wget은 API 없이 단순 cli 툴이다.
- wget은 따로 설치해야한다.
- 대용량 파일 다운로드, 재귀 다운로드, 비대화형 다운로드, 여러 파일 다운로드 등 복잡한 다운로드 상황을 모두 처리할 수 있다.

```
# wget을 사용해 단일 파일 다운로드하고 현재 디렉토리에 저장 & 다운로드 하는 동안 진행 표시 줄 표시
wget http://www.openss7.org/repos/tarballs/strx25-0.9.2.1.tar.bz2
```
```
# 파일을 다른이름으로 다운로드하고 저장
wget -O taglist.zip http://www.vim.org/scripts/download_script.php?src_id=7701
```
```
# 다운로드 속도 지정
wget --limit-rate = 200k http://www.openss7.org/repos/tarballs/strx25-0.9.2.1.tar.bz2
```
```
# 불완전 다운로드 계속(중간에 중지된 다운로드 다시 시작) ※-c 없으면 같은 파일 이름이 있을때 파일이름에 .1을 자동추가 다운로드 한다.
 wget -c http://www.openss7.org/repos/tarballs/strx25-0.9.2.1.tar.bz2
```
```
# 백그라운드 다운로드 (wget-log에 출력이 기록된다.) / tail -f wget-log 를 통해서 상태 확인이 가능하다.
 wget -b http://www.openss7.org/repos/tarballs/strx25-0.9.2.1.tar.bz2
```
```
# 사용자 에이전트를 숨겨서 wget 사용 다운로드를 브라우저 처럼 표시해 다운로드
wget --user-agent = "Mozilla / 5.0 (X11; Ui; Linux i686; en-US; rv : 1.9.0.3) Gecko / 2008092416 Firefox / 3.0.3"URL-TO-DOWNLOAD
```
```
# 파일다운로드 전 파일 다운로드 가능여부, 페이지 유무 확인 가능한 방법
wget --spider DOWNLOAD-URL
```
```
# 인터넷 연결이 불안전하거나 파일 크기가 크면 다운로드 실패 가능성이 있기때문에 다운로드 수행 횟수를 20회로 지정
wget --tries = 20 DOWNLOAD-URL
```
```
# 전체 웹 사이트 다운로드, 로컬로 볼 수 있도록 하고 싶을때 실행한다.
wget --mirror -p --convert-links -P ./LOCAL-DIR WEBSITE-URL
```
```
# 특정 파일 유형만 다운로드 안받기
wget --reject = gif WEBSITE-TO-BE-DOWNLOADED
```
```
# 에러를 로그로 남기고 싶을때
wget -o download.log DOWNLOAD-URL
```
```
# 특정 크기를 초과하면 다운로드 종료한다. 단, 재귀적 다운로드 시에만 가능하다.
wget -Q5m -i FILE-WHICH-HAS-URLS
```
```
# 특정 파일 유형만 다운로드
wget -r -A.pdf http : // url-to-webpage-with-pdfs /
```
```
# FTP 다운로드 방법
wget ftp-url
```
```
# 인증이 필요한 FTP 다운로드 방법
wget --ftp-user = USERNAME - ftp-password = 패스워드 DOWNLOAD-URL
```

# 여러 파일 다운로드
먼저 다운로드할 URL을 행별로 텍스트에 저장한다.
downloadlist.txt
```
URL1
URL2
URL3
URL4
```
명령 입력
```
wget -i downloadlist.txt
```


