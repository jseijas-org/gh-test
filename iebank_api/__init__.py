from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os
app = Flask(__name__)
load_dotenv()
# Select environment based on the DEBUG environment variable
if os.getenv('ENV') == 'dev':
    print("Running in development mode")
    app.config.from_object('config.DevelopmentConfig')
elif os.getenv('ENV') == 'ghci':
    print("Running in github mode")
    app.config.from_object('config.GithubCIConfig')
else:
    print("Running in production mode")
    app.config.from_object('config.ProductionConfig')
db = SQLAlchemy(app)
from iebank_api.models import Account
db.create_all()
CORS(app)

from iebank_api import routes