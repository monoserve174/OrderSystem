from flask import render_template, redirect, url_for, request, flash
from app.models import *
from app.forms import LoginForm
from flask_login import login_user, logout_user, current_user


# Set login views
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        user = User.query.filter_by(username=loginform.username.data).first()
        if user:
            if user.check_hash_pwd(loginform.password.data):
                login_user(user)
                next_url = request.args.get('next')
                return redirect(next_url or url_for('index'))
            else:
                flash('帳號或密碼錯誤')
                return redirect(url_for('login'))
        else:
            flash('帳號或密碼錯誤')
            return redirect(url_for('login'))
    return render_template('auth/login.html', form=loginform)


# Set login check
def user_loader(id):
    return User.read(id)


# Set logout views
def logout():
    logout_user()
    flash('登出成功，請重新登入。')
    return redirect(url_for('login'))