from bson import json_util
from flask import Blueprint
from flask_login import login_required

from ...lib.db import AccountDb

expert = Blueprint('expert', __name__, url_prefix='/expert')


@expert.route('/', methods=['GET'])
@login_required
def index():
    expert_data = get_expert_data()
    return json_util.dumps(expert_data)


def get_expert_data():
    return AccountDb.find(is_expert=True)
