from bson import json_util
from flask import Blueprint, request
from flask_login import current_user, login_required

from ...lib.db import MonitoringDb

monitoring = Blueprint('monitoring', __name__, url_prefix='/monitoring')


@monitoring.route('', methods=['GET'])
@login_required
def index():
    form_data = get_form_data(request)
    monitoring_data = get_monitoring_data(form_data)
    return json_util.dumps(monitoring_data)


def get_form_data(request):
    return dict(user_id=current_user.user_id)


def get_monitoring_data(form_data):
    return MonitoringDb.find(**form_data)
