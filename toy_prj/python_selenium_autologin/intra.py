import encript
import wait_load
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

 #코드로 브라우저를 실행시키기 위한 인터넷 드라이버
#브라우저 실행
browser = webdriver.Chrome('driver/chromedriver') 
browser.get('https://edu.ssafy.com/comm/login/SecurityLoginForm.do')
sleep(0.5)
browser.maximize_window()
sleep(0.5)


def login():
    try:   
        if (browser.find_element_by_id('userId').is_displayed()) :
            userid=browser.find_element_by_id('userId')
            sleep(0.5)
            userid.send_keys(encript.decript("KJM&cYggYw1SWV$.aKS",encript.decripto))
            sleep(0.5)
            print("login1")
            
        if browser.find_element_by_id('userPwd').is_displayed():
            pw=browser.find_element_by_id('userPwd')
            sleep(0.5)
            pw.send_keys(encript.decript("o$cmg6mg6f",encript.decripto))
            sleep(0.5)
            print("login2")
            
        if browser.find_element_by_class_name('form-btn').find_element_by_tag_name('a').is_displayed():
            submit=browser.find_element_by_class_name('form-btn').find_element_by_tag_name('a')
            sleep(0.5)
            submit.click()
            sleep(0.5)
            print("login3")
        print("실행됨")
       
    except:
        print("어디선가 오류가 발생했습니다.")
        return False
    return True



def incheck():
    try:  #출근 버튼이 보이면
        if (browser.find_element_by_id('checkIn').is_displayed()) :
            inck = browser.find_element_by_id('checkIn')
            sleep(0.5)
            inck.click()
            sleep(0.5)
            print("출근")
            
    except:
        print("출근하는데 오류가 발생했습니다.")
        return False
    return True




def outcheck():
    try:
        if (browser.find_element_by_id('checkOut').is_displayed()) :
            outck = browser.find_element_by_id('checkOut')
            sleep(0.5)
            outck.click()
            sleep(0.5)
            print("퇴근")
            
    except:
        print("퇴근하는데 오류가 발생했습니다.")
        return False
    return True


    
def logout():
    try:   
        browser.get('https://edu.ssafy.com/comm/login/systemLogout.do')
        sleep(0.5)
        print("로그아웃!")
        
    except:
        print("어디선가 오류가 발생했습니다.")
        return False
    return True
