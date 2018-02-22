from flask import Flask

from config import Config
from .login_manager import login_manager

from .account import account as account_blueprint
from .socmed import socmed as socmed_blueprint
from .userdata import userdata as userdata_blueprint
from .chat import chat as chat_blueprint


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
    app.register_blueprint(socmed_blueprint)
    app.register_blueprint(userdata_blueprint)
    app.register_blueprint(chat_blueprint)
