import requests
import os
import json
import csv


# 2번 =========================================================================================     
base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"
goal_url=base_url+"?key="+os.getenv("KOBIS_KEY")+"&movieCd="


source=[]
with open('boxoffice.csv' , 'r') as user:
        reader=csv.reader(user, delimiter=',')
        for row in reader:
            source.append(row)

movie_code_list=[]
for i,low in enumerate(source):
    if i >0 :
        movie_code_list.append(low[0])


for i in range(len(movie_code_list)):
    respon = requests.get(goal_url+movie_code_list[i])
    raw_text = respon.text
    json_dict=json.loads(raw_text)
    
    
    movieInfoResult = json_dict.get('movieInfoResult')
    
    movieInfo = movieInfoResult.get('movieInfo')
    movie_code = movieInfo.get('movieCd')
    movie_name_ko = movieInfo.get('movieNm')
    movie_name_en = movieInfo.get('movieNmEn')
    movie_name_og = movieInfo.get('movieNmOg')
    prdt_year = movieInfo.get('openDt')
    showTm = movieInfo.get('showTm')
    genres =movieInfo.get('genres')[0].get('genreNm')
    directors = movieInfo.get('directors')[0].get('peopleNm')
    watch_grade_nm = movieInfo.get('audits')[0].get('watchGradeNm')
    actors=[]
    actor1=None
    actor2=None
    actor3=None
    # print(len(movieInfo.get('actors')))
    if len(movieInfo.get('actors')) != 0:
        if len(movieInfo.get('actors')) > 3:
            for i in range(3):
                actors.append(movieInfo.get('actors')[i].get('peopleNm'))
        elif len(movieInfo.get('actors')) < 3:
            try :
                for i in range(len(movieInfo.get('actors'))):
                    actors.append(movieInfo.get('actors')[i].get('peopleNm'))
            except:
                actors=[]
            
    
    if len(actors) == 1:
        actor1=actors[0]
    if len(actors) == 2:
        actor1=actors[0]
        actor2=actors[1]
    if len(actors) == 3:
        actor1=actors[0]
        actor2=actors[1]
        actor3=actors[2]
    
    with open('movie.csv' , 'a+') as wuser:
        tempw=csv.writer(wuser, delimiter=',')
        tempw.writerow([movie_code,movie_name_ko,movie_name_en,movie_name_og,prdt_year,genres,directors,watch_grade_nm,actor1,actor2,actor3])    
