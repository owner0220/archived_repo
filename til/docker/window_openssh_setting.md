- 운영체제 : window server 2012 r2
- powershell openssh 설치



Powershell

```powershell
# 1. 파일을 다운로드 받을 위치로 이동
PS C:\Users\Administrator> cd c:\users\admistrator\desktop

# 2. openssh를 Invoke-WebRequest를 이용해서 다운로드 (Invoke-WebRequest를 TLS 1.2나 1.3세팅 필요)
PS > [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# 3. 이제 powershell 모듈인 Invoke-WebRequest를 이용해서 open ssh를 다운로드 받는다.
PS C:\Users\Administrator\Desktop> Invoke-WebRequest -Uri "https://github.com/PowerShell/Win32-OpenSSH/releases/download/v7.7.2.0p1-Beta/OpenSSH-Win64.zip" -OutFile "openSSH.zip"

# 4. Expand-Archive 모듈이 없는 경우에는 .NET을 바로 사용해서 압축을 풀어준다.
# Add-Type 으로 .net 함수를 실행하는 필수 .dll을 로드한다. 그리고 [io.compression.zipfile]이 언급된 .dll 파일을 참고해 ::ExtractToDirectory 방법을 이용해 압축을 푼다.
PS C:\Users\Administrator\Desktop> Add-Type -assembly "system.io.compression.filesystem"

# 5. 이제 압축을 푼다.
PS C:\Users\Administrator\Desktop> [io.compression.zipfile]::ExtractToDirectory( 'C:\Users\Administrator\Desktop\openSSH.zip','C:\Program Files\' )

# 6. 압축을 풀어놓은 폴더로 들어가서 openssh를 설치
PS C:\Users\Administrator\Desktop> cd 'C:\Program Files\OpenSSH'
PS C:\Program Files\OpenSSH> .\install-sshd.ps1

# 제대로 설치가 되면 아래와 같은 output이 나온다. 끝에 successfully installed만 있어도 된다.
#**** Warning: Publisher OpenSSH resources are not accessible.
#[SC] SetServiceObjectSecurity SUCCESS
#[SC] ChangeServiceConfig2 SUCCESS
#[SC] ChangeServiceConfig2 SUCCESS
#sshd and ssh-agent services successfully installed

# 7. SSHD service 동작 확인 (sshd ssh 접속을 위한 것 , ssh-agent 접속에 authentication)
PS C:\Users\Administrator\Desktop\OpenSSH-Win64> get-service | findstr ssh
# Stopped ssh-agent OpenSSH Authentication Agent
# Stopped sshd OpenSSH SSH Server


# 8. ssh 를 받아줄 sshd 서비스 실행
PS C:\Program Files\OpenSSH> Start-Service sshd
PS C:\Program Files\OpenSSH> Start-Service ssh-agent

# 9. firewall 규칙 추가
PS C:\Users\Administrator> netsh advfirewall firewall add rule name=SSHPort dir=in action=allow protocol=TCP localport=22

# 10. reboot 할때마다 실행 할 수 있도록 서비스 등록
PS C:\Users\Administrator> Set-Service -Name sshd -StartupType "Automatic"
```

