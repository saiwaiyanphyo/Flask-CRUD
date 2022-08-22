from crypt import methods
import email
from email import message
from logging import exception
from urllib import request
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app  = Flask(__name__)

db_name = 'test'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:asdf1234@localhost/' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

#database connection 
class friends(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.String, primary_key=True)
    user_name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String)
    gender = db.Column(db.String)

    def __init__(self, user_id, user_name, age, email,gender):
        self.id = user_id
        self.name = user_name
        self.age = age
        self.email = email
        self.gender = gender

#route
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        add_usr_id = request.form['new_usr_id']
        add_usr_name = request.form['new_usr_name']
        add_usr_age = request.form['new_usr_age']
        add_usr_email = request.form['new_usr_email']
        add_usr_gender = request.form['new_usr_gender']
        commit_user = friends(add_usr_id, add_usr_name, add_usr_age, add_usr_email, add_usr_gender)
        db.session.add(commit_user)
        db.session.commit()
        message = "The record for {add_usr_name} was added."
        return render_template('add.html', message=message)
    else:
        return render_template('add.html')

@app.route('/show')
def read():
    show_friend = friends.query.all()
    return render_template('show.html', show_friend = show_friend)

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/')
def index():
        return ('This is index')
   

if __name__ == '__main__':
     app.run(port=8000, debug=True)
