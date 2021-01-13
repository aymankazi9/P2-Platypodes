import model  # import of data file

from flask import Flask, render_template

import model


app = Flask(__name__)


@app.route('/')  # app routes to various html pages that we have assigned it to
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
def login_route():
    return render_template("loginpage.html", model=model.setup())


@app.route('/signuppage/')
def signup_route():
    return render_template("signup.html", model=model.setup())


@app.route('/feedback/')
def fb_route():
    return render_template("feedback.html", model=model.setup())


@app.route('/FAQ/')
def faq_route():
    return render_template("FAQ.html", model=model.setup())


@app.route('/california/')
def ca_route():
    return render_template("ca.html", model=model.setup())


@app.route('/texas/')
def tx_route():
    return render_template("tx.html", model=model.setup())


@app.route('/florida/')
def fl_route():
    return render_template("fl.html", model=model.setup())


@app.route('/newyork/')
def ny_route():
    return render_template("ny.html", model=model.setup())


@app.route('/test/')
def test_route():
    return render_template("test.html", model=model.setup())


@app.route('/tos&p/')
def tosp_route():
    return render_template("tos&p.html", model=model.setup())