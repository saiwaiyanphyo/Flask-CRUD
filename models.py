from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    email = db.Column(db.String(30))
    gender = db.Column(db.String(10))

    def __init__(self, name, age, email,gender):
        self.name = name
        self.age = age
        self.email = email
        self.gender = gender