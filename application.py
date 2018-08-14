import os
import psycopg2

from flask import Flask, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine('postgresql://rzeznik:Chujek123@localhost/edxP1')
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("initial.html")
    return "Project 1: TODO"

@app.route("/login")
def index():
    return render_template("login.html")
    return "Project 1: TODO"

@app.route("/register")
def index():
    return render_template("register.html")
    return "Project 1: TODO"


if __name__ == '__main__':
    app.run(debug=True)
