from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()  

class Players():
    __tablename__ = "players"
    players_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    DOB = db.Column(db.DateTime)
    favourite_game = db.Column(db.String(64))
    phonenumber = db.Column(db.String(64))
    phonetype = db.Column(db.String(50))
    username = db.Column(db.String(64))
    password = db.Column(db.String(255))

    # Assigning the values to the database fields
    def __init__(self,first_name, last_name, DOB, phonenumber,phonetype,favourite_game, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.phonetype = phonetype
        self.username = username
        self.password = password
        self.DOB = DOB
        self.phonenumber = phonenumber
        self.favourite_game = favourite_game

    # Checking the authentication of the user
    def is_authenticated(self):
        return True