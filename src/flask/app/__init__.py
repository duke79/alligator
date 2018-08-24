# HTTP Error Codes and their meaning: https://www.symantec.com/connect/articles/http-error-codes

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.data.config import Config

""" App """
## Init app
app = Flask(__name__)
## Init SQLAlchemy
def create_session(engine):
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()
    session._model_changes = {}
    return session
config = Config()["database"]["mysql"]
db_uri = "mysql+pymysql://{0}:{1}@{2}:3306/{3}" \
    .format(config["user"], config["password"], config["host"], config["db"])
# db_uri = "sqlite:///sqlalchemy_example.db"
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)
db_session = create_session(db.engine)
# db.create_all() # No use until the model classes are imported. Use scripts.create_db_schema instead.

""" Views """
from app.views import graph  # /graph
