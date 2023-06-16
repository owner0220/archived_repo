### 리눅스, 윈도우 txt 파일 저장시 개행문자
- 간혹 파일을 저장하고 리눅스에서 vi를 통해 문서를 열어보면 개행문자가 ^M으로 표현되어 있는 경우가 있다.
- vi에서는 CTRL-M (^M) blue carriage return 문자로 파란색 글이 있는 경우를 말한다.
- vi 검색으로 ^M이 잡히지 않는다면 ^M 대신 \015를 사용하면 된다.
- 여기서 \015는 CR(Carrige Return, \r, 0x0d)으로 새로운 행을 추가한다는 의미
> LF(Line Feed, \n, 0x0a) 시작 위치로 복귀한다는 의미.
- 리눅스에서는 개행문자로 LF(0x0a)만 사용된다.
- 하지만 윈도우에서는 개행문자를 CRLF (0x0d 0x0a)로 표시해 1byte 더 크게 적용되면서 vi화면에 ^M과 같은 문자가 뜨게된다.



#### 해결책 in linux
1. dos 문자를 unix로 변경
```
dos2unix filename
```
2. upstream 에디터 sed
```
sed -e "s/\r//g" file > newfile
```
3. perl 사용
```
perl -pi -e 's/\r//g' file
```
