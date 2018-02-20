from bson import json_util
from flask import Blueprint, current_app as app, request
from flask_login import current_user, login_required

from ..db import AccountDb

from .user import User

account = Blueprint('account', __name__, url_prefix='/account')

from .login import login
from .register import register
from .logout import logout


@account.route('/', methods=['GET'])
@login_required
def get():
    user_id = current_user.user_id
    if user_id == app.config['ADMIN_ID']:
        user_id = int(request.args.get('user_id') or user_id)

    account_db = AccountDb()
    return json_util.dumps(account_db.find(user_id=user_id))
