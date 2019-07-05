### 쉘에서 폴더의 절대 위치 찾기
abspath=$(cd ${0%/*}&&echo $PWD/)


### 폴더의 절대 위치에서 상위 폴더를 표기 하려면?
uppath=$(Cd ${0%/*}&&cd ../&&echo $PWD/)
