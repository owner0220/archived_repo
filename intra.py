import encript
from selenium import webdriver
 #코드로 브라우저를 실행시키기 위한 인터넷 드라이버
#브라우저 실행
browser = webdriver.Chrome('driver/chromedriver') 
browser.get('https://edu.ssafy.com/comm/login/SecurityLoginForm.do')

def login():
    try:   
        if (browser.find_element_by_id('userId').is_displayed()) :
            userid=browser.find_element_by_id('userId')
            userid.send_keys(encript.decript("KJM&cYggYw1SWV$.aKS",encript.decripto))
            

        if browser.find_element_by_id('userPwd').is_displayed():
            pw=browser.find_element_by_id('userPwd')
            pw.send_keys(encript.decript("o$cmg6mg6f",encript.decripto))
            

        if browser.find_elements_by_class_name('form-btn') != None:
            submit=browser.find_element_by_class_name('form-btn')
            submit.click()
        print("실행됨")
    except:
        print("어디선가 오류가 발생했습니다.")
        return False
    return True

def incheck():
    try:  #출근 버튼이 보이면
        if (browser.find_element_by_id('btn').is_displayed()) :
            inck = browser.find_element_by_id('btn')
            inck.click
    except:
        print("출근하는데 오류가 발생했습니다.")
        return False
    return True

def outcheck():
    try:
        if (browser.find_element_by_id('btn').is_displayed()) :
            inck = browser.find_element_by_id('btn')
            inck.click
    except:
        print("퇴근하는데 오류가 발생했습니다.")
        return False
    return True


    
