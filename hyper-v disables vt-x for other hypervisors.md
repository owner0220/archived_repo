Hyper-V 가 설치된 windows 8 pro 이상 버전에서
Hypervisor는 호스트 OS 밑에서 VT hardware의 안정성 관리를 위해서 계속 실행된다.
이때 hypervisor는 다른 것들의 VT 하드웨어 호출을 막는다.

Hyper-V를 꺼두면 Vbox를 사용할 수 있지만 Hyper-V로 동작하는 VM은 동작하지 않는다.

> docker-toolbox는 오래된 운영체제(Hyper-V가 지원되지 않는 OS)를 지원하기 위한 목적의 프로그램 이다.



참고
> https://en.wikipedia.org/wiki/Hyper-V
> https://docs.microsoft.com/ko-kr/virtualization/hyper-v-on-windows/about/
