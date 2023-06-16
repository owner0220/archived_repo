sed -n "/201901/!p" 파일 위치 > 새롭게 저장할 파일



응용
```shell
#!/bin/bash

cnt=0
end=2000
while [ $cnt -le $end ]
do

cnt=$(( $cnt + 1 ))

dd=`date -d "2014-01-01 ${cnt} month ago" +"%Y%m"`

echo $dd\|
target=$(( $cnt % 2 ))

echo read $target write $(( ( $target + 1 ) % 2 )).txt



sed -n "/${dd}|/!p" ./${target}.txt > ./$(( ( $target + 1 ) % 2 )).txt

done

exit 0;

```
