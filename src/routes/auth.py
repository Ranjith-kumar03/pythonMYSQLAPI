from flask import Blueprint, request
from src.database.database import db, user

auth = Blueprint("auth", __name__, url_prefix="/api/v1/stupid")


@auth.post("/register")
def register():
    username = request.json['username']
    email = request.json['email']
    _user = user(
        username=username,
        email=email
    )
    db.session.add(_user)
    db.session.commit()
    return f' {username},{email}'
