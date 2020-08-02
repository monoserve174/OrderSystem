from flask import render_template, redirect, url_for, request, flash
from app.forms import RegisterForm


def register():
    registerform = RegisterForm()
    return render_template('/auth/register.html', form=registerform)
