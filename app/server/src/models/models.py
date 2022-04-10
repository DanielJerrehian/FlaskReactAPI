from sqlalchemy_serializer import SerializerMixin

from src.models.db import db

class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer)
    favorite_color = db.Column(db.String(60))
