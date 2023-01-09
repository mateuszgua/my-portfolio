from app import config

import os
from flask import Flask
from flask_mail import Mail
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
mail = Mail(app)
CORS(app)

if app.config["ENV"] == "production":
    app.config.from_object('app.config.ProductionConfig')
elif app.config["ENV"] == "testing":
    app.config.from_object('app.config.TestingConfig')
else:
    app.config.from_object('app.config.DevelopmentConfig')


from app import views, form