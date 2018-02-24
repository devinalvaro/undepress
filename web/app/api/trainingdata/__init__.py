from bson import json_util
from flask import Blueprint, current_app as app
from flask_login import current_user, login_required

from ...lib.db import TrainingdataDb

trainingdata = Blueprint('trainingdata', __name__, url_prefix='/trainingdata')

from .add import add


@trainingdata.route('/', methods=['GET'])
@login_required
def index():
    form_data = {}
    if current_user.user_id == app.config['ADMIN_ID']:
        return json_util.dumps(get_trainingdata_data(form_data))
    else:
        return None


def get_trainingdata_data(form_data):
    return TrainingdataDb.find(**form_data)
