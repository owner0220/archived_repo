#구글 검색으로 이미지를 긁어오세요

#크롤링4==============================================================
import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q="
search = "제니"
req = requests.get(url+search).text
soup = BeautifulSoup(req,"html.parser")
img = soup.find_all("img")
for i in img:
    print(i)