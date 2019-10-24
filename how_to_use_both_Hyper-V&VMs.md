정답은 아니지만 차선으로 가능한 방법 (부팅 환경을 새롭게 설정한다.)


```powershell
# Copy your GUID that was created, in this case it's "ff-23-113-824e-5c5144ea".
C:\>bcdedit /copy {current} /d "No Hyper-V" 
The entry was successfully copied to {ff-23-113-824e-5c5144ea}. 

# Replace "ff-23-113-824e-5c5144ea" with the GUID generated from the above cmd.
C:\>bcdedit /set {ff-23-113-824e-5c5144ea} hypervisorlaunchtype off 
The operation completed successfully.
```

When you're ready to make the switch:

1. Goto your start menu
2. Clict the power button
3. Hold down the Shift key
4. Select the "restart" option and reboot


이렇게 하면 리스타트 버튼을 눌렀을 때 
"Use another operating system"으로 "No Hyper-V"로 도커를 지우지 않고도 VM 시스템을 사용할 수 있다.

> https://nickjanetakis.com/blog/docker-tip-13-get-docker-for-windows-and-virtualbox-working-together
> https://www.hanselman.com/blog/SwitchEasilyBetweenVirtualBoxAndHyperVWithABCDEditBootEntryInWindows81.aspx
