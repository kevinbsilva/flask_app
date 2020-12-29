from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField, BooleanField

from wtforms.validators import DataRequired

class LoginForm(FlaskForm):

    username= TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()],description="Input your password here")
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

