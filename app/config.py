import os
from os import path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))

load_dotenv(path.join(basedir, '.env'))


class Config:
    STATIC_FOLDER = 'static'

    HOST = '0.0.0.0'
    PORT = 5001
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True
