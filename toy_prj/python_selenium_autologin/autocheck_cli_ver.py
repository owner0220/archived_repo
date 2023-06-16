# parser.py
import requests
from bs4 import BeautifulSoup as bs


# 개발중...
# 인터넷 브라우저 동작 없이 코드로 출석체크를 실행하기 위한 프로그램
# 1. 인터넷 접속                                      ok
# 2. 로그인 요청                                      --
#  - 파라미터 찾기                                    --
#  - 요청 보내기                                      --
#  - 요청 확인                                        --
# 3. 로그인 세션 유지                                 --
# 4. 로그인 중에 화면 정보 받아서 실행시키기            --


LOGIN_INFO = {
    'userId': '아이디를 입력',
    'userPassword': '비밀번호를 입력'
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    # HTTP POST request: 로그인을 위해 POST url와 함께 전송될 data를 넣어주자.
    login_req = s.post('https://www.naver.com', data=LOGIN_INFO)
    # 어떤 결과가 나올까요?
    print(login_req.status_code)

val = s.get("https://www.naver.com")
print(val.text)
