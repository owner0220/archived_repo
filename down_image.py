import requests

url = "https://edu.ssafy.com/data/upload_files/crossUpload/openLrn/ebook/unzip/A20190212170431657/"
filepath = "assets/page-images/page-3754782000-1.jpg"


for i in range(1,55):
    while True:
        aurl = url+"assets/page-images/page-3805544000-"+str(i)+".jpg"
        req = requests.get(aurl)
            if req.status_code == 200:
                with open("Django_book_0"+str(i)+".jpg",'wb') as w:
                    w.write(req.content)
                    break



req = requests.get(url+filepath)
with open("Django_book_00.jpg",'wb') as w:
    w.write(req.content)
