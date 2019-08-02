expr 은 숫자만 있을 때 연산이 가능하다.


- 예제 테스트 파일 test.sh
```
!/bin/bash
st_time=`date +%S`
echo $st_time

sleep 10s

end_time=`date +%S`
echo $end_time

result=$( expr $end_time - $st_time )
echo $result
```
- 실행하면 정말 슬립 시간 10s 실행된 프로그램 실행 시간을 보여준다.
