from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import LoginForm, RegistrationForm
from flask_bcrypt import Bcrypt
#special python variable with the name of the module
app=Flask(__name__)
#The secret key requiered by WTForms
app.config['SECRET_KEY']='f0902237d035d764f7d9cd235d64d860'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#define database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    #                           \/ python class in line 26
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
                                        #this calls the database TABLE
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
        #hash form.password.data and decode the object to a utf-8 string
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #create an instance of the User object and pass it the form data and hashed password
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        #add the user object to the session
        db.session.add(new_user)
        #commit the new_user object to the database (inserts a row to our user table inside site.db)
        #Remember you can always wipe your tables completely by calling the db.drop_all() method!
        db.session.commit()

        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('landing'))
    return render_template('register.html', form=form)

@app.route("/about")
def about():
    return "<h1>WIP ? Wow Incomplete Programs</h1>"
