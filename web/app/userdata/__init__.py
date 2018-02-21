from bson import json_util
from flask import Blueprint, current_app as app, request
from flask_login import current_user, login_required

from ..db import UserdataDb

userdata = Blueprint('userdata', __name__, url_prefix='/userdata')

from .add import add


@userdata.route('/', methods=['GET'])
@login_required
def index():
    user_id = current_user.user_id
    if user_id == app.config['ADMIN_ID']:
        user_id = int(request.args.get('user_id') or user_id)
    data_type = request.args.get('type')

    userdata_db = UserdataDb()
    return json_util.dumps(
        userdata_db.find(user_id=user_id, data_type=data_type))
