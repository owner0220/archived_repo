### 리눅스에서 사용되는 nohup 명령어
1. 표준 출력을 nohup.out(또는 다른 곳)으로 돌리는 작업 수행
2. 프로세스가 중단되지 않는 백그라운드 작업 수행


```
nohup ./aaa.sh &
```

프롬프트가 돌아오면
ps -ef | grep aaa.sh  
으로 명령어를 수행해 해당 프로세스가 정상적으로 떠있는 것을 확인할 수 있다.
수행중인 작업을 종료하려면 ps -ef 명령어로 해당 프로세스의 pid를 확인하고 kill 명령어로 죽여야 한다.
또한 nohup 명령어에 의해 수행된 작업은 자동으로 nohup.out 이름으로 nohup 명령어를 실행한 위치에 자동으로 생성된다.

### nohup 로그 없이 다운
```
#방법
nohup 프로그램 매개변수 1> /dev/null 2>&1 &
#예시
nohup ./hadoop.sh 20160711 1> /dev/null 2>&1 &
```
- 백그라운드로 실행할 파일 hadoop.sh
- 실행할 파일에서 필요한 매개변수 20160711
- 1> 리다이렉션 (발생 echo를 리다이렉션)
- 2> 리다이렉션
- /dev/null (윈도우 휴지통같은)