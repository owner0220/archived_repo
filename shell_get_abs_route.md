### 쉘에서 폴더의 절대 위치 찾기
abspath=$(cd ${0%/*}&&echo $PWD/)


### 폴더의 절대 위치에서 상위 폴더를 표기 하려면?
uppath=$(Cd ${0%/*}&&cd ../&&echo $PWD/)

### readlink
- 디렉토리에 대해서는 실제 절대 경로를 알려준다.
- 실질적 기능 : pwd 기능에 문자를 붙인 것과 같다.

```
# 쉘 입력 예시
readlink -f 파일이름
```
```
# 쉘 출력
/root/data/파일이름
```


### basename
- 파일이름 추출
- 실질적 기능 : 슬래시로 구분되는 맨 마지막을 뜯어서 준다. (단,슬래시로 구분된 문자들 중에 뒤에서 부터 공백이 아닌 문자를 출력한다.)
```
# 쉘 입력 예시1
basename /root/ee/qwe.jpg
```
```
# 예시1 입력 결과
qwe.jpg
```
```
# 쉘 입력 예시2 ( 확장자 제거 할 수도 있다.)
basename /root/ee/qwe.jpg    .jpg
```
```
# 예시2 입력 결과
qwe
```
```
# 쉘 입력 예시3 (문자 제거목적에서 사용할 수 있다.)
basename /root/ee/qwe.jpg  we.jpg
```
```
# 예시3 입력 결과
q
```


### dirname
- 파일이름 부분을 제외한 path 부분만을 알려준다
- 실질적 기능 : 슬래시(/)기준으로 맨 마지막 문자를 뜯어준다.
```
# 쉘 입력 예시1
dirname root/test/2/in.jpg
```
```
# 예시1 입력 결과
root/test/2
```
```
# 쉘 입력 예시2
dirname /root/test/2/in.jpg
```
```
# 예시2 입력 결과
/root/test/2
```
```
# 쉘 입력 예시3
dirname /root/test/2/in.jpg/out.jpg
```
```
# 예시3 입력 결과
/root/test/in.jpg
```
