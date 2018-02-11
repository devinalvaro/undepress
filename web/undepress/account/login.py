from flask_login import login_user

from db import AccountDb
from .user import User


def login(email, password):
    account_db = AccountDb()

    result = account_db.find_one(email=email, password=password)
    if result:
        user = User(result['user_id'])
        login_user(user)
        return "LOGIN_SUCCESS"
    else:
        return "LOGIN_INVALID"
