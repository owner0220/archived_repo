## 원격 컴퓨터에 접속시 (web console UpCloud control panel 혹은 VNC 연결)
### 원격 컴퓨터 세팅(Remote Desktop settings)
1. 원격 컴퓨터 연결 권한 설정(RDP settings)
- 서버에는 로그인 했지만 RDP(Remote Desktop Protocol)은 여전히 연결이 되지 않을 때 원격 컴퓨터에 연결 권한이 있는지 확인한다.
> https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc742818(v=ws.11)

### 방화벽 (Firewall)
- ping(ICMP 프로토콜) 연결이 기본적으로 막혀있는 경우들이 많다.
1. 방화벽 인바운드 규칙에서 Remote Desktop 규칙을 찾아서 세팅한다.
- Window Server 2008은 Remote Desktop(TCP-In)과 Remote Desktop - RemoteFX (TCP-In) 두가지
- 서버 원격컴퓨터프로토콜 연결은 디폴트 포트로  3389 TCP 포트를 사용한다.
- 2012 Windows Servers 규칙은 기본적으로 Domain과 Private로 나뉜다. 또는 Public profiles as well as TCP and UDP protocols, which translates to 4 seperate Remote Desktop -User Mode rules, all of which would usually be enabled
- ICMP 프로토콜을 열기 위해서는 File and Printer Sharing (Echo Request - ICMPv4 - In)과 v6 두가지 IP 버전을 찾아서 정책 설정을 해주면 된다.

### 네트워크 연결
- 먼저 외부로 ping이 가는지 확인
```
ping 8.8.8.8
```
- 인터넷이 연결 안된 것처럼 보인다면 먼저 ip를 확인한다.
```
ipconfig
```
- Ethernet adapters: the private network, public IPv4 and public IPv6. 을 확인하면서 ip가 동적 할당으로 되어 있는지 확인한다.


### 연결은 됬지만 속도가 늦다면...
1. 네트워크 드라이버를 최신버전으로 업데이트 한다.


### 포트 충돌 (Port conflict)
1. 포트 확인
```
netstat -a -o
```
- PID(Program ID)가 다른데 하나의 port를 공유하는 것들이 포트 충돌을 일으킨다.

2. 현재 실행된 프로그램들의 포트 확인
```
tasklist /svc
```
3. 충돌 포트 번호 바꾸기
- 새로운 포트 번호는 1024~49151 사이 번호를 입력하면 되는데
- Windows Firewall Inbound 규칙을 새로운 규칙 추가로 만든다.
```
Rule Type: Port
Protocol and Ports: TCP, Specific local ports, <port number>
Action: Allow the connection
Profile: all options ticked
Name: Remote Desktop – TCP <port number>
```
여기서 port number는 원격컴퓨터프로토콜이 될 포트 번호이고 적용하기 위해서는 다시 연결을 시도하면 된다.
단, RDP 포트 번호는 레지스트리를 수정해서 바꿔야 하기 때문에 바꾸기 전에 백업을 해둬야 한다.


`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal SErver\WinStations\RDP-Tcp\PortNumber`

레지스트리 키를 (십진법으로)수정하고 저장한 후에 
Services(Local) list에서 Remote Desktop Service를 찾아서 restart 한다. 

`windows.server.example.com:34567`

