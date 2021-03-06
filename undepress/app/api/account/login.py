from flask import request

from . import account
from ...lib.db import AccountDb
from ...lib.password import hash_password
from ...lib.token import encode_token, set_token


@account.route('/login', methods=['POST'])
def login():
    form_data = get_form_data(request)
    user_id = get_user_id(form_data)

    if user_id is not None:
        token = encode_token(user_id)
        set_token(user_id, token)
        return token
    else:
        return "ACCOUNT_LOGIN_INVALID", 403


def get_form_data(request):
    email = request.form['email']
    password = hash_password(request.form['password'])
    return dict(email=email, password=password)


def get_user_id(form_data):
    result = AccountDb.find_one(**form_data)
    return result['user_id'] if (result is
                                 not None) and ('user_id' in result) else None
