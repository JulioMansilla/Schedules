from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import LoginForm, RegistrationForm

#special python variable with the name of the module
app=Flask(__name__)
#The secret key requiered by WTForms
app.config['SECRET_KEY']='f0902237d035d764f7d9cd235d64d860'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#define database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(32), nullable=False)
    periods = db.relationship('Periods', backref='owner', lazy=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
class Periods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False);
    room = db.Column(db.String(50), nullable = False);
    teacher = db.Column(db.String(100), nullable = False);
    time = db.Column(db.String(20), nullable = False);
    day = db.Column(db.String(25), nullable = False);
    color = db.Column(db.String(30), nullable = False);
    period = db.Column(db.SmallInteger, nullable = False);
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Periods('{self.name}', '{self.room}', '{self.teacher}', '{self.time}', '{self.period}')"
#define routes
@app.route("/")
@app.route("/landing")
def landing():
    return render_template('landing.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    #Hardcoded test case, we will remove it after we implement sql
    if form.validate_on_submit():
        if form.email.data == 'bob@bob.com' and form.password.data == 'bobster123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('landing'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('landing'))
    return render_template('register.html', form=form)

@app.route("/about")
def about():
    return "<h1>WIP ? Wow Incomplete Programs</h1>"
