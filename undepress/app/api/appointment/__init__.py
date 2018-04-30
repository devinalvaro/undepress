from bson import json_util
from flask import Blueprint, request
from flask_login import current_user, login_required

from ...lib.db import AccountDb, AppointmentDb

appointment = Blueprint('appointment', __name__, url_prefix='/appointment')

from .add import add
from .set import set


@appointment.route('', methods=['GET'])
@login_required
def index():
    form_data = get_form_data(request)
    appointment_data = get_appointment_data(form_data)
    return json_util.dumps(appointment_data)


def get_form_data(request):
    user_id = current_user.user_id

    if is_expert(user_id):
        return dict(expert_id=user_id)
    else:
        return dict(patient_id=user_id)


def is_expert(user_id):
    return AccountDb.find_one(user_id=user_id)['is_expert'] is not None


def get_appointment_data(form_data):
    return AppointmentDb.find(**form_data)
