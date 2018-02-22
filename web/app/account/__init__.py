from bson import json_util
from flask import Blueprint, current_app as app, request
from flask_login import current_user, login_required

from ..db import AccountDb

account = Blueprint('account', __name__, url_prefix='/account')

from .login import login
from .logout import logout
from .register import register
from .user import User


@account.route('/', methods=['GET'])
@login_required
def get():
    form_data = get_form_data(request)

    account_db = AccountDb()
    return json_util.dumps(account_db.find(**form_data))


def get_form_data(request):
    user_id = current_user.user_id
    if user_id == app.config['ADMIN_ID']:
        user_id = int(request.args.get('user_id') or user_id)

    return dict(user_id=user_id)
