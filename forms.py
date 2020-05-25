#import WTForms, fields, and validators.
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo

#create the class to handle the registration and login form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=24), DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=32)])
    confirm_password = PasswordField('Confirm Password', validators=[Length(min=8, max=32), DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up!')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login!')
