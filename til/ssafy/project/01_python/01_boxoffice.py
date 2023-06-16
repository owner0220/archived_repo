import requests
import os
import json
import csv


# 1번 =========================================================================================
base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json"
targetDT=["20181111","20181118","20181125","20181202","20181209","20181216","20181223","20181230","20190106","20190113"]
targetDT.reverse()
goal_url=base_url+"?key="+os.getenv("KOBIS_KEY")+"&weekGb=0&targetDt="


for i in range(len(targetDT)):
    
    old=[]
    old_title=[]

    with open('boxoffice.csv' , 'r') as user:
            reader=csv.reader(user, delimiter=',')
            for row in reader:
                old.append(row)
    
    for line in old:
        if line[1] not in old_title:
            old_title.append(line[1])
    
    
        #요청 텍스트 값 받음
    response = requests.get(goal_url+targetDT[i])
    raw_text = response.text
    
    #요청 값을 파이썬에서 사용하기 위해 dict로 변환
    json_dict=json.loads(raw_text)
    
    # 1단계 값 받기 
    # boxofficeresult 딕트값 가져오기
    boxOfficeResult=json_dict['boxOfficeResult']
    # weeklyBoxOfficeList  딕트값 가져오기
    weeklyBoxOfficeList=boxOfficeResult['weeklyBoxOfficeList']
    # print(old_title)
    with open('boxoffice.csv' , 'a+') as wuser:
            tempw=csv.writer(wuser, delimiter=',')
            for mlist in weeklyBoxOfficeList:
                movieCd=mlist['movieCd']
                movieNm=mlist['movieNm']
                audiAcc=mlist['audiAcc']
                reqdate=targetDT[0]
                if movieNm in old_title:
                    continue
                else:
                    tempw.writerow([movieCd,movieNm,audiAcc,reqdate])