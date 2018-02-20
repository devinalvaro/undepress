from flask import Blueprint, request

from ..db import AccountDb

from .user import User

account = Blueprint('account', __name__, url_prefix='/account')

from .login import login
from .register import register
from .logout import logout


@account.route('/', methods=['GET'])
def get():
    user_id = request.args['user_id']

    account_db = AccountDb()
    return account_db.find(user_id=user_id)
