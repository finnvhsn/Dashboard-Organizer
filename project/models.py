from sqlalchemy.sql import func
from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """
    Author: Finn von Heesen
    Description: This class provides the database model for the table User.
    Date of development: 15. March 2024
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    notes = db.relationship('Note')


class Note(db.Model):
    """
    Author: Finn von Heesen
    Description: This class provides the database model for the table Note.
    Date of development: 20. April 2024
    """
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    