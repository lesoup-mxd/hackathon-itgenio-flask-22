from app import app
from flask import render_template


@app.route('/')
@app.route('/in')
@app.route('/home')
@app.route('/home/index')
def index():
    return render_template(
        "home/index.html",
        )