### 19.12.11 윈도우 환경
### certutil.exe 활용
### 이전에는 SCCM프로그램으로 돌리기도 했다.
## how to export a certificate with powershell?

```powershell
Enter-PSSession -ComputerName ADFS-01
$thumprint = (Get-ChildItem -Path Cert:\LocalMachine\My | Where-Object {$_.Subject -match "CN=ssl.networknet.nl"}).Thumbprint
$pwd = ConvertTo-SecureString -String "password" -Force -AsPlainText
Get-ChildItem -Path Cert:\LocalMachine\My\$thumprint | Export-PfxCertificate -FilePath C:\ssl.networknet.nl.pfx -Password $pwd
```

## how to import a certificate with powershell?
```powershell
Enter-PSSession -ComputerName ADFS-02
$pwd = ConvertTo-SecureString -String "password" -Force -AsPlainText
Import-PfxCertificate -FilePath C:\adfs.networknet.nl.pfx Cert:\LocalMachine\My -Password $pwd
```

