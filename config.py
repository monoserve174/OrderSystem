import os
basedir = os.path.abspath(os.path.dirname(__name__))


# Set App Config
class Config(object):
    SECRET_KEY = 'KevinSecret_key'
    # config for sqlite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app/static/db.sqlite')
    # config for mysql
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://kevin: @localhost:3306/ordersystem'
    SQLALCHEMY_TRACK_MODIFICATIONS = False