from flask import render_template, redirect, url_for, request, flash


# Set index views
def index():
    return render_template('index.html')
