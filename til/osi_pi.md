OSI_PI server menu
https://techsupport.osisoft.com/Documentation/PI-Powershell/html/51ab160b-1bc3-43e2-810d-d45214fa4606.htm
https://pisquare.osisoft.com/message/114339-re-how-to-export-digital-tags-with-powershell?commentID=114339#comment-114339
https://pisquare.osisoft.com/community/all-things-pi/blog/2016/12/19/timestamps-and-the-powershell-tools-for-the-pi-system
https://pisquare.osisoft.com/thread/39114-sampled-values-with-powershell
https://livelibrary.osisoft.com/LiveLibrary/content/en/sql-commander-lite-v1/GUID-6D57C5C4-4A9F-4FA2-92DE-48AFD67BF940#addHistory=true&filename=GUID-52DF8F26-5D52-4010-AFDB-BE5A3317CC29.xml&docid=GUID-6D57C5C4-4A9F-4FA2-92DE-48AFD67BF940&inner_id=&tid=&query=&scope=&resource=&toc=false&eventType=lcContent.loadDocGUID-6D57C5C4-4A9F-4FA2-92DE-48AFD67BF940

https://pisquare.osisoft.com/message/106763-re-pi-sql-query-results-to-file?commentID=106763#comment-106763
*piconfig* 
Contents of c:\test\PiExtract.txt

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

.

.

.

tagename,*-1h,*,99999999999999

@exit
