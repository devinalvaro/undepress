from flask_login import LoginManager

from .account import User
from .db import AccountDb

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    if does_account_exist(user_id):
        return User(user_id)


def does_account_exist(user_id):
    return AccountDb.find_one(user_id=user_id)
