from flask_login import login_user

from db import AccountDb
from .user import User


def login(email, password):
    account_db = AccountDb()

    if not account_db.find(email, password):
        return "LOGIN_INVALID"
    else:
        user = User(email)
        login_user(user)
        return "LOGIN_SUCCESS"
