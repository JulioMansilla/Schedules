from flask import Flask, render_template, url_for
from forms import LoginForm, RegistrationForm

#special python variable with the name of the module
app=Flask(__name__)
#The secret key requiered by WTForms
app.config['SECRET_KEY']='f0902237d035d764f7d9cd235d64d860'


#define routes
@app.route("/")
@app.route("/landing")
def landing():
    return render_template('landing.html')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)

@app.route("/about")
def about():
    return "<h1>WIP ? Wow Incomplete Programs</h1>"
