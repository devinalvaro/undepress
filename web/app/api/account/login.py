from flask import render_template, request
from flask_login import login_user

from . import account
from .user import User
from ...db import AccountDb


@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    form_data = get_form_data(request)
    user_id = get_user_id(form_data)
    if user_id:
        login_user(User(user_id))

        return "ACCOUNT_LOGIN_SUCCESS"
    else:
        return "ACCOUNT_LOGIN_INVALID"


def get_form_data(request):
    return dict(email=request.form['email'], password=request.form['password'])


def get_user_id(form_data):
    result = AccountDb.find_one(**form_data)
    return result['user_id'] if result else None
