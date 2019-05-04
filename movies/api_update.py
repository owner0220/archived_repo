from urllib.request import urlopen,Request
import json
import os

class Movie_update:
    def __init__(self):
        #request 요청을 할 주소와 방법을 명시하고 스트림열 기본정보를 등록
        url = " http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key="+os.environ["KEY"]
        req = Request(url,method="GET")
        result = ""
        #스트림을 열어서 결과를 읽어 나온 str 정보를 result에 저장한다.
        with urlopen(req) as f:
            result = (f.read().decode('utf-8'))
        #저장된 str을 객체로 변환해준다.
        #str의 포맷이 json 규칙이기 때문에 json parse를 이용해
        #객체로 변환해 준다.
        result = json.loads(result)
        movieList = result.get("movieListResult").get("movieList")
        for movie in movieList:
            print(movie)
            # print(result)
            # print(type(result))
            # print(os.environ["KEY"])