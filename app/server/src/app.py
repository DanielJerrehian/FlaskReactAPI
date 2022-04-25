from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from src.models.db import db
from src.models.marshmallow import ma
from src.routers.index import main


def create_app():
    app = Flask(__name__)
    CORS(app)
    load_dotenv(dotenv_path=".env")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["ENV"] = "development"
    app.config["DEBUG"] = True
    app.config["CORS_HEADERS"] = "Content-Type"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///models/database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    ma.init_app(app)
    
    app.register_blueprint(main)

    return app

