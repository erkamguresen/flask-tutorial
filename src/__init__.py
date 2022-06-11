__version__ = '0.1.0'

from flask import Flask

from src.extensions import db
from src.routes.auth import auth_bp
from src.routes.error import error_bp
from src.routes.groups import groups_bp
from src.routes.health import health_bp
from src.routes.users import users_bp


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = \
        "postgresql://sergio:my-password@localhost:5432/backenddb"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)
    # be careful it creates the table each time, so use for unit tests only
    db.create_all()

    app.register_blueprint(auth_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(groups_bp)
    app.register_blueprint(error_bp)
    return app
