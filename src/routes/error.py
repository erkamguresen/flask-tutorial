import traceback

from flask import Blueprint, jsonify
from marshmallow import ValidationError
from werkzeug.exceptions import NotFound

error_bp = Blueprint("errors", __name__)


@error_bp.app_errorhandler(ValidationError)
def handle_validation_error(err):
    print(traceback.format_exc())
    return jsonify({"message": "Incorrect data format."}), 400


@error_bp.app_errorhandler(RuntimeError)
def handle_value(err):
    print(type(err.args))
    return jsonify({"message": err.args[0]}), 401


@error_bp.app_errorhandler(NotFound)
def handle_not_found(err):
    return jsonify({"message": "This resource isn't available."}), 404


@error_bp.app_errorhandler(Exception)
def handle_generic_exception(err):
    print(type(err))
    print(err)
    return jsonify({"message": "Unknown error. Please check the logs for more details."}), 500
