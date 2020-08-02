from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('帳號(Login Name)', validators=[DataRequired()])
    password = PasswordField('密碼(Password)', validators=[DataRequired()])
    submit = SubmitField('登入')
