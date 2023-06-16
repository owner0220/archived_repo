### Shell에서 폴더 안 파일 목록 비교할 때

```shell
#!/bin/bash
ls -l ./input > readline.csv

ls -al | grep 파일명 | wc -l


cat ./readline.csv |
while read line
do
FILENAME=`echo ${line} | awk -F " " '{print $9}' | tr -d ' '`


SUCCESS_OR_FAIL=`ls ./text/ | grep "${FILENAME}" | wc -l`

if [[ "${SUCCESS_OR_FAIL}" == "0" ]];then

echo $FILENAME

fi

done
exit 0;


```
#### 상황
- 폴더 두개가 있을 때 확장자는 다른 같은 이름의 파일 중 한 폴더에만 존재하는 것을 찾을 때
- 제목은 완전히 구별된다는 전제조건(unique 하다)

### 로직
- 한쪽 폴더 리스트를 뽑아서 csv에 저장한다.
- 저장한 csv파일을 불러와 한줄 씩 읽으며 파일이름을 뽑아 낸다.
- 확인할 다른 폴더의 파일 리스트에 위의 파일 이름을 비교하고 있으면 1 없으면 0
- if 문에서 그 값을 확인하고 없는 경우만 출력한다.
