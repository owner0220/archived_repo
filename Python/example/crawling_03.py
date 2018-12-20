#게시판 제목 긁어오기

#크롤링3==============================================================
import requests
from bs4 import BeautifulSoup

url = "http://www.jnu.ac.kr"
req = requests.get(url).text
soup = BeautifulSoup(req,"html.parser")
a="#cnts_list_new > div:nth-of-type(1) > table:nth-of-type(3)"
coinset = soup.select(a)
print(coinset)
