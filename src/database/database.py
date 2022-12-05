from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class user(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(41), unique=True, nullable=False)
    email = db.Column(db.String(41), unique=True, nullable=False)
    createdAt = db.Column(db.Date, default=datetime.now)
    updatedAt = db.Column(db.Date, onupdate=datetime.now)
