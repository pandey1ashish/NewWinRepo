#! /usr/env/bin python3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    return render_template("table.html", content=name)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login_form.html")
    elif request.method == 'POST':
        text = request.form['first_name']
        return "Form submitted! %s"%text
    

@app.route('/usr_login', methods=['GET', 'POST'])
def usr_login():
    username = request.form['username']
    print(username)
    password = request.form['password']
    print(password)
    
    
if __name__ == "__main__":
    app.run()