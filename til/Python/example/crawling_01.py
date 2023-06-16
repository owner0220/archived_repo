# 다음 검색 순위 긁어오기


#크롤링1==============================================================

import requests
from bs4 import BeautifulSoup

url = "https://daum.net"
#res = requests.get(url).status_code
res = requests.get(url).text
soup = BeautifulSoup(res,"html.parser")
a = "#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li > div > div:nth-of-type(1) > span.txt_issue > a"
pick = soup.select(a)
rank = 1
for x in pick:
    print(str(rank)+"위 : "+x.text)
    rank+=1 