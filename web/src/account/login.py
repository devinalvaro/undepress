from flask_login import login_user

from .models import User


def login(email, password):
    user = User(email, password)
    login_user(user)
