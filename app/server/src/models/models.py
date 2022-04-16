from src.models.db import db
from src.models.marshmallow import ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer)
    favorite_color = db.Column(db.String(60))


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


# class Color(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     color = db.column(db.String(60), nullable=False)


# class ColorSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Color
#         load_instance = True