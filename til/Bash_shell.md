### Bash_shell

- Bash(Bourne Again Shell)

1. 설정 파일

- /etc/profile
- /etc/bashrc
- ~/.bash_profile
- ~/.bash_logout

/etc 디렉토리에 위치하는 파일들은 모든 사용자에게 일반적으로 적용되는 파일로 홈 디렉토리에서 숨김파일로 저장( . 으로 시작하는 파일들)

### /etc/profile

- 환경 변수와 bash가 실행될 때 실행되는 프로그램을 제어하는 **전역**적인 시스템 설정과 관련 되어 있다.

### /etc/bashrc

- 별칭(alias)과 bash가 실행될 때 실행되는 함수를 제어하는 전역적인 시스템 설정과 관련되어 있다. 파일이 생략될 수도 있으며 /etc/profile에 함께 포함 되기도 한다.

### ~/.bash_profile

- 환경 변수와 bash가 실행될 때 실행되는 프로그램을 제어하는 지역적인 시스템 설정과 관련된 파일이다. 이때 환경 변수들은 오직 그 사용자에게만 한정되며, 이외의 사람에게는 영향을 미치지 않는다. 이 파일은 /etc/profile이 실행된 다음 바로 실행된다.
- (모든 사용자에게 영향을 주는 /etc/profile과는 달리 ~/.bash_profile은 오직 bash를 실행하는 그 사용자에게만 영향을 준다.)



### ~/.bashrc

- 별칭(alias)과 bash가 실행될 때 실행되는 함수를 제어하는 **지역**적인 시스템 설정과 관련되어 있다. /etc/bashrc가 실행된 다음 바로 실행된다.



### ~/.bash_logout

- 사용자가 로그 아웃하기 직전에 실행하는 프로그램에 관한 bash의 지역적인 시스템 설정과 관련된 파일이다.







### 변수

- 변수는 컴퓨터 기억장소 안에 이름 붙여진 저장 위치이다. 하나의 변수를 정의할 때, 이 위치에는 그 변수의 정의된 값이 있게 된다.
- 환경 변수는 시스템에 의해 생성된 것이고 일반적으로 /etc/profile에 정의되더 있다.
- 지역 변수는 사용자가 정의하는 것으로 ~/.bashrc 같은 지역적인 설정 파일에 위치한다.



### 변수 정의

- 변수이름=값

```
#변수 정의
test="great"
#변수사용 위해 내보내기
export test
```



### 변수 접근

- 변수 앞에 $를 붙이면 된다.

```
$test
```

- 단순히 변수 이름 이었던 것이 $를 붙이면 변수에 저장된 값으로 변한다.





### 경로 설정

```
#방법 1
PATH=/bin:/user/bin:/usr/local/bin
export PATH
#방법 2
PATH=$PATH:/user/games
export PATH
```

- 변수에 새로운 변수를 저장할 때는 $를 활용해서 한다.
- 경로가 추가될 때는 경로 사이에 : 로 이어준다.



### 히스토리 관리

- 명령을 모두 기록하고 있다.
- HISTSIZE
- HISTFILE
- HISTFILESIZE

를 활용해서 히스토리를 관리 할 수 있다.



### 메일 체크

- MAIL
- MAILCHECK
- MAILPATH
- MAIL_WARNING
