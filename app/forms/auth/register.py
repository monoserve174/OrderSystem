from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('帳號(Login Name)', validators=[DataRequired()])
    email = EmailField('信箱(Email)', validators=[DataRequired(), Email(message='請輸入正確信箱格式')])
    password = PasswordField('密碼(Password)', validators=[DataRequired()])
    check_password = PasswordField('確認密碼(Password)', validators=[EqualTo('password')])
    submit = SubmitField('註冊')
