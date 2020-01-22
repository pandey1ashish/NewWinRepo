#! /usr/env/bin python3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    return render_template("table.html", content=name)



if __name__ == "__main__":
    app.run()