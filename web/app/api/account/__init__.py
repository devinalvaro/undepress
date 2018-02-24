from bson import json_util
from flask import Blueprint, current_app as app, request
from flask_login import current_user, login_required

from ...lib.db import AccountDb

account = Blueprint('account', __name__, url_prefix='/account')

from .login import login
from .logout import logout
from .register import register
from ...lib.user import User


@account.route('/', methods=['GET'])
@login_required
def index():
    form_data = get_form_data(request)
    return json_util.dumps(get_account_data(form_data))


def get_form_data(request):
    user_id = current_user.user_id
    if user_id == app.config['ADMIN_ID']:
        user_id = int(request.args.get('user_id') or user_id)

    return dict(user_id=user_id)


def get_account_data(form_data):
    return AccountDb.find(**form_data)
