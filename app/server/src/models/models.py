from sqlalchemy.orm import backref

from server.src.models.db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    favorite_color = db.Column(db.String(60), nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'), nullable=True)
    gender = db.relationship('Gender', uselist=False, backref=backref('user', uselist=True), lazy=True)


class Gender(db.Model):
    __tablename__ = 'gender'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(20), nullable=False)


