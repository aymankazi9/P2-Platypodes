import model

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template("home.html", model=model.setup())


@app.route('/tracker/')
def tracker_route():
    return render_template("tracker.html", model=model.setup())


@app.route('/newspage/')
def news_route():
    return render_template("newspage.html", model=model.setup())


@app.route('/aboutus/')
def about_route():
    return render_template("aboutus.html", model=model.setup())


@app.route('/loginpage/')
def loginsignup_route():
    return render_template("loginpage.html", model=model.setup())

@app.route('/sandiego/')
def sd_route():
    return render_template("sd.html", model=model.setup())

@app.route('/losangeles/')
def la_route():
    return render_template("la.html", model=model.setup())

@app.route('/sanfrancisco/')
def sf_route():
    return render_template("sf.html", model=model.setup())

@app.route('/newyork/')
def ny_route():
    return render_template("ny.html", model=model.setup())

@app.route('/test/')
def test_route():
    return render_template("test.html", model=model.setup())

