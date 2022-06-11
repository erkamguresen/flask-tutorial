import jwt
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash

from src import db
from src.dto.credentials import CredentialsSchema
from sqlalchemy import select

from src.models.user import User
from src.routes import secret_token

auth_bp = Blueprint("auth", __name__)
credentials_schema = CredentialsSchema()


@auth_bp.route("/login", methods=["POST"])
def login():
    d = request.json

    if "username" not in d or "password" not in d:
        raise RuntimeError("Unable to authenticate.")

    credentials = credentials_schema.load(d)

    user = db.session.scalars(select(User).where(User.username == credentials.username)).one()
    if not check_password_hash(user.password, credentials.password):
        raise RuntimeError("Invalid password")

    encoded_jwt = jwt.encode({"sub": user.id, "username": user.username}, secret_token, algorithm="HS512")
    return jsonify({"token": encoded_jwt})