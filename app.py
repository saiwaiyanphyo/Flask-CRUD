from cmath import exp
from crypt import methods
import email
from email import message
from logging import exception
from urllib import request
from flask import Flask, render_template, url_for, request, redirect
from models import db, UserModel
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import text
import logging

logging.basicConfig(level=logging.DEBUG)

app  = Flask(__name__)


db_name = 'test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:asdf1234@localhost/' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

#route
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    if request.method == 'POST':
        logging.info(request)
        name = request.form['new_usr_name']
        age = request.form['new_usr_age']
        email = request.form['new_usr_email']
        gender = request.form['new_usr_gender']
        adding_user = UserModel(name, age, email, gender)
        db.session.add(adding_user)
        db.session.commit()
        message = "The record was added."
        return render_template('add.html', message=message)
    else:
        return render_template('add.html')

@app.route('/show')
def read():
    show_friend = UserModel.query.all()
    return render_template('show.html', show_friend = show_friend)

@app.route('/update/<int:id>', methods=['Get','POST'])
def update(id):
    update_user = UserModel.query.get_or_404(id)

    if request.method == 'POST':
        update_user.name = request.form['name']
        update_user.age = request.form['age']
        update_user.email = request.form['email']
        try:
            db.session.commit()
            return redirect('/show')
        except:
            return ('There was an error in updating')
    else:
        return render_template('update.html', update_user = update_user)

@app.route('/delete/<int:id>')
def delete(id):
    delete_user = UserModel.query.get_or_404(id)
    
    try:
        db.session.delete(delete_user)
        db.session.commit()
        return redirect('/show')
    except:
        return 'There is a problem in deleting'

@app.route('/')
def index():
        return render_template('index.html')
   

if __name__ == '__main__':
     app.run(port=8000, debug=True)
