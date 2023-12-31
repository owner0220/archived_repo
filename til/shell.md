### 환경변수 설정 파일
- 터미널 세션, 원격 로그인 세션 사용 ,로그인 시 파일이 로드 된다.
.bashrc
.bash_profile
.bash_login
.profile


- 전체 환경 변수
/etc/enviroment
/etc/profile
/etc/profile.d/
/etc/bash.bashrc/

### 상대경로 / 절대경로
- 상대경로는 쉘 환경에서 파일을 실행한 위치를 참조한다.



https://opentutorials.org/course/2598/14210


### WGET
```
wget -c --tries=0 --retry-connrefused --timeout=2 --wait=1 \
http://www.schmidp.com/bigfile
```
설명
- c tells wget to continue a download, so you can stop wget and restart it later without downloading the whole file again.
– tries=0 means that the download will be tried indefinitely if the connection breaks.
– retry-connrefused forces wget to retry even if the server is currently not listening.
– timeout=2 tells wget to reconnect if no data is received for more than 2 seconds.
– wait=1 means wget will sleep for one second before it reconnects.

shell은 단순히 사용자의 명령을 실행시키는 

### 텍스트 파일을 쉘 변수에 집어 넣는 방법
```
#!/bin/bash
value=$(<config.txt)
echo "$value"
```

shell은 일반 프로그래밍 언어와 달리 subshell 부분이 끝나고 나면 subshell에서 사용한 변수들이 모두 날아간다.
(subshell 이전에 변수를 선언해서 사용해도 마찬가지)
그래서 while 문을 쓸 때도 for 문으로 대체 해서 쓰거나
```
while read line
do

done < $input
```
이러한 형태로 사용한다.


### ^M 개행 문자 삭제하는 방법
```
샘플
cat -v file.log
abcd^M
bcde^M
cdef^M
defg^M
```

1. tr
```
#방법 1
tr -d '^M' < file.log
#방법 2
tr -d '\015' < file.log
#변경된 내용 저장
tr -d \015' < file.log > file.tr.log
```
2. sed
```
#방법 1
sed 's/^M//g' file.log
#방법 2
sed 's/\015//g' file.log
#변경된 내용 저장
sed -i 's/^M//g' file.log
```
3.awk
```
#방법 1
awk 'sub(/^M/,"");' file.log
#방법 2
awk 'sub(/\015/,"");' file.log
#변경된 내용 저장
awk 'sub(/\015/,"");' file.log > file.awk.log
```
4.perl
```
#방법 1
perl -p -e 's/^M//g' file.log
#방법 2
perl -p -e 's/\015//g' file.log
#변경된 내용 저장
perl -pi -e 's/\015//g' file.log
```
5.vi
```
#방법 1
:%s/^M//
#방법 2
:%s/\015//
#방법 3
:set ff=unix
:wq
```


