import os
import psycopg2

from flask import Flask, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

# Set up database
engine = create_engine('postgresql://rzeznik:Chujek123@localhost/csv_test')
db = scoped_session(sessionmaker(bind=engine))


#Users = db.execute("SELECT * FROM users").fetchall()
#print(Users)
flight = db.execute("SELECT (username, password) FROM users").fetchall()
print(flight)
#for i in flight:
#    print(i)
