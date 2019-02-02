from django.shortcuts import render, redirect
from shorter.models import urlplace
from django.conf import settings
import random, string
import re
# Create your views here.
def first(request):
    #데이터를 입력해서 서버로 보내는 역할
    #만약에 get 데이터가 있으면 받아서 보여준다.
    
    # def get_client_ip(request):
    #     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    #     if x_forwarded_for:
    #         ip = x_forwarded_for.split(',')[0]
    #     else:
    #         ip = request.META.get('REMOTE_ADDR')
    # return ip

    return render(request,"index.html")

def shorturl(request):
    url =  request.POST.get("url")

    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if (re.match(regex,url) is not None):
        shorturl =  randomchar(6)
        while True:
            try :
                urlplace.objects.get(shorturl=shorturl)
                shorturl =  randomchar(6)
            except:
                break  
        
        data = urlplace(url = url, shorturl = shorturl)
        data.save()
        #서버에서 데이터를 저장하고
        #매칭된 데이터를 담아서 보내준다.
        shortrul = "https://enigmatic-dawn-88839.herokuapp.com/" + shortrul
        return render(request,"index.html",{"url":url,"shorturl":shorturl})
    else:
        return render(request,"index.html",{"url":"인터넷 주소를 확인해주세요 ex) https://www.zuso.com"})


    # Create your views here.
def red(request,shorturl):
    shorten = urlplace.objects.get(shorturl=shorturl)

    return redirect(f"{shorten}")


def randomchar(num_chars):
    NUM_CHARS = num_chars # how long the string should be
    textbank = (string.ascii_uppercase + string.digits) * NUM_CHARS
    word = random.sample(textbank,NUM_CHARS)
    return "".join(word)
        


    

        
    