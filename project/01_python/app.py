import requests
import os
import json
import csv


# 1번 =========================================================================================
# base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json"
# targetDT=["20181111","20181118","20181125","20181202","20181209","20181216","20181223","20181230","20190106","20190113"]
# targetDT.reverse()
# goal_url=base_url+"?key="+os.getenv("KOBIS_KEY")+"&weekGb=0&targetDt="


# for i in range(len(targetDT)):
    
#     old=[]
#     old_title=[]

#     with open('boxoffice.csv' , 'r') as user:
#             reader=csv.reader(user, delimiter=',')
#             for row in reader:
#                 old.append(row)
    
#     for line in old:
#         if line[1] not in old_title:
#             old_title.append(line[1])
    
    
#         #요청 텍스트 값 받음
#     response = requests.get(goal_url+targetDT[i])
#     raw_text = response.text
    
#     #요청 값을 파이썬에서 사용하기 위해 dict로 변환
#     json_dict=json.loads(raw_text)
    
#     # 1단계 값 받기 
#     # boxofficeresult 딕트값 가져오기
#     boxOfficeResult=json_dict['boxOfficeResult']
#     # weeklyBoxOfficeList  딕트값 가져오기
#     weeklyBoxOfficeList=boxOfficeResult['weeklyBoxOfficeList']
#     print(old_title)
#     with open('boxoffice.csv' , 'a+') as wuser:
#             tempw=csv.writer(wuser, delimiter=',')
#             for mlist in weeklyBoxOfficeList:
#                 movieCd=mlist['movieCd']
#                 movieNm=mlist['movieNm']
#                 audiAcc=mlist['audiAcc']
#                 reqdate=targetDT[0]
#                 if movieNm in old_title:
#                     continue
#                 else:
#                     tempw.writerow([movieCd,movieNm,audiAcc,reqdate])

# 2번 =========================================================================================     
# base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"
# goal_url=base_url+"?key="+os.getenv("KOBIS_KEY")+"&movieCd="


# source=[]
# with open('boxoffice.csv' , 'r') as user:
#         reader=csv.reader(user, delimiter=',')
#         for row in reader:
#             source.append(row)

# movie_code_list=[]
# for i,low in enumerate(source):
#     if i >0 :
#         movie_code_list.append(low[0])


# for i in range(len(movie_code_list)):
#     respon = requests.get(goal_url+movie_code_list[i])
#     raw_text = respon.text
#     json_dict=json.loads(raw_text)
    
    
#     movieInfoResult = json_dict.get('movieInfoResult')
    
#     movieInfo = movieInfoResult.get('movieInfo')
#     movie_code = movieInfo.get('movieCd')
#     movie_name_ko = movieInfo.get('movieNm')
#     movie_name_en = movieInfo.get('movieNmEn')
#     movie_name_og = movieInfo.get('movieNmOg')
#     prdt_year = movieInfo.get('openDt')
#     showTm = movieInfo.get('showTm')
#     genres =movieInfo.get('genres')[0].get('genreNm')
#     directors = movieInfo.get('directors')[0].get('peopleNm')
#     watch_grade_nm = movieInfo.get('audits')[0].get('watchGradeNm')
#     actors=[]
#     actor1=None
#     actor2=None
#     actor3=None
#     print(len(movieInfo.get('actors')))
#     if len(movieInfo.get('actors')) != 0:
#         if len(movieInfo.get('actors')) > 3:
#             for i in range(3):
#                 actors.append(movieInfo.get('actors')[i].get('peopleNm'))
#         elif len(movieInfo.get('actors')) < 3:
#             try :
#                 for i in range(len(movieInfo.get('actors'))):
#                     actors.append(movieInfo.get('actors')[i].get('peopleNm'))
#             except:
#                 actors=[]
            
    
#     if len(actors) == 1:
#         actor1=actors[0]
#     if len(actors) == 2:
#         actor1=actors[0]
#         actor2=actors[1]
#     if len(actors) == 3:
#         actor1=actors[0]
#         actor2=actors[1]
#         actor3=actors[2]
    
#     with open('movie.csv' , 'a+') as wuser:
#         tempw=csv.writer(wuser, delimiter=',')
#         tempw.writerow([movie_code,movie_name_ko,movie_name_en,movie_name_og,prdt_year,genres,directors,watch_grade_nm,actor1,actor2,actor3])    



# 3번 =========================================================================================
# source=[]
# with open('boxoffice.csv' , 'r') as user:
#         reader=csv.reader(user, delimiter=',')
#         for row in reader:
#             source.append(row)

# movie_name_list=[]
# for j,low in enumerate(source):
#     if j >0 :
#         movie_name_list.append(low[1])
# movie_date=[]

# for k,low in enumerate(source):
#     if k >0 :
#         movie_date.append(low[3])

# base_url="https://openapi.naver.com/v1/search/movie.json"
# goal_url=base_url+"?display=10&start=1&query="
# jmovie_code={li[1]:li[0] for li in source}
# for i in range(len(movie_name_list)):
#     final_url=goal_url+movie_name_list[i].replace(" ", "")+"&yearfrom="+str((int(jmovie_code[movie_name_list[i]][0:4])-1))+"&yearto="+str(int(jmovie_code[movie_name_list[i]][0:4])+1)
    
    
#     req = requests.get(final_url, headers={"X-Naver-Client-Id":os.getenv('NAVER_ID'),"X-Naver-Client-Secret":os.getenv('NAVER_SECRET')}, params={'ie': 'UTF-8'})
    
    
    
#     res = req.text
#     j_dict=json.loads(res)

    
    
#     movie_code = jmovie_code[movie_name_list[i]]
    
#     image =  j_dict.get('items')[0].get('image')
#     link =   j_dict.get('items')[0].get('link')
#     userRating =  j_dict.get('items')[0].get('userRating')            
#     print([movie_code,image,link,userRating])
#     with open('movie_naver.csv' , 'a+') as muser:
#         tempw=csv.writer(muser, delimiter=',')
#         tempw.writerow([movie_code,image,link,userRating])

# 4번 =========================================================================================
# image_list={}
# image_code=[]
# with open('movie_naver.csv' , 'r') as naver:
#         read=csv.reader(naver, delimiter=',')
#         for i,ro in enumerate(read):
#             if i > 0:
#                 image_list[ro[0]]=ro[1]
#                 image_code.append(ro[0])

# for p in range(len(image_code)):
#     url = image_list[image_code[p]]
#     print(url)
#     r = requests.get(url)
#     with open('./images/'+image_code[p]+'.jpg', 'wb') as f:  
#         f.write(r.content)