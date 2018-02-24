from flask import request
from flask_login import login_required

from . import monitoring
from ...lib.db import MonitoringDb


@monitoring.route('/add', methods=['POST'])
@login_required
def add():
    form_data = get_form_data(request)
    insert_monitoring(form_data)

    return "MONITORING_ADD_SUCCESS"


def get_form_data(request):
    return dict(
        user_id=int(request.form['user_id']),
        symptom_numbers=request.form['symptom_numbers'],
        timestamp=request.form['timestamp'])


def insert_monitoring(form_data):
    MonitoringDb.insert(**form_data)
