## 인터넷 없이 파이썬 패키지 설치

- 설치파일 준비
- pip를 이용해 설치



1. 설치파일 준비

- pip install 패키지이름 --download="다운로드할 폴더 위치 경로"
- 입력 후 실행해서 다운로드 받는다. 단, 설치할 컴퓨터의 OS에 맞는 파일을 확인해서 다운로드 하자.

```bash
# 입력 예시
pip install pandas --download="/home/abcd/required_packages"
```

- 다운로드 후 required_packages 폴더로 이동해보면, *.whl파일이나 tar.gz파일이 있다.

- 이 파일을 USB로 복사해서 준비해 놓는다.

2. 인터넷 없는 컴퓨터에 USB를 연결하고 파일 설치

- pip install *파일이름* -f *파일있는디렉토리* --no-index
- 입력 후 실행해서 설치한다.

```bash
# 입력 예시
pip install tabulate-0.7.7-py2.py3-none-any.whl -f ./ --no-index
```



