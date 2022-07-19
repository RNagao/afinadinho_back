from os import environ

class Sensive_dev:
    SECRET_KEY = "fwge5hryjfyhdfdgfher"
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

class Sensive_prod:
    SECRET_KEY = environ.get('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL').replace("://", "ql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False