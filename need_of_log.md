### 로그 파일의 필요성
- 언제 어디서 무엇이 오류로 발생했는지 빠른 조치를 취할 수 있기 때문에 로그는 중요하다.
- 로그도 표준화가 되어 있다는 사실!! 표준화된 결과를 이용해서 웹 분석프로그램들이 생길 수 있었다!

### 로그 예시
- NCSA Common log format(웹 서버 로그 텍스트파일 포맷)
- 여기서 Common Log Format 내용은 다음과 같다.
host         ident       authuser            date                     request         status bytes
```
127.0.0.1 user-identifier frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
```

127.0.0.1 는 서버에 요청을 시도하는 클라이언트 ip 주소
user-identifier는 클라이언트의 RFC 1413 identity
frank는 요청하는 사람 userid
[10/Oct/2000:13:55:36 -0700]는  기본 타임 포맷(format %d/%b/%Y:%H:%M:%S %z)로 요청을 받은 시간
"GET /apache_pb.gif HTTP/1.0" GET 방식으로 /apache_pb.gif 를  HTTP/1.0 프로토콜로 요청
200 은 HTTP status code 이다. (2xx 성공 / 3xx 리다이렉션 / 4xx 클라이언트 에러 / 5xx 서버에러)
2326은 요청을 한 클라이언트에게 돌아가는 size of object 이다.

참조
> https://en.wikipedia.org/wiki/Common_Log_Format#cite_note-2
