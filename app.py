from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///user.db'
db= SQLAlchemy(app)

class Users(db.Model):
     id= db.Column(db.Integer,primary_key=True)
     name= db.Column(db.String(200)nullable=False)
    content= db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    data_created= db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
@app.route('/index')
def index():
    return render_template("design.html")

@app.route('/userinfo')
def userinfo():
    title="subscribe"
    title= "Add your details"
    return render_template("userinfo.html")
@app.route('/next', methods=["POST"])
def next():
    firstname= request.next.get("firstname")
    
    
    return render_template("next.html", firstname=firstname)
