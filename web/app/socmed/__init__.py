from bson import json_util
from flask import Blueprint, current_app as app, request
from flask_login import current_user, login_required

from ..db import SocmedDb

socmed = Blueprint('socmed', __name__, url_prefix='/socmed')

from .add import add
from .remove import remove


@socmed.route('/', methods=['GET'])
@login_required
def index():
    user_id = current_user.user_id
    if user_id == app.config['ADMIN_ID']:
        user_id = int(request.args.get('user_id') or user_id)

    socmed_db = SocmedDb()
    return json_util.dumps(socmed_db.find(user_id=user_id))
