from flask import request
from flask_login import current_user, login_required

from . import appointment
from ...lib.db import AppointmentDb


@appointment.route('/add', methods=['POST'])
@login_required
def add():
    form_data = get_form_data(request)
    insert_appointment(form_data)

    return "APPOINTMENT_ADD_SUCCESS"


def get_form_data(request):
    return dict(
        patient_id=current_user.user_id,
        expert_id=int(request.form['expert_id']),
        timestamp=request.form['timestamp'],
        location=request.form['location'],
        issue_description=request.form['issue_description'],
        status=request.form['status'])


def insert_appointment(form_data):
    AppointmentDb.insert(**form_data)
