from flask import Blueprint, request, Response, jsonify
from sqlalchemy import select, insert
from werkzeug.security import generate_password_hash

from src import db
from src.entities.user import User
from src.routes import token_auth

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("", methods=["GET"])
@token_auth.login_required
def get_all_users():
    # all_users = [{
    #     "id":1,
    #     "name":"bob"
    # },{
    #     "id":2,
    #     "name":"marley"
    # }]

    # style 1.X
    # all_users = User.query.all()

    # style 2.0
    users = db.session.scalars(select(User)).all()
    # return jsonify(all_users)
    return jsonify([{"id": u.id, "username": u.username} for u in users])


@users_bp.route("", methods=["POST"])
@token_auth.login_required
def create_user():
    d = request.json
    print(d)
    # print(request.data)
    # print(request.headers)
    # print(request.method)
    # print(request.files)
    # print(request.args)

    # style 1.X
    # u = User()
    # u.username = d["username"]
    # u.email = d["email"]
    # u.password = generate_password_hash(d["password"])
    # db.session.add(u)

    # style 2.0
    try:
        db.session.execute(
            insert(User).values(username=d["username"], email=d["email"],
                                password=generate_password_hash(d["password"])))
        db.session.commit()
        print("added")
    except Exception as e:
        print(e)

    # return Response(status=204)
    return jsonify({
        "username": d["username"],
        "email" : d["email"]
    }), 201


@users_bp.route("/<user_id>", methods=["GET"])
@token_auth.login_required
def get_user(user_id):
    # style 1.X
    # u = User.query.filter(User.id == user_id).one()

    # style 2.0
    user = db.session.scalars(select(User).where(User.id == user_id)).one()
    return jsonify({
        "id": user.id,
        "username": user.username
    })
