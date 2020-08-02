# import Flask App
from app import app, views, login_manager
from flask_login import login_required, current_user
# Set login page
login_manager.login_view = "login"
login_manager.login_message = "此系統需登入才能使用。"


# Set Router
# Set index router
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@login_required
def index():
    print(current_user)
    return views.index()


# Set login router
@app.route('/login', methods=['GET', 'POST'])
def login():
    print(current_user)
    return views.login()


# Set login check
@login_manager.user_loader
def user_loader(id):
    return views.user_loader(id)


@app.route('/logout', methods=['GET'])
def logout():
    return views.logout()