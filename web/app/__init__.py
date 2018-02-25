from flask import Flask

from config import Config
from .login_manager import login_manager

from .api import account_blueprint
from .api import appointment_blueprint
from .api import chat_blueprint
from .api import monitoring_blueprint
from .api import socmed_blueprint


def create_app():
    app = Flask(__name__)

    init_config(app)
    init_login_manager(app)

    register_blueprints(app)

    return app


def init_config(app):
    app.config.from_object(Config)
    Config.init_app(app)


def init_login_manager(app):
    login_manager.init_app(app)


def register_blueprints(app):
    app.register_blueprint(account_blueprint)
    app.register_blueprint(appointment_blueprint)
    app.register_blueprint(chat_blueprint)
    app.register_blueprint(monitoring_blueprint)
    app.register_blueprint(socmed_blueprint)
