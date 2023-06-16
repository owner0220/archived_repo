### 파일 삭제시 전부 삭제 하고 싶을 때 사용하는 것
```
find /root/test -name "*.pdf" -print0 | xargs -0 rm
```

단, 이때는 path 로 잡아준 root/test 하위 폴더에 까지 검색을 해서 삭제를 하므로 주의해야 한다.
지금 path로 잡아준 root/test 에서만 삭제하고 싶을 때는 아래처럼 써서 사용하면 된다
```
find . -maxdepth 1 -name "*.pdf" -print0 | xargs -0 rm
```
