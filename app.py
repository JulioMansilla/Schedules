from flask import Flask, render_template

#special python variable with the name of the module
app=Flask(__name__)


#define routes
@app.route("/")
@app.route("/landing")
def landing():
    return render_template('landing.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')
