from flask import Flask
import model
from flask import Flask
import model
from flask import render_template
import sqlite3 as sl3

app = Flask(__name__)
import stats
import storefb
import storesignup
# import storelogin
from flask import request


@app.route('/')  # app routes to various html pages that we have assigned it to
def home_route():
    stats.fetch_web_data()
    return render_template("/homesite/home.html", model=model.setup())


@app.route('/tracker/')
def tracker_route():
    return render_template("/homesite/tracker.html", model=model.setup())


@app.route('/newspage/')
def news_route():
    return render_template("/homesite/newspage.html", model=model.setup())


@app.route('/aboutus/')
def about_route():
    return render_template("/homesite/aboutus.html", model=model.setup())


@app.route('/loginpage/')
def login_route():
    return render_template("/homesite/loginpage.html", model=model.setup())


@app.route('/feedback/')
def fb_route():
    return render_template("/homesite/feedback.html", model=model.setup())


@app.route('/california/')
def ca_route():
    return render_template("/trackers/ca.html", model=model.setup())


@app.route('/texas/')
def tx_route():
    return render_template("/trackers/tx.html", model=model.setup())


@app.route('/florida/')
def fl_route():
    return render_template("/trackers/fl.html", model=model.setup())


@app.route('/newyork/')
def ny_route():
    conn = sl3.connect('platypodes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM COVIDSTATS")

    return render_template("/trackers/ny.html", rows=c.fetchall(), model=model.setup())


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

    return render_template("/homesite/map.html", rows=c.fetchall(), model=model.setup())


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

    return render_template("/misc/confirmation.html", model=model.setup())


@app.route('/sign_up', methods=['POST'])
def sign_up():
    mailadd = request.form['email']
    psswrd = request.form['psw']
    pssrep = request.form['psw-repeat']

    storesignup.insertsignup(mailadd, psswrd, pssrep)
    '''
    print (fname)
    print (lname)
    print (mailid)
    print(service)
    print(opinion)
    '''
    return render_template("/homesite/loginpage.html", model=model.setup())


@app.route('/login', methods=['POST'])
def login():
    mailadd = request.form['email']
    psswrd = request.form['psw']

    print('Login Page Username:', mailadd)
    print('Login Page Password:', psswrd)
    result = storesignup.logincheck(mailadd, psswrd)
    if result == "yes":
        return render_template("/homesite/dashboard.html", model=model.setup())
    else:
        return render_template("/homesite/loginpage.html", msg='Invalid Username or Password', model=model.setup())


@app.route('/tos&p/')
def tosp_route():
    return render_template("/misc/tos&p.html", model=model.setup())


@app.route('/home2/')
def home2_route():
    return render_template("/altdimension/home2.html", model=model.setup())


@app.route('/TPTReflections/')
def tpt_route():
    return render_template("/altdimension/tpt.html", model=model.setup())


@app.route('/CSPReflections/')
def csp_route():
    return render_template("/altdimension/cspreflections.html", model=model.setup())


@app.route('/cookies/')
def cookie_route():
    return render_template("/misc/cookies.html", model=model.setup())


@app.route('/confirmation/')
def confirmation_route():
    return render_template("/misc/confirmation.html", model=model.setup())


@app.route('/info/')
def info_route():
    return render_template("/homesite/information.html", model=model.setup())


@app.route('/FAQ/')
def faq_route():
    return render_template("/homesite/FAQ.html", model=model.setup())


@app.route('/prevention/')
def prevention_route():
    return render_template("/homesite/prevention.html", model=model.setup())


@app.route('/trends/')
def trends_route():
    return render_template("/homesite/trends.html", model=model.setup())


@app.route('/learnmore/')
def learn_route():
    return render_template("/homesite/learn.html", model=model.setup())


@app.route('/dashboard/')
def dash_route():
    return render_template("/homesite/dashboard.html", model=model.setup())

@app.route('/subscribe/')
def sub_route():
    return render_template("/homesite/subscribe.html", model=model.setup())

@app.route('/requirements/')
def requirement_route():
    return render_template("/altdimension/cbrequirements.html", model=model.setup())