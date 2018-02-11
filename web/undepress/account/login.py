from flask_login import login_user

from db import AccountDb
from .user import User


def login(email, password):
    account_db = AccountDb()

    if not account_db.find(email, password):
        return "Username or password is invalid"
    else:
        user = User(email, account_db.is_active(email))
        login_user(user)
        return "Logged in"
