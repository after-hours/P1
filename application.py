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

login_details = None

# Set up database
engine = create_engine('postgresql://rzeznik:Chujek123@localhost/csv_test')
db = scoped_session(sessionmaker(bind=engine))

flight = db.execute("SELECT * FROM users").fetchall()
print(flight)

@app.route("/")
def index():
    return render_template("initial.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_log = request.form.get("user_log")
        pass_log = request.form.get("pass_log")

        #print(user_log)
        #print(pass_log)
        book_titles = db.execute("SELECT book_title FROM books").fetchall()
        print(book_titles)

        login_details = db.execute("SELECT * FROM users WHERE (username=:username AND password=:password)",
                                    {"username": user_log, "password": pass_log}).fetchone()
        #registered_name = login_details[1]
        #print(login_details[1])

        if login_details == None:
            print("fail")
            return render_template("login.html")
        else:
            print("works")
            return render_template("main.html", login_details=login_details, book_titles=book_titles)
        #login section code
        #1)get input from user
        #2)check weather the input is correct through the select method
        #3.1)if there is a match for the variable then allow the user to go through
        #3.2)to the main menu section
        #4.1)if there is not a match use javascript to produce an error
        #4.2)render_template login again if unsucessfull

        #db.execute()
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username_reg = request.form.get("user_input")
        password_reg = request.form.get("pass_input")
        print(username_reg)
        print(password_reg)
        db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
        {"username": username_reg, "password": password_reg})
        db.commit()
        return render_template("success_reg.html")
    else:
        return render_template("register.html")

@app.route("/main_menu", methods=["GET", "POST"])
def main_menu():
    if request.method == "GET":
        return render_template("error.html")
    else:
        return render_template("main.html")



if __name__ == '__main__':
    app.run(debug=True)
