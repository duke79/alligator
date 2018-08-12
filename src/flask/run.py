from app import app
from flask_cors import CORS, cross_origin
from app.data.config import Config

config = Config()

'''Run app'''
CORS(app, origins=config["allowed_domains"])  # Allow cross-domain
app.run(port=5000, debug=config["debug"])
