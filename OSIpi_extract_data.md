> 2019-07-29
>
> OSIsoft PI SDK
>
> https://pisquare.osisoft.com/message/106763-re-pi-sql-query-results-to-file?commentID=106763#comment-106763
>
> https://techsupport.osisoft.com/Documentation/PI-AF-SDK/Html/M_OSIsoft_AF_PI_PIPoint_InterpolatedValues.htm

# OSI PI Sql query results to file

OSI PI에서 데이터를 가져올 수 있는 방법

### cli 환경에서 Programfiles/PI/amd/ 안에 있는 piconfig.exe 파일을 이용하는 방법

```
piconfig -node 서버주소 -port 5450 -username 유저이름 -password 비밀번호 < c:\test\input.txt
```

- input.txt 파일

```
echo off
@table piarc
@mode list
@stype delimited
@istr tag,starttime,endtime,count
@ostr ...
@ostr tag,time,value,
@output C:\test\Results.csv
tagename,*-1h,*,99999999999999
tagename,*-1h,*,99999999999999
tagename,*-1h,*,99999999999999
tagename,*-1h,*,99999999999999
tagename,*-1h,*,99999999999999
tagename,*-1h,*,99999999999999
@exit
```



### piconfig + 윈도우 배치, vbs 활용

- MainJob.bat 생성

```
@echo off  
setlocal EnableDelayedExpansion  
set file=tags.csv  
FOR /F "tokens=*" %%i IN (%file%) DO exportData.bat "%%i"  
```

- ExportData.bat

```
generate.vbs %1    
".\temp\%~1.bat"  
```

- tags.txt

추출하고자 하는 태그 리스트를 한줄씩 개행으로 구분해서 tags.txt 파일에 저장합니다.

- generate.vbs

```
' THIS FILE HAS BEEN HARD CODED TO EXTRACT ALL DATA FROM 01-JAN-01 TO CURRENT DATE. IF YOU    
' WANT TO USE THIS FILE TO EXTRACT FOR A SPECIFIC PERIOD ETC. MODIFY THE LOOP BELOW AND START/END    
' DATES.... - keilan    
    
if WScript.Arguments.Count = 0 then    
    WScript.Echo "Missing parameters"    
    
else    
    
' Define Constants    
    
  Const ForWriting = 2    
  Const ForReading = 1    
    
' Filesystem Objects    
    
  Set objShell = CreateObject("WScript.shell")    
  strCurrDir = objShell.CurrentDirectory    
    
  Dim objFSO, objFSOText, objFolder, batFile, outFile    
    
  Set objFSO = CreateObject("Scripting.FileSystemObject")    
    
' Tags    
    
  tag = WScript.Arguments(0)  
  
  
sWithOutQuotes = Replace(tag, """", "")   
  
  
newpath = strCurrDir & "\temp\" & sWithOutQuotes & ".bat"  
'WScript.Echo newpath  
  Set batFile = objFSO.OpentextFile(newpath, ForWriting, True)    
    
  ' a IS A LOOP FOR START YEAR TO END YEAR (ASSUMING THE 21ST CENTURY!    
  ' MODIFY IT AS PER REQUIREMENTS.... - Keilan    
    
for a = 16 TO 16    
    
  strDate = "01-JAN-" & RIGHT("0" & a,2)    
  endDate = "01-JAN-" & RIGHT("0" & a+1,2)    
    
  IF a = 16 THEN endDate = "*"    
    
  Set outFile = objFSO.OpentextFile(strCurrDir & "\" & tag & "_" & strDate & ".txt", ForWriting, True)    
    
  outFile.Writeline "@tabl piarc"    
  outFile.Writeline "@mode list"    
  outFile.Writeline "@output .\csv\" & sWithOutQuotes & "_" & strDate & ".csv"    
  outFile.Writeline "@timf9"    
  outFile.Writeline "@sigd 9"    
  outFile.Writeline "@istru tag, starttime, endtime, count"    
  outFile.Writeline "@ostru tag, time, value"    
  outFile.Writeline "@echo none"    
  outFile.Writeline "@ostru ..."    
  outFile.Writeline tag & "," & strDate & "," & endDate & ", 1000000"    
  outFile.Writeline "@ends"    
    
  outFile.Close    
    
  batFile.WriteLine Chr(34)&"C:\Program Files\PI\adm\piconfig" & Chr(34) & " < """ & sWithOutQuotes & "_" & strDate & ".txt"""    
    
  next    
    
  ' I ZIP THE FILES AFTER EXTRACTING DATA, MAKE SURE WZZIP EXISTS AND IS IN PATH VARIABLES    
    
  'batFile.WriteLine "wzzip " & tag & ".zip" & " *.CSV"    
  'batFile.WriteLine "del *.txt /f"    
  'batFile.WriteLine "del *.csv /f"    
  'batFile.WriteLine "del " & tag & ".bat"    
    
  batFile.Close    
    
end if   
```



### PowerShell

```powershell
#region defaults - apply changes here  
    $PIDataArchiveHostName = "GB-PIDA1"  
    $PIPointName = "CDT158"  
    $StartTimeString = "1-Jan-2019"  
    $EndTimeString = "1-Feb-2019"  
    $tsYears = 0  
    $tsMonths = 0  
    $tsDays = 0  
    $tsHours = 0  
    $tsMinutes = 0  
    $tsSeconds = 30  
    $tsMillisends = 0;  
#endregion  
# Creating a Stopwatch to measure execution time  
$StopWatch = New-Object System.Diagnostics.Stopwatch  
$StopWatch.Start()  
# Load AF SDK  
[System.Reflection.Assembly]::Load("OSIsoft.AFSDK, Version=4.0.0.0, Culture=neutral, PublicKeyToken=6238be57836698e6")  
# Instantiate the PIServer object  
$KnownServers = New-Object OSIsoft.AF.PI.PIServers  
$PIServer = $KnownServers[$PIDataArchiveHostName]  
# Load the PI Point  
$PIPoint = [OSIsoft.AF.PI.PIPoint]::FindPIPoint($PIServer, $PIPointName)  
# Define time boundaries and interval for interpolations  
$StartTime = [OSIsoft.AF.Time.AFTime]::Parse($StartTimeString)  
$EndTime = [OSIsoft.AF.Time.AFTime]::Parse($EndTimeString)  
$TimeRange = New-Object OSIsoft.AF.Time.AFTimeRange($StartTime, $EndTime)  
$TimeSpan = New-Object OSIsoft.AF.Time.AFTimeSpan($tsYears, $tsMonths, $tsDays, $tsHours, $tsMinutes, $tsSeconds, $tsMillisends)  
# Request Interpolated values  
$AFValues = $PIPoint.InterpolatedValues($TimeRange, $TimeSpan, "", $true)  
# Report amount of values returned and elapsed time  
$AFValues.Count  
$StopWatch.Elapsed.TotalSeconds  
```

