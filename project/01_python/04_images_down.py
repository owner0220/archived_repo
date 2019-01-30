import requests
import os
import json
import csv


# 4번 =========================================================================================
image_list={}
image_code=[]
with open('movie_naver.csv' , 'r') as naver:
        read=csv.reader(naver, delimiter=',')
        for i,ro in enumerate(read):
              if i > 0:
                image_list[ro[0]]=ro[1]
                image_code.append(ro[0])

for p in range(len(image_code)):
    url = image_list[image_code[p]]
    print(url)
    r = requests.get(url)
    with open('./images/'+image_code[p]+'.jpg', 'wb') as f:  
        f.write(r.content)