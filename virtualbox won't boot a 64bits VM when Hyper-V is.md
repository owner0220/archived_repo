### Error
```
Running pre-create checks...
Error with pre-create check: "Hyper-V is installed. VirtualBox won't boot a 64bits VM when Hyper-V is activated. If it's installed but deactivated, you can use --virtualbox-no-vtx-check to try anyways"
Looks like something went wrong in step ´Checking if machine default exists´
```



### Solve
- c/program files/docker toolbox/start.sh 수정

원본
```
...생략
STEP="Checking if machine $VM exists"
if [ $VMEXISTSCODE -eq 1 ]; then
  "${DOCKERMACHINE}" rm -f "${VM}" &> /dev/null || :
  rm -rf ~/.docker/machine/machines/"${VM}"
  #set proxy variables if they exists
  if [ -n ${HTTPPROXY+x} ]; then
    PROXYENV="$PROXYENV --engine-env HTTPPROXY=$HTTPPROXY"
  fi
  if [ -n ${HTTPSPROXY+x} ]; then
    PROXYENV="$PROXYENV --engine-env HTTPSPROXY=$HTTPSPROXY"
  fi
  if [ -n ${NOPROXY+x} ]; then
    PROXYENV="$PROXYENV --engine-env NOPROXY=$NOPROXY"
  fi

  "${DOCKERMACHINE}" create -d virtualbox $PROXYENV "${VM}"
fi
...생략
```

굵은 글씨를 다음 코드로 변경
```
...생략
STEP="Checking if machine $VM exists"
if [ $VMEXISTSCODE -eq 1 ]; then
  "${DOCKERMACHINE}" rm -f "${VM}" &> /dev/null || :
  rm -rf ~/.docker/machine/machines/"${VM}"
  #set proxy variables if they exists
  if [ -n ${HTTPPROXY+x} ]; then
    PROXYENV="$PROXYENV --engine-env HTTPPROXY=$HTTPPROXY"
  fi
  if [ -n ${HTTPSPROXY+x} ]; then
    PROXYENV="$PROXYENV --engine-env HTTPSPROXY=$HTTPSPROXY"
  fi
  if [ -n ${NOPROXY+x} ]; then
    PROXYENV="$PROXYENV --engine-env NOPROXY=$NOPROXY"
  fi
# 변경된 부분==================================================
"${DOCKERMACHINE}" create -d virtualbox $PROXYENV "${VM}"
# ============================================================
fi
...생략
```


 
