from flask import render_template, redirect, url_for, request, flash, jsonify
from app.models import User


def register():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
    return render_template('/auth/register.html')


# 驗證註冊帳號
def validate_register_username():
    username = request.form.get('username')
    if User.query.filter_by(username=username).first():
        return jsonify(False)
    return jsonify(True)


# 驗證註冊信箱
def validate_register_email():
    email = request.form.get('email')
    if User.query.filter_by(email=email).first():
        return jsonify(False)
    return jsonify(True)
