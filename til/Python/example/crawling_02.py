# 네이버 검색 순위 긁어오기

#크롤링2==============================================================
import requests
from bs4 import BeautifulSoup
url="https://www.naver.com"
req = requests.get(url).text
soup = BeautifulSoup(req,"html.parser")
pick = soup.select("tbody > tr")
num=1
for tr in pick:
    ct=0
    print(tr.select("td"))