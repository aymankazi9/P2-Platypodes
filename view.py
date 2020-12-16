import model

from flask import Flask, render_template

app = Flask(__name__)

@app_route('/')
def home_route():
    return render_template("home.html", model=model.setup)


@app_route('/tracker/')
def tracker_route():
    return render_template("tracker.html", model=model.setup)


@app_route('/newspage/')
def news_route():
    return render_template("newspage.html", model=model.setup)


@app_route('/aboutus/')
def about_route():
    return render_template("aboutus.html", model=model.setup)


@app_route('/loginpage/')
def loginsignup_route():
    return render_template("loginpage.html", model=model.setup)
