from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess



chromepath="C:\Program Files\Google\Chrome\Application\chrome.exe"
userdatadir="..\userd\chd"

subprocess.Popen([chromepath,"--remote-debugging-port=9222",f"--user-data-dir={userdatadir}"])



chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "" # Your Chrome Driver path
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
