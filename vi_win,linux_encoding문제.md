Win파일에서 가져온 linux

변환 방법1 (파일 자체 포맷을 완전히 변환)
```
#리눅스에서 win파일을 unix 계열로 파일 변환(dos2unix 프로그램 이용)
dos2unix
```

변환 방법2
```
#리눅스 vi편집기로 파일을 열고 아래와 같은 명령어 입력(찾아 바꾸기)
:%s/^M//g
#(단, 여기서 ^M은 Ctrl-V 키와 Ctrl-m 을 눌러서 생기는 문자를 말한다.)
```

변환 방법3 (vi로 열때만 포맷을 변경 적용해서 읽는다. ※파일 자체 포맷을 변경하지 않는다.)
```
#리눅스 vi편집기로 파일 포맷 변경하기 (vi편집기로 파일을 연 후 아래와 같은 명령어를 입력한다.)
:set ff=unix
```

관련된 사용 설명서는 아래를 참조
> http://vimdoc.sourceforge.net/htmldoc/options.html#'fileformat'
> https://vim.fandom.com/wiki/File_format
> https://stackoverflow.com/questions/82726/convert-dos-line-endings-to-linux-line-endings-in-vim
