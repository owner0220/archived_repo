import flask
from flask import Flask

cnd=0

app = Flask(__name__)



@app.route("/")
def hello():
    print("3번")
    return "ww"


@app.route("/html_tag")    
def html_tag():
    print("2번")
    return """
    1번
    2번
    3번
    """

@app.route("/html_file")
def html_file():
    return flask.render_template("html_file.html")
    
@app.route("/welcome/<string:name>")
def welcome(name):
    return flask.render_template("welcome.html", people=name)
    
@app.route("/cube/<int:num>")
def cube(num):
    return flask.render_template("welcome.html", innum=num)

@app.route("/cube/<int:num>")
def cube1(num):
    triple = num*num*num
    return flask.render_template("cube.html",triple=triple,num=num)
    
@app.route('/lunch')
def lunch():
    import random
    menu = ['닭','삼겹살','짜장','라면']
    pick=random.sample(menu,1)[0]
    return flask.render_template("lunch.html",pick=pick)

@app.route('/lotto')
def lotto():
    import random
    lolst = range(1,46)
    lot = random.sample(lolst,6)
    lot.sort()
    print(lot)
    print(pick)
    return flask.render_template("lotto.html",pick=pick)
    
@app.route('/naver')
def naver():
    return flask.render_template("naver.html")
    
@app.route('/google')
def google():
    return flask.render_template("google.html")
