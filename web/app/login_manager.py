from flask_login import LoginManager

from .account import User
from .db import AccountDb

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    account_db = AccountDb()
    if account_db.find_one(user_id=user_id):
        return User(user_id)
