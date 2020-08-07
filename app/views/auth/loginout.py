from flask import render_template, redirect, url_for, request, flash
from app.models import *
from flask_login import login_user, logout_user, current_user


# Set login views
def login():
    if request.method == "POST":
        username = request.form.get('username')
        if User.query.filter_by(username=username).first():
            user = User.query.filter_by(username=username).first()
            if user.check_hash_pwd(pwd=request.form.get('password')):
                logout_user(user)
                return redirect(url_for('index'))
        flash('帳號或密碼錯誤！！')
        return render_template('auth/login.html')
    return render_template('auth/login.html')


# Set login check
def user_loader(id):
    return User.read(id)


# Set logout views
def logout():
    logout_user()
    flash('登出成功，請重新登入。')
    return redirect(url_for('login'))