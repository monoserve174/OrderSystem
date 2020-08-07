# Load Package
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from datetime import datetime
# Load app config
from config import Config

# Create Flask App
app = Flask(__name__)
# import app config
app.config.from_object(Config)
# Create bootstrap template for app
bootstrap = Bootstrap(app)
# Create db for app
db = SQLAlchemy(app)
# Create migrate for app and db
migrate = Migrate(app, db)
# Create login_manager for app
login_manager = LoginManager(app)


# import db
from app.models import *

# import router
from app.router import *
