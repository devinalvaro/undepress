from flask_login import login_user

from .models import User


def login(email, password):
    # TODO: implement db
    # return db.query.get(email)

    user = User(email, password)
    login_user(user)
