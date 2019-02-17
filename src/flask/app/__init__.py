# HTTP Error Codes and their meaning: https://www.symantec.com/connect/articles/http-error-codes

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.data.config import Config
from app.data.tables.alchemy_base import AlchemyBase, db_uri, db_session
from flask_migrate import Migrate

config = Config()

""" App """
## Init app
app = Flask(__name__)

## Init SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
if config["debug"]:
    app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app, model_class=AlchemyBase)
# db.create_all() # No use until the model classes are imported. Use scripts.create_db_schema instead.
from .data.tables import *
migrate = Migrate(app, db)

# @app.after_request
# def session_commit(response):
#     """
#     Ref: https://chase-seibert.github.io/blog/2016/03/31/flask-sqlalchemy-sessionless.html
#     """
#     if response.status_code >= 400:
#         return
#     try:
#         db_session.commit()
#     except DatabaseError:
#         db_session.rollback()
#         raise
#     # session.remove() is called for you by flask-sqlalchemy

""" Views """
from app.views import graph  # /graph
