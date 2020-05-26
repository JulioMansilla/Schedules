from flask import Flask, render_template, url_for, flash, redirect
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
