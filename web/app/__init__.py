from flask import Flask
from flask_login import LoginManager

from config import Config
from .account import User
from .db import AccountDb

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    login_manager.init_app(app)

    from .account import account as account_blueprint
    app.register_blueprint(account_blueprint)

    from .socmed import socmed as socmed_blueprint
    app.register_blueprint(socmed_blueprint)

    from .userdata import userdata as userdata_blueprint
    app.register_blueprint(userdata_blueprint)

    from .chat import chat as chat_blueprint
    app.register_blueprint(chat_blueprint)

    return app


@login_manager.user_loader
def load_user(user_id):
    account_db = AccountDb()
    if account_db.find_one(user_id=user_id):
        return User(user_id)
