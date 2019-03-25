from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def front(request):
    # url = "http://dart.fss.or.kr/api/search.json?auth=4add7af9e6cbf1210c75509e2d51ed520056fefd"
    # url = "http://dart.fss.or.kr/corp/searchCorpL.ax"
    # 회사 이름 검색 할 수 있는 사이트 URL
    url = "http://dart.fss.or.kr/dsab001/search.ax"
    # res = requests.get(url)
    data = {'currentPage': 1,
    'sort': 'date',
    'series': 'desc',
    'textCrpNm': '엘지씨엔에스',
    'maxResults': 100

}


    res = requests.post(url,data=data)
    soup = BeautifulSoup(res.content, 'html.parser')
    rows = soup.find_all('a')
    content = list()
    for i in rows:
        if "main.do" in i.get('href'):
            print(i.text.strip())
            print(i.get('href'))
            content.append((i.text.strip(),"http://dart.fss.or.kr"+i.get('href')))
    
    q = {'txt' : content, }




    return render(request,"front.html",q)
