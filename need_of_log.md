### 로그 파일의 필요성
- 언제 어디서 무엇이 오류로 발생했는지 빠른 조치를 취할 수 있기 때문에 로그는 중요하다.
- 로그도 표준화가 되어 있다는 사실!! 표준화된 결과를 이용해서 웹 분석프로그램들이 생길 수 있었다!
- Common Log Format(CLF)에서 로그파일을 생성한다면 Extended Log Format(ELF)는 더 자세한 정보와 유용성을 발휘한다.



### CLF(Common Log Format) 로그 예시
- NCSA Common log format(웹 서버 로그 텍스트파일 포맷)
- 여기서 Common Log Format 내용은 다음과 같다.
host         ident       authuser            date                     request         status bytes
```
127.0.0.1 user-identifier frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
```

- 127.0.0.1 는 서버에 요청을 시도하는 클라이언트 ip 주소
- user-identifier는 클라이언트의 RFC 1413 identity
- frank는 요청하는 사람 userid
- [10/Oct/2000:13:55:36 -0700]는  기본 타임 포맷(format %d/%b/%Y:%H:%M:%S %z)로 요청을 받은 시간
- "GET /apache_pb.gif HTTP/1.0" GET 방식으로 /apache_pb.gif 를  HTTP/1.0 프로토콜로 요청
- 200 은 HTTP status code 이다. (2xx 성공 / 3xx 리다이렉션 / 4xx 클라이언트 에러 / 5xx 서버에러)
- 2326은 요청을 한 클라이언트에게 돌아가는 size of object 이다.

참조
> https://en.wikipedia.org/wiki/Common_Log_Format#cite_note-2



### ELF(Extended Log Format) 로그 예시
```
#Version: 1.0
#Date: 12-Jan-1996 00:00:00
#Fields: time cs-method cs-uri
00:34:23 GET /foo/bar.html
12:21:16 GET /foo/bar.html
12:45:52 GET /foo/bar.html
12:57:34 GET /foo/bar.html
```

- Version은 ELF 포맷 양식 버전
- Date는 엔트리가 처음 추가된 날을 의미한다.
- Fields는 로그에 기록되는 상세 정보

---
- 예시에는 없지만
- software는 로그에 저장되는 소프트웨어 구분자
- Start-Date는 로그가 시작된 시간
- End-Date는 로그가 끝난 시간
- Remark 정보의 코멘트 / 이 코멘트는 분석 툴에서 무시 된다


### LM(Log Management)
- 대량으로 생성되는 로그들을 관리를 목적으로 한다.(프로그램일수도 사람일수도)
- Log collection
- Centralized log aggregation
- Long-term log strage and retention
- log rotation
- log analysis(in real-time and in bulk after storage)
- log search and reporting
실제로 운영할 땐 다음과 같은 문제들이 발생 할 수 있다.
1. 대규모 조직의 경우 하루에 수백기가바이트 이상의 로그 기록이 발생 할 수 있는데 데이터 수집, 중앙 집중화 저장에 문제
2. 로그는 여러 형식으로 생성되기 때문에 분석에 적합하게 정규화 해야 한다.
3. 속도 장치에서 로그를 생성하는 속도로 인해 수집 및 집계가 어려울 수 있다.
4. 로그 이벤트가 정확하지 않을 수 있다.
