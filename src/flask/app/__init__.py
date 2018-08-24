# HTTP Error Codes and their meaning: https://www.symantec.com/connect/articles/http-error-codes

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.data.config import Config

""" App """
## Init app
app = Flask(__name__)
## Init SQLAlchemy
config = Config()["database"]["mysql"]
db_uri = "mysql+pymysql://{0}:{1}@{2}:3306/{3}" \
    .format(config["user"], config["password"], config["host"], config["db"])
# db_uri = "sqlite:///sqlalchemy_example.db"
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)
# db.create_all() # No use until the model classes are imported. Use scripts.create_db_schema instead.

""" Views """
from app.views import graph  # /graph
