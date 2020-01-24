#! /usr/env/bin python3

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/Roast', methods = ['GET','POST'])
def roast():
    print("inside Roast")
    return render_template("Roast.html")

@app.route('/Brew', methods = ['GET','POST'])
def brew():
    if request.method == 'POST':
        print(456)
        customer = request.form["firstname"]
        brew_type = request.form["roastType"]
        print(789)
        return render_template("Brew.html", selection = brew_type, custname = customer)   
    else:
        return "This is a GET request."



if __name__ == '__main__':
    app.run()