from flask import render_template, request
from flask_login import login_user

from . import account
from .user import User
from ..db import AccountDb


@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        account_db = AccountDb()
        result = account_db.find_one(email=email, password=password)
        if result:
            user = User(result['user_id'])
            login_user(user)

            return "ACCOUNT_LOGIN_SUCCESS"
        else:
            return "ACCOUNT_LOGIN_INVALID"
