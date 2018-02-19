from flask import Flask
from flask_login import LoginManager
from os import urandom

from .account import User
from .db import AccountDb

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.secret_key = urandom(24)

    login_manager.init_app(app)

    from .account import account as account_blueprint
    app.register_blueprint(account_blueprint)

    return app


@login_manager.user_loader
def load_user(user_id):
    account_db = AccountDb()
    if account_db.find_one(user_id=user_id):
        return User(user_id)
