from flask import Flask, render_template
import random
import os

app = Flask(__name__)

@app.route("/")
def git():
    
   return render_template("11_workshop.html")

   
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)