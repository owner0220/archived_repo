from flask import Flask, render_template
import random
import os

app = Flask(__name__)

f =open("dictionary.txt",'r')
dic={}

for line in f.readlines():
    dic[line.split("\t")[0]]=line.split("\t")[1]


@app.route("/dictionary/<string:word>")
def dictionary(word):
    print(dic)
    if word in dic.keys():
        print("이건 서버에서 나오는 글")
        return word+"은(는) "+dic[word]+"입니다."
    else:
        return word+"은(는) 나만의 단어장에 없는 단어입니다."

   
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)from flask import Flask, render_template
import random
import os

app = Flask(__name__)

f =open("dictionary.txt",'r')
dic={}

for line in f.readlines():
    dic[line.split("\t")[0]]=line.split("\t")[1]


@app.route("/dictionary/<string:word>")
def dictionary(word):
    print(dic)
    if word in dic.keys():
        print("이건 서버에서 나오는 글")
        return word+"은(는) "+dic[word]+"입니다."
    else:
        return word+"은(는) 나만의 단어장에 없는 단어입니다."

   
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)