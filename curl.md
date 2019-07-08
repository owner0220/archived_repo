### curl 데이터 보내기
#### 방법 1
```
user(사용자:aaaa / 비번:1111) 인증을 하고
긴 데이터가 저장된 2222.txt 파일을 보낼때 데이터를 의미하는 옵션 -d 설정
curl --user aaaa:1111 -X POST -d @2222.txt https://website.com/path
```


#### 방법 2
```
curl --user aaaa:1111 -X POST -d title="타이틀입니다" -d content="내용입니다." -d writedd="190708" http://website.com/path
```


#### 방법 3
```
curl --user aaaa:1111 -X POST --data "title=타이틀입니다&content=내용입니다.&writedd=190708" http://website.com/path
```
