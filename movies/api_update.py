from urllib.request import urlopen,Request
import json
import os

class Movie_update:

    def __init__(self):
        #request 요청을 할 주소와 방법을 명시하고 스트림열 기본정보를 등록
        korean = " http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key="+os.environ.get("KEY")
        naver = "https://openapi.naver.com/v1/search/movie.json?query=endgame"
        theMvDB = "https://api.themoviedb.org/3/search/movie?api_key="+os.environ.get("db_api_key")+"&query=Jack+Reacher"

        # self.get_movie_korean(self.get_req_json(korean))
        # self.get_movie_naver(self.get_req_json(naver,{"X-Naver-Client-Id":os.environ.get("Client_Id"),"X-Naver-Client-Secret":os.environ.get("Client_Secret")}))
        # self.get_movie_MvDB(self.get_req_json(theMvDB))
    
    def get_req_json(self,url,headers={}):
        req = Request(url,method="GET",headers=headers)
        # print(req)
        result = ""
        #스트림을 열어서 결과를 읽어 나온 str 정보를 result에 저장한다.
        with urlopen(req) as f:
            result = (f.read().decode('utf-8'))
        #저장된 str을 객체로 변환해준다.
        #str의 포맷이 json 규칙이기 때문에 json parse를 이용해
        #객체로 변환해 준다.
        json_result = json.loads(result)
        return json_result            
    
    def get_movie_korean(self,json_object):
        movieList = json_object.get("movieListResult").get("movieList")
        for movie in movieList:
            print(movie)
    
    def get_movie_naver(self,json_object):
        movieList = json_object.get("items")
        for movie in movieList:
            print(movie)
    
    def get_movie_MvDB(self,json_object):
        movieList = json_object.get("results")
        for movie in movieList:
            print(movie)
        