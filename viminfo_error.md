E138:Can't write viminfo file $HOME/.viminfo!


해결책 
```
cd $HOME/
ls -al vim*
```
으로 vim 파일들 확인

-rw-------  1 844 844     0 Jul 26 17:50 .viminfa.tmp
-rw-r--r--  1 844 844     0 Jul 16 19:26 .viminfb.tmp
-rw-------  1 844 844     0 Jul 10 17:23 .viminfc.tmp
-rw-------  1 844 844     0 Jun 13 15:29 .viminfd.tmp
-rw-r--r--  1 844 844     0 May  8 12:01 .viminfe.tmp
-rw-------  1 844 844     0 Apr 30 12:06 .viminff.tmp
-rw-------  1 844 844     0 Apr 24 19:15 .viminfg.tmp
-rw-------  1 844 844     0 Apr 10 19:59 .viminfh.tmp
-rw-------  1 844 844     0 Apr  1 18:53 .viminfi.tmp
-rw-------  1 844 844     0 Apr  1 18:53 .viminfj.tmp
-rw-------  1 844 844     0 Mar 26 13:12 .viminfk.tmp
-rw-------  1 844 844  4096 Mar 13 13:03 .viminfl.tmp
-rw-------  1 844 844     0 Feb 13 20:48 .viminfm.tmp
-rw-------  1 844 844     0 Jan 30 16:13 .viminfn.tmp
-rw-------  1 844 844 12121 Jul 30 13:23 .viminfo
-rw-------  1 844 844     0 May 31  2012 .viminfo.tmp
-rw-r--r--  1 844 844    20 Mar 29  2010 .vimrc

이렇게 tmp 파일들이 많다면


```
rm .vimin*.tmp
```
으로 tmp파일들을 삭제 해주면 문제 없이 돌아간다.
