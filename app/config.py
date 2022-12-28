import os
from os import path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))

load_dotenv(path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", default=None)
    STATIC_FOLDER = 'static'

    HOST = '0.0.0.0'
    PORT = 5050
    DEBUG = False
    TESTING = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True
