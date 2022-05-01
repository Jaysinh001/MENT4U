from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/spammers"

db = SQLAlchemy(app)

class Contact(db.Model):
    sr_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    feedback = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(20))


class Coarses(db.Model):
    sr_no = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=False, nullable=False)
    slug = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(250), nullable=False)
    link = db.Column(db.String(30), nullable=False)
    image = db.Column(db.String(30), nullable=True)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/carrierChoice')
def carrierChoice():
    return render_template('carrierChoice.html')


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        feedback = request.form.get('feedback')
        entry = Contact(name=name, phone = phone, feedback = feedback, date= datetime.now(),email = email)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')




@app.route('/coarses')
def coarses():
    return render_template('courses.html')



@app.route('/scholarship')
def scholarships():
    return render_template('scholarship.html')


@app.route('/cse_it')
def cse_it():
    return render_template('cse_it.html')


@app.route('/electrical')
def electrical():
    return render_template('electrical.html')


@app.route('/software')
def software():
    return render_template('software.html')


if __name__ == "__main__":
    app.run(debug=True)