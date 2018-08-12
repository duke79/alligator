# HTTP Error Codes and their meaning: https://www.symantec.com/connect/articles/http-error-codes

from flask import Flask

app = Flask(__name__)

from app.views import auth  # /api/auth
from app.views import user  # /api/user
from app.views import graph  # /graph
