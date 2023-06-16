import requests as rq
from bs4 import BeautifulSoup


# find companies
def find_companies():
    data = {
        'currentPage': 1, # 페이지 네이션
        'searchIndex': 1  # ㄱ ~ ㅎ 선택
    }

    res = rq.post('http://dart.fss.or.kr/corp/searchCorpL.ax', data=data)
    # print(res.text)

    soup = BeautifulSoup(res.content, 'html.parser')

    rows = soup.find(class_='pop_table_A').find(class_='table_scroll').find_all('tr')

    if len(rows) > 1:
        for row in rows:
            no = row.find_all('input')[1].get('value').strip()
            columns = row.find_all('td')
            company_name = columns[0].text.strip()
            name = columns[1].text.strip()
            desc = columns[3].text.strip()
            print(company_name, select_popup(no))


def search_companies():
    # search companies
    # http://dart.fss.or.kr/dsab001/search.ax
    res = rq.post('http://dart.fss.or.kr/dsab001/search.ax', data={
        "textCrpNm": "나경상사/나경인터내셔날/나나건설/나나주택/나노/나노/나노이앤씨/나노인터페이스/나노정밀/나노캠텍",
        "currentPage": 1,
        # "maxResults": 15,
        # "maxLinks": 10,
        # "sort": "date",
        # "series": "desc",
        # "textCrpCik": "",
        # "finalReport": True,
        # "startDate": "20170518",
        # "endDate": "20171118"
    })
    soup = BeautifulSoup(res.content, 'html.parser')
    page_info = soup.find(class_="page_info")
    rows = soup.select('table tbody tr')

    for row in rows:
        columns = row.find_all('td')

        number = text_filter(columns[0].text.strip())                # 번호
        company_name = text_filter(columns[1].text.strip())  # 공시대상회사
        report_name = text_filter(columns[2].text.strip())   # 보고서 명
        who_give = text_filter(columns[3].text.strip())      # 제출인
        data = text_filter(columns[4].text.strip())          # 접수일자
        etc = text_filter(columns[5].text.strip())           # 기타

        print(number, company_name, report_name, who_give, data, etc )

    print(page_info.text.strip())


def select_popup(select_key):
    url = "http://dart.fss.or.kr/dsae001/selectPopup.ax?selectKey=%s" %(select_key)
    res = rq.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    return {row.find('th').text: text_filter(row.find('td').text) for row in soup.find_all('tr')}


def text_filter(t):
    return t.replace('\n', '').replace('\r', '').replace('\t', '')


if __name__ == '__main__':
    # search_companies()

    find_companies()