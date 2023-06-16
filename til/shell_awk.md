### shell 끝에 세줄 없애기
cat aaa.csv | awk '!x[$0]++'




### shell | 을 기준으로 문자 잘라서 출력하기
```
AB1=`echo "${line}" | awk -F "|" '{print $1}' | tr -d ' '`
AB2=`echo "${line}" | awk -F "|" '{print $2}' | tr -d ' '`
AB3=`echo "${line}" | awk -F "|" '{print $3}' | tr -d ' '`
AB4=`echo "${line}" | awk -F "|" '{print $4}' | tr -d ' '`
AB5=`echo "${line}" | awk -F "|" '{print $5}' | tr -d ' '`
AB6=`echo "${line}" | awk -F "|" '{print $6}' | tr -d ' '`
```

데이터를 구분자 |를 기준으로 앞에서 부터 1~6까지 나뉘어 저장이 되는데
$1
$2
$3
을 통해서 불러올 수 있다.

그리고 보면 ""로 감싸지 않은 |가 있는데 이것은 이전의 명령들이 끝나고
나온 값을 이어서 다음의 명령을 실행하게 해준다.


