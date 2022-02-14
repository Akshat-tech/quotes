from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Akshat1707?@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://heatuwedqwjkrf:9508249c5ff3fdc5b2278218d02ac7c086edb426187302a31c55dae0e1807a53@ec2-3-222-49-168.compute-1.amazonaws.com:5432/d7tnhq3ji33dek'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) ## db is a instance of SQLAlchemy

class Favquotes(db.Model): ## This class will create a database table Favquotes using db
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all() ##fetch all records from database and store it in result variable
    return render_template('index.html',result=result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))
