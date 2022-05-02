from flask import Flask
from dotenv import load_dotenv
import os

from server.src.network.cors import cors
from server.src.models.db import db
from server.src.models.migrate import migrate
from server.src.models.marshmallow import ma
from server.src.routers.index import main


def create_app():
    app = Flask(__name__)
    
    load_dotenv(dotenv_path=".env")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["ENV"] = "development"
    app.config["DEBUG"] = True
    app.config["CORS_HEADERS"] = "Content-Type"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///models/database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from server.src.models import models

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True) # render_as_batch because using SQLite (https://www.youtube.com/watch?v=wpRVZFwsD70)
    ma.init_app(app)
    
    app.register_blueprint(main)

    return app

