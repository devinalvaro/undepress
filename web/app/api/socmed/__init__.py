from bson import json_util
from flask import Blueprint, request
from flask_login import current_user, login_required

from ...lib.db import SocmedDb

socmed = Blueprint('socmed', __name__, url_prefix='/socmed')

from .set import set


@socmed.route('/', methods=['GET'])
@login_required
def index():
    form_data = get_form_data(request)
    return json_util.dumps(get_socmed_data(form_data))


def get_form_data(request):
    return dict(user_id=current_user.user_id)


def get_socmed_data(form_data):
    return SocmedDb.find(**form_data)
