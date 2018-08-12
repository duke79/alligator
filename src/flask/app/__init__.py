# HTTP Error Codes and their meaning: https://www.symantec.com/connect/articles/http-error-codes

from flask import Flask

app = Flask(__name__)

from app.views import graph  # /graph
