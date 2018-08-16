from app import app
from flask_cors import CORS, cross_origin
from app.data.config import Config

config = Config()

'''Run app'''
CORS(app, origins=config["allowed_domains"])  # Allow cross-domain
if config["debug"]:
    app.run(port=80, debug=True, host='0.0.0.0')
else:
    app.run(port=80)
