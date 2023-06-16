import requests
import os
import json
import csv

# 3번 =========================================================================================
source=[]
with open('boxoffice.csv' , 'r') as user:
        reader=csv.reader(user, delimiter=',')
        for row in reader:
            source.append(row)

movie_name_list=[]
for j,low in enumerate(source):
    if j >0 :
        movie_name_list.append(low[1])
movie_date=[]

for k,low in enumerate(source):
    if k >0 :
        movie_date.append(low[3])

base_url="https://openapi.naver.com/v1/search/movie.json"
goal_url=base_url+"?display=10&start=1&query="
jmovie_code={li[1]:li[0] for li in source}
for i in range(len(movie_name_list)):
    final_url=goal_url+movie_name_list[i].replace(" ", "")+"&yearfrom="+str((int(jmovie_code[movie_name_list[i]][0:4])-1))+"&yearto="+str(int(jmovie_code[movie_name_list[i]][0:4])+1)
    
    
    req = requests.get(final_url, headers={"X-Naver-Client-Id":os.getenv('NAVER_ID'),"X-Naver-Client-Secret":os.getenv('NAVER_SECRET')}, params={'ie': 'UTF-8'})
    
    
    
    res = req.text
    j_dict=json.loads(res)

    
    
    movie_code = jmovie_code[movie_name_list[i]]
    
    image =  j_dict.get('items')[0].get('image')
    link =   j_dict.get('items')[0].get('link')
    userRating =  j_dict.get('items')[0].get('userRating')            
    # print([movie_code,image,link,userRating])
    with open('movie_naver.csv' , 'a+') as muser:
        tempw=csv.writer(muser, delimiter=',')
        tempw.writerow([movie_code,image,link,userRating])
