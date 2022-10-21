from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class SignupForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    password = PasswordField('Password', validators= [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit_button = SubmitField('Create my Account')


class LoginForm(FlaskForm):
    email  = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class Contact(FlaskForm):
    first_name = StringField('fname', validators=[DataRequired()])
    last_name = StringField('lname', validators=[DataRequired()])
    phone_number = StringField('number', validators=[DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    subject1 = StringField('subject1', validators=[DataRequired()])
    subject2 = StringField('subject2', validators=[DataRequired()])
    subject3 = StringField('subject3', validators=[DataRequired()])
    personal = StringField('personal', validators=[DataRequired()])
    submit = SubmitField('Submit')

    