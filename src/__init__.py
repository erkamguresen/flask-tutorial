__version__ = '0.1.0'

from flask import Flask

from src.routes.error import error_bp
from src.routes.health import health_bp
from src.routes.users import users_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(error_bp)
    return app
