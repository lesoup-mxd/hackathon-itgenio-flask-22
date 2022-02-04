from flask import Flask, render_template, redirect, url_for
history = {}

app = Flask(__name__)
@app.route("/")
def index():
    global history
    history = {}
    return render_template("index.html")