import requests
import flask
from selenium import webdriver

# 인터넷 브라우저로 출석체크를 실행
# 외부에서 서버로 요청을 보내면 출근,퇴근을 실행 할 수 있는 프로그램 만들기
# 1. 서버 구동                                        ok
# 2. 서버 요청 시 동작확인                             ok
#  - 브라우저 실행                                    ok
#  - 로그인                                           ok
#  - 요청 확인                                        ok
# 3. 로그인 세션 유지 및 화면 실행                      ok
# 4. 출근 버튼 클릭 및 결과 확인                        ok
# 5. 퇴근 버튼 클릭 및 결과 확인                        ok




#서버 실행
app = flask.Flask(__name__)
        


#코드로 브라우저를 실행시키기 위한 인터넷 드라이버
browser = webdriver.Chrome('driver/chromedriver') 
#브라우저 실행
browser.get('http://www.naver.com')




def login(logid,pwd):
    login_bt=browser.find_element_by_class_name('lg_local_btn')
    login_bt.click()
    # ID 입력 박스를 찾아
    id=browser.find_element_by_id('userId')
    # 입력 한다
    id.send_keys(logid)
    
    # PWD 입력 박스를 찾아
    id=browser.find_element_by_id('userPwd')
    # 입력 한다
    id.send_keys(pwd)

    #버튼을 찾아 클릭한다.
    naver_submit=browser.find_element_by_class_name('btn btn-lg btn-wide btn-primary')
    naver_submit.click()





@app.route('/')
def first():
    return "출석체크서버 동작!!!"

#logid와 pwd를 url로 전달해 로그인
#logid와 pwd를 ,로 구분해 전달
@app.route('/in/<string:logid>,<string:pwd>')
def inck(logid,pwd):
    login(logid,pwd)

    #버튼을 찾아
    naver_submit=browser.find_element_by_class_name('btn btn-lg btn-wide btn-primary')
    #클릭한다.
    naver_submit.click()

    return "출첵 됨 굳"


@app.route('/out/<string:logid>/<string:pwd>')
def outck(logid,pwd):
    login(logid,pwd)


    return "퇴근출첵 됨 굳"

 

 

 

