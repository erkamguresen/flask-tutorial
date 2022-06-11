from flask import Blueprint, request, Response, jsonify

from src.routes import token_auth

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("", methods=["GET"])
@token_auth.login_required
def get_all_users():
    all_users = [{
        "id":1,
        "name":"bob"
    },{
        "id":2,
        "name":"marley"
    }]
    return jsonify(all_users)


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
    return Response(status=204)