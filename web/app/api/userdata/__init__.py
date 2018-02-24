from bson import json_util
from flask import Blueprint, current_app as app, request
from flask_login import current_user, login_required

from ...lib.db import UserdataDb

userdata = Blueprint('userdata', __name__, url_prefix='/userdata')

from .add import add


@userdata.route('/', methods=['GET'])
@login_required
def index():
    form_data = get_form_data(request)
    return json_util.dumps(get_userdata_data(form_data))


def get_form_data(request):
    return dict(
        user_id=current_user.user_id, data_type=request.args.get('type'))


def get_userdata_data(form_data):
    return UserdataDb.find(**form_data)
