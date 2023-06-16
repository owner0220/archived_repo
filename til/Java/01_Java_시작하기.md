[TOC]



# Java 개발 시작하기

## JAVA  플랫폼 3대 구성요소

### JDK | Java Development Kit

- 항상 호환버전의 JRE가 포함되고 JRE에는 기본 JVM을 포함한다.





### JVM | Java Virtual Machine

- 자바 애플리케이션이 디바이스 또는 클라우드 환경에서 실행되는 데 필요한 리소스를 확보하도록 보장하는 역할을 한다.





### JRE | Java Runtime Environment

- 자바를 실행하기 위해 필요한 소프트웨어로 다른 구성 요소의 컨데이너이며 각 구성 요소의 활동을 조율하는 역할을 한다.
- Java class libraries
- Java class loader
  - 클래스를 로드해 코어 자바 클래스 라이브러리에 연결하는 역할을 한다.



---

### 결론!

JDK만 설치하고 java 파일을 컴파일해주는 자바 컴파일러 (javac.exe)와

컴파일된 자바 프로그램을 실행해 줄 자바 런처(java.exe)의

위치를 환경변수로 등록해주면 자바개발 환경이 마련된다.

※ 다른 프로그램을 사용하면서 특별히 JVM, JRE를 설정해줄 때에만 따로 버전별 다운로드 해 연결해준다.

