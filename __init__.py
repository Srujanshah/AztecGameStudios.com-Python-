from flask import Flask,render_template,request,url_for,redirect,session
from flask_sqlalchemy import SQLAlchemy
from models import Players,db
import os
import datetime

# Initializing the Flask 
app = Flask(__name__)
app.secret_key = os.urandom(24)
db_uri = 'mysql://agsroot:ags@db:3306/aztecgamestudios'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Giving routes to different pages

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/home")
def home():
    return render_template("main.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/games")
def games():
    # Countdown for the days to the Release Date
    delta = datetime.datetime(2018,12,31) - datetime.datetime.now()
    days_left = delta.days
    return render_template("games.html", days_left = days_left)

@app.route("/login")
def login():
    return render_template("login.html")

# Task to do after the click of the Login Button
@app.route("/loginAction", methods=['POST','GET'])
def loginAction():
    if request.method == 'POST':
        usr = request.form['username']
        pwd = request.form['password']
        if usr is not None:
            player = Players.query.filter(Players.username == usr).first()
        if player.password == pwd:
            session['username'] = usr
            return render_template("hello.html", username = session['username'])
        else:
            session['username'] = None
            flash("Invalid Username or Password")
            return redirect(url_for('login'))

# Action to be taken on the click of Register Button
@app.route("/registerAction", methods=['POST'])
def registerAction():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        DOB = request.form['DOB']
        favourite_game = request.form['favourite_game']
        phonenumber = request.form['phonenumber']
        phonetype = request.form.get('phonetype')
        username = request.form['username']
        password = request.form['password']
        usr = Players(first_name, last_name, DOB, favourite_game, phonenumber, phonetype, username, password)
        db.session.add(usr)
        db.session.commit()
        session['username'] = username
    return render_template("hello.html", username = session['username'])


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)