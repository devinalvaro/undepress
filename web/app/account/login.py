from flask import render_template, request
from flask_login import login_user

from . import account
from .user import User
from ..db import AccountDb


@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    form_data = get_form_data(request)

    account_db = AccountDb()
    result = account_db.find_one(**form_data)
    if result:
        user = User(result['user_id'])
        login_user(user)

        return "ACCOUNT_LOGIN_SUCCESS"
    else:
        return "ACCOUNT_LOGIN_INVALID"


def get_form_data(request):
    return dict(email=request.form['email'], password=request.form['password'])
