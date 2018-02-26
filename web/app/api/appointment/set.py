from flask import request
from flask_login import current_user, login_required

from . import appointment
from ...lib.db import AppointmentDb


@appointment.route('/set', methods=['POST'])
@login_required
def set():
    form_data = get_form_data(request)
    set_appointment(form_data)

    return "APPOINTMENT_SET_SUCCESS"


def get_form_data(request):
    form_data = dict(
        patient_id=request.form.get('patient_id'),
        expert_id=request.form.get('expert_id'),
        status=request.form['status'])

    fill_patient_id_or_expert_id(form_data)

    ensure_ids_are_integers(form_data)

    return form_data


def fill_patient_id_or_expert_id(form_data):
    if form_data['patient_id'] is None:
        form_data['patient_id'] = current_user.user_id
    elif form_data['expert_id'] is None:
        form_data['expert_id'] = current_user.user_id


def ensure_ids_are_integers(form_data):
    form_data['patient_id'] = int(form_data['patient_id'])
    form_data['expert_id'] = int(form_data['expert_id'])


def set_appointment(form_data):
    query = dict(
        patient_id=form_data['patient_id'], expert_id=form_data['expert_id'])
    update = dict(status=form_data['status'])
    AppointmentDb.set(query, **update)
