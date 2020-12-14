import model

from flask import Flask, render_template

app = Flask(__name__)

@app_route('/')
def home_route():
    return render_template("home.html, ")
