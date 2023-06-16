```
pslist=`ps -ef | grep -v grep | grep dgf`

# echo 에 -E 옵션을 주면 이스케이프 문자들을 반영하여 결과를 출력해준다.
echo -E $pslist |
while read line
do


done

exit 0;

```
