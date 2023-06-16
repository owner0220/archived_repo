import encript
import wait_load
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
 #코드로 브라우저를 실행시키기 위한 인터넷 드라이버
#브라우저 실행
browser = webdriver.Chrome('driver/chromedriver') 
browser.get('https://edu.ssafy.com/comm/login/SecurityLoginForm.do')
browser.maximize_window()

print(str(browser.find_element_by_tag_name('html')))