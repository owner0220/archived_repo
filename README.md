미니멀 파이썬 HTTP 서버 입니다.
GET 요청시 Hello World JSON 을 보내주며
POST 요청시에는 요청한 JSON 형태로 다시 echo response를 내어 줍니다.

```
python server.py 8009
Starting httpd on port 8009...
```

```
curl http://localhost:8009
{"received": "ok", "hello": "world"}
```

```
curl --data "{\"this\":\"is a test\"}" --header "Content-Type: application/json" http://localhost:8009
{"this": "is a test", "received": "ok"}
```

단, 배포시 스레딩 지원이 안되며 연결이 1개만 지원 python BaseHTTPServer 문서를 참고 하시면 됩니다.
 
리눅스 설치 후 다음 명령어로 서비스 
```
sudo service server start
```
