from flask import Flask
import model
from flask import Flask
import model
from flask import render_template
import sqlite3 as sl3

app = Flask(__name__)
import stats
import storefb
from flask import request


@app.route('/')  # app routes to various html pages that we have assigned it to
def home_route():
    stats.fetch_web_data()
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


@app.route('/map/')
def map_route():
    conn = sl3.connect('platypodes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM COVIDSTATS")
    # rows=c.fetchall()
    # print(rows)
    # with conn:
    # data = conn.execute("SELECT * FROM COVIDSTATS")
    # for row in data:
    # print(row)

    return render_template("map.html", rows=c.fetchall(), model=model.setup())


@app.route('/feedback_form', methods=['POST'])
def feedback_form():
    fname = request.form['firstname']
    lname = request.form['lastname']
    mailid = request.form['email']
    service = request.form['type']
    opinion = request.form['feedback']
    storefb.insertfeedback(fname, lname, mailid, service, opinion)
    '''
    print (fname)
    print (lname)
    print (mailid)
    print(service)
    print(opinion)
    '''
    return render_template("feedback.html", model=model.setup())


@app.route('/tos&p/')
def tosp_route():
    return render_template("tos&p.html", model=model.setup())


@app.route('/home2/')
def home2_route():
    return render_template("home2.html", model=model.setup())
